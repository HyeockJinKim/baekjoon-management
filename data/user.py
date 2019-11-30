from getpass import getpass

from boj.boj import Boj
from data.problem import Problem


class User:
    def __init__(self, username: str):
        self.boj = Boj(username)
        self.problems = set()
        self.password = None
        self.read_db()

    def login(self) -> bool:
        """
        Login Boj
        :return:
        """
        if self.boj.is_login():

            return True
        if not self.password:
            self.password = getpass()

        if not self.boj.login(self.password):
            print('Login Failed..')
            return False
        return True

    def update(self) -> bool:
        """
        Update Problem and Solution
        :return:
        """
        if not self._update_problem():
            return False

        if not self._update_solution():
            return False

        return True

    def _update_problem(self) -> bool:
        if not self.login():
            return False

        print('Update user\'s Problem Information')
        problems = self.boj.load_user_problems()
        if not problems:
            return False

        problems = [Problem.create(**problem) for problem in problems]
        self.problems.update(problems)

        length = len(self.problems)
        index = 0
        for problem in self.problems:
            if not problem.crawl_problem_info(self.boj):
                return False
            index += 1
            print('진행: {:5.2f} % current/total {:5d} / {:5d}'.format(100*index//length, index, length))
        print('문제 업데이트 완료!!')
        return True

    def _update_solution(self) -> bool:
        if not self.login():
            return False

        print('Update user\'s Problem Solution')

        length = len(self.problems)
        index = 0
        for problem in self.problems:
            if not problem.crawl_solution(self.boj):
                return False
            index += 1
            print('진행: ', 100*index//length, '%  current/total', index, '/', length)
        print('Solution 리스트 업데이트 완료!!')
        return True

    def read_db(self):
        pass

    def store(self) -> bool:
        if not self.write_info():
            return False

        if not self.write_db():
            return False

        return True

    def write_db(self) -> bool:
        pass

    def write_info(self) -> bool:
        pass
