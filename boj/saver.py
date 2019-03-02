from os.path import join
import os
import sqlite3


class Saver:

    def __init__(self, home=None):
        if home is None:
            self.home = join('.')
        else:
            self.home = home
            if not os.path.isdir(home):
                os.mkdir(home)

        self.db = join(self.home, 'info.db')
        self.create()

    def create(self):
        """
        Create Database Table

        ::Table::
        problem:
            # Algorithm problem in boj
            id           Integer, Primary key           : problem id
            confirm      Integer, Default 0             : whether this problem is already checked or not
            title        VARCHAR(50)                    : problem's title
            limit_time   VARCHAR(20)                    : problem's limited time
            limit_memory VARCHAR(20)                    : problem's limited memory
            category     VARCHAR(50)                    : problem's category
            description  text                           : problem's description
            input        text                           : problem's input description
            output       text                           : problem's output description

        marking:
            # unknown user's solution
            id        Integer, Primary key              : solution id
            problem   Integer, Foreign key(problem(id)) : foreign key for problem id
            success   VARCHAR(50)                       : whether problem is solved or not
            memory    Integer                           : used memory for solving problem
            language  VARCHAR(50)                       : language for solving problem
            time      Integer                           : used time for solving problem
            length    Integer                           : submitted code's byte

        solution:
            # user's solution
            id        Integer, Primary key              : solution id
            problem   Integer, Foreign key(problem(id)) : foreign key for problem id
            success   VARCHAR(50)                       : whether problem is solved or not
            memory    Integer                           : used memory for solving problem
            language  VARCHAR(50)                       : language for solving problem
            time      Integer                           : used time for solving problem
            length    Integer                           : submitted code's byte

        """
        with sqlite3.connect(self.db) as conn:
            cur = conn.cursor()
            queries = (
                'CREATE TABLE IF NOT EXISTS problem (' \
                'id INTEGER PRIMARY KEY NOT NULL,' \
                'confirm INTEGER,' \
                'title VARCHAR (50),' \
                'limit_time VARCHAR (20),' \
                'limit_memory VARCHAR (20),' \
                'category VARCHAR (50),' \
                'description text,' \
                'input text,' \
                'output text' \
                ')',
                'CREATE TABLE IF NOT EXISTS marking (' \
                'id INTEGER PRIMARY KEY NOT NULL,' \
                'problem INTEGER NOT NULL,' \
                'success VARCHAR(50),' \
                'memory INTEGER,' \
                'language VARCHAR (50),' \
                'time INTEGER,' \
                'length INTEGER,' \
                'foreign key(problem) references problem(id)' \
                ')',
                'CREATE TABLE IF NOT EXISTS solution (' \
                'id INTEGER PRIMARY KEY NOT NULL,' \
                'problem INTEGER NOT NULL,' \
                'success VARCHAR(50),' \
                'memory INTEGER,' \
                'language VARCHAR (50),' \
                'time INTEGER,' \
                'length INTEGER,'
                'foreign key(problem) references problem(id)' \
                ')'
            )
            for query in queries:
                cur.execute(query)
            conn.commit()

    def execute_select_query(self, query, param=None):
        """
        Execute 'select' query

        :param param:  param for query
        :param query:  'select' query
        :return:       Query result
        """

        try:
            with sqlite3.connect(self.db) as conn:
                cur = conn.cursor()
                if param is not None:
                    cur.execute(query, param)
                else:
                    cur.execute(query)

                rows = cur.fetchall()
                conn.commit()
            return rows
        except:
            # No result
            return None

    def execute_insert_query(self, query, data):
        """
        Execute 'insert' query

        :param data:   data to insert
        :param query:  'insert' query
        :return:       whether query success or not
        """

        try:
            with sqlite3.connect(self.db) as conn:
                cur = conn.cursor()
                cur.execute(query, data)
                conn.commit()
            return True
        except:
            return False

    """
    TABLE Problem's Function
    
    """

    def insert_problem_info(self, info):
        """
        Insert problem table's information

        ::Table::
        problem:
            # Algorithm problem in boj
            id           Integer, Primary key           : problem id
            confirm      Integer, Default 0             : whether this problem is already checked or not
            limit_time   VARCHAR(20)                    : problem's limited time
            limit_memory VARCHAR(20)                    : problem's limited memory
            title        VARCHAR(50)                    : problem's title
            category     VARCHAR(50)                    : problem's category
            description  text                           : problem's description
            input        text                           : problem's input description
            output       text                           : problem's output description

        :param info: Problem's info to insert
        :return:     Whether query success or not
        """

        query = 'insert into problem (id, confirm, limit_time, limit_memory, title, category, description, input, output) ' \
                'values (?, ?, ?, ?, ?, ?, ?, ?, ?)'
        data = (
            info['id'],
            info['confirm'],
            info['limit_time'],
            info['limit_memory'],
            info['title'],
            info['category'],
            info['description'],
            info['input'],
            info['output']
        )
        return self.execute_insert_query(query, data=data)

    def load_all_problem_info(self):
        """
        Load problem table's information
        :return:
        """
        query = 'select * from problem'
        return self.execute_select_query(query)

    def check_problem(self, problem_id):
        """
        Check whether id is already in problem table

        :param problem_id:  id to check whether it is in database or not
        :return:            check result
        """

        query = 'select * from problem where id=?'
        return self.execute_select_query(query, param=(problem_id,))

    """
    TABLE Marking's Function
    
    """

    def insert_marking_info(self, info):
        """
        Save marking table's information

        ::Table::
        marking:
            # unknown user's solution
            id        Integer, Primary key              : solution id
            problem   Integer, Foreign key(problem(id)) : foreign key for problem id
            success   VARCHAR(50)                       : whether problem is solved or not
            memory    Integer                           : used memory for solving problem
            language  VARCHAR(50)                       : language for solving problem
            time      Integer                           : used time for solving problem
            length    Integer                           : submitted code's byte

        :param info:
        :return:
        """
        query = 'insert into marking (id, problem, success, memory, language, time, length) ' \
                'values (?, ?, ?, ?, ?, ?, ?)'
        data = (
            info['id'],
            info['problem'],
            info['success'],
            info['memory'],
            info['language'],
            info['time'],
            info['length']
        )
        return self.execute_insert_query(query, data=data)

    def load_marking(self):
        """
        Load marking table's information
        :return:
        """
        query = 'select * from marking'
        return self.execute_select_query(query)

    def check_marking(self, marking_id):
        """
        Check whether id is already in marking table

        :param marking_id:  id to check whether it is in database or not
        :return:            check result
        """

        query = 'select * from marking where id = ?'
        return self.execute_select_query(query, marking_id)

    """
    TABLE Solution's Function
    
    """

    def insert_solution_info(self, info):
        """
        Save solution table's information

        ::Table::
        marking:
            # unknown user's solution
            id        Integer, Primary key              : solution id
            problem   Integer, Foreign key(problem(id)) : foreign key for problem id
            success   VARCHAR(50)                       : whether problem is solved or not
            memory    Integer                           : used memory for solving problem
            language  VARCHAR(50)                       : language for solving problem
            time      Integer                           : used time for solving problem
            length    Integer                           : submitted code's byte

        :param info:
        :return:
        """
        query = 'insert into solution (id, problem, success, memory, language, time, length) ' \
                'values (?, ?, ?, ?, ?, ?, ?)'
        data = (
            info['id'],
            info['problem'],
            info['success'],
            info['memory'],
            info['language'],
            info['time'],
            info['length']
        )
        return self.execute_insert_query(query, data=data)

    def load_solution(self):
        """
        Load marking table's information
        :return:
        """
        query = 'select * from solution'
        return self.execute_select_query(query)

    def check_solution(self, solution_id):
        """
        Check whether id is already in solution table

        :param solution_id: id to check whether it is in database or not
        :return:            check result
        """

        query = 'select * from solution where id = ?'
        return self.execute_select_query(query, solution_id)
