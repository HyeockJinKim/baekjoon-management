from getpass import getpass

from boj.boj import Boj


class User:
    def __init__(self, username: str):
        self.boj = Boj(username)
        self.problems = set()
        self.password = None
        self.read_db()

    def login(self):
        """
        Login Boj
        :return:
        """
        if self.boj.is_login():
            return True
        if not self.password:
            self.password = getpass()
        self.boj.login(self.password)
        return True

    def update(self):
        """
        Update Problem and Solution
        :return:
        """
        if not self.login():
            return False

        problems = self.boj.load_user_problems()
        if not problems:
            return False

        self.problems = set(problems)
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
