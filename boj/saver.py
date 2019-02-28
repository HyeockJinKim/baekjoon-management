from os.path import join
import sqlite3


class Saver:

    def __init__(self, home=None):
        if home is None:
            self.home = join('.')
        else:
            self.home = home

        self.db = join(self.home, 'info.db')

    def create(self):
        """
        Create Database Table

        ::Table::
        problem:
            # Algorithm problem in boj
            id           Integer, Primary key           : problem id
            title        VARCHAR(50)                    : problem's title
            category     VARCHAR(50)                    : problem's category
            description  text                           : problem's description

        marking:
            # unknown user's solution
            id        Integer, Primary key              : solution id
            problem   Integer, Foreign key(problem(id)) : foreign key for problem id
            success   Boolean                           : whether problem is solved or not
            memory    Integer                           : used memory for solving problem
            language  VARCHAR(50)                       : language for solving problem
            time      Integer                           : used time for solving problem
            length    Integer                           : submitted code's byte

        solution:
            # user's solution
            id        Integer, Primary key              : solution id
            problem   Integer, Foreign key(problem(id)) : foreign key for problem id
            success   Boolean                           : whether problem is solved or not
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
                'title VARCHAR (50),' \
                'category VARCHAR (50),' \
                'description VARCHAR (50)' \
                ')',
                'CREATE TABLE IF NOT EXISTS marking (' \
                'id INTEGER PRIMARY KEY NOT NULL,' \
                'problem INTEGER NOT NULL,' \
                'success INTEGER,' \
                'memory INTEGER,' \
                'language VARCHAR (50),' \
                'time INTEGER,' \
                'length INTEGER,' \
                'foreign key(problem) references problem(id)' \
                ')',
                'CREATE TABLE IF NOT EXISTS solution (' \
                'id INTEGER PRIMARY KEY NOT NULL,' \
                'problem INTEGER NOT NULL,' \
                'success INTEGER,' \
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

    def execute_select_query(self, query):
        """
        Execute 'select' query

        :param query: 'select' query
        :return:       Query result
        """

        try:
            with sqlite3.connect(self.db) as conn:
                cur = conn.cursor()
                cur.execute(query)
                rows = cur.fetchall()
                conn.commit()
            return rows
        except:
            return []

    def execute_insert_query(self, query, data):
        """
        Execute 'insert' query

        :param query: 'insert' query
        :return:       whether query success or not
        """

        try:
            with sqlite3.connect(self.db) as conn:
                cur = conn.cursor()
                cur.execute(query, data)
                rows = cur.fetchall()
                print(rows)
                conn.commit()
            return True
        except:
            return False

    def insert_problem_info(self, info):
        """
        Insert problem table's information

        ::Table::
        problem:
            # Algorithm problem in boj
            id           Integer, Primary key           : problem id
            title        VARCHAR(50)                    : problem's title
            category     VARCHAR(50)                    : problem's category
            description  text                           : problem's description

        :param info: Problem's info to insert
        :return:     Whether query success or not
        """

        query = 'insert into problem (id, title, category, description) values (?, ?, ?, ?)'
        data = (info['id'], info['title'], info['category'], info['description'])
        return self.execute_insert_query(query, data=data)

    def load_problem(self):
        """
        Load problem table's information
        :return:
        """
        query = 'select * from problem'
        return self.execute_select_query(query)

    def insert_marking_info(self, info):
        """
        Save marking table's information

        ::Table::
        marking:
            # unknown user's solution
            id        Integer, Primary key              : solution id
            problem   Integer, Foreign key(problem(id)) : foreign key for problem id
            success   Boolean                           : whether problem is solved or not
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

    def insert_solution_info(self, info):
        """
        Save solution table's information

        ::Table::
        marking:
            # unknown user's solution
            id        Integer, Primary key              : solution id
            problem   Integer, Foreign key(problem(id)) : foreign key for problem id
            success   Boolean                           : whether problem is solved or not
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
