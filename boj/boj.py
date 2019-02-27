from boj.loader import request_url
from boj import parser


class Boj:

    def __init__(self, username):
        self.BOJ_URL = 'https://www.acmicpc.net'
        self.BOJ_LOGIN_URL = self.BOJ_URL + '/signin'
        self.BOJ_USER_URL = self.BOJ_URL + '/user/{}'
        self.BOJ_PROBLEM_URL = self.BOJ_URL+'/status?from_mine=1&problem_id={}&user_id={}'
        self.BOJ_SOLUTION_URL = self.BOJ_URL+'/source/{}'
        self.username = username
        self.cookie = None

    def login(self, password):
        """
        Login Boj

        :param password: password for login
        :return:
        """
        url = self.BOJ_LOGIN_URL
        login_info = {
            'login_user_id': self.username,
            'login_password': password
        }

        res = request_url(url, data=login_info)
        self.cookie = res.info()['Set-Cookie']

    def load_user_problems(self):
        """
        Load problems solved by user

        """

        url = self.BOJ_USER_URL.format(self.username)
        response = request_url(url).read()

        problems = parser.get_all_problems(response)
        print(problems)

        return problems

    def get_problems_info(self, problems):
        """
        Get information of user's problems

        :param problems: problem solved by user
        :return:         problem's info
        """

        number = problems['num']
        title = problems['title']

        problems_info = []
        for index in range(len(number)):
            url = self.BOJ_URL + number[index].a['href']
            response = request_url(url)

            data = parser.get_problem_info(response)
            data.update({
                'num': number[index].text,
                'title': title[index].text,
                'link': url,
            })
            problems_info.append(data)

        return problems_info

    def get_solution_info(self, num):
        """

        :param num:
        :return:
        """

        url = self.BOJ_PROBLEM_URL.format(num, self.username)
        response = request_url(url).read()

        problems = parser.get_solution_info(response)
        return problems

    def get_solution(self, index):
        url = self.BOJ_SOLUTION_URL.format(index)
        response = request_url(url, cookie=self.cookie).read()

        source = parser.get_source(response)

        return source








