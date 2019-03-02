from boj.net import get_url, process_cookie, post_url
from boj import parser


language_map = {
    'C': '.c',
    'C11': '.c',
    'C++': '.cpp',
    'C++11': '.cpp',
    'C++14': '.cpp',
    'C++17': '.cpp',
    'C (Clang)': '.c',
    'C11 (Clang)': '.c',
    'C++ (Clang)': '.cpp',
    'C++11 (Clang)': '.cpp',
    'C++14 (Clang)': '.cpp',
    'C++17 (Clang)': '.cpp',
    'Java': '.java',
    'Java (OpenJDK)': '.java',
    'Java 11': '.java',
    'Python 2': '.py',
    'Python 3': '.py',
    'PyPy2': '.py',
    'PyPy3': '.py',
    'Go': '.go',
    'Ruby 2.5': '.rb',
    'Kotlin (JVM)': '.kt',
    'Kotlin (Native)': '.kt'
}


class Boj:

    def __init__(self, username=None):
        # URL for parsing
        self.BOJ_URL = 'https://www.acmicpc.net'
        # URL for user cookie
        self.BOJ_LOGIN_URL = self.BOJ_URL + '/signin'
        # URL for solution
        self.BOJ_USER_URL = self.BOJ_URL + '/user/{}'  # username
        self.BOJ_PROBLEM_URL = self.BOJ_URL + '/problem/{}'  # problem id
        self.BOJ_SUBMISSION_URL = self.BOJ_URL + '/status?from_mine=1&problem_id={}&user_id={}'  # problem id, username
        self.BOJ_SOLUTION_URL = self.BOJ_URL+'/source/download/{}'  # solution id

        # user info of boj
        self.username = username
        self.cookie = None

    """
    Functions for boj Auto commit
        login
        load_user_problems
        get_problems_info
        get_solution_info
        get_source
    
    """
    def login(self, password):
        """
        Login Boj and save cookie

        :param password: password for login
        """
        url = self.BOJ_LOGIN_URL
        login_info = {
            'login_user_id': self.username,
            'login_password': password
        }

        res = post_url(url, data=login_info)
        self.cookie = process_cookie(res.headers['Set-Cookie'])

    def load_user_problems(self):
        """
        Load problems solved by user

        :return: all problems solved by user {num, title}
        """

        url = self.BOJ_USER_URL.format(self.username)
        response = get_url(url)

        if response.status_code == 200:
            problems = parser.get_all_problems(response.text)
            return problems

        return None

    def get_problem_info(self, number, title):
        """
        Get information of problem

        :param number: problem_id
        :param title:  problem's title
        :return:       problem's information {problem_id, title, limit_time, limit_memory, description, input, output}
        """

        url = self.BOJ_PROBLEM_URL.format(number)
        response = get_url(url)

        if response.status_code == 200:
            data = parser.get_problem_info(response.text)
            data.update({
                'id': number,
                'title': title,
            })
            return data
        return None

    def get_multiple_problems_info(self, problems):
        """
        Get information of user's problems

        :param problems: problem solved by user {problem_id, title}
        :return:         problem's info {problem_id, title, limit_time, limit_memory, description, input, output}
        """

        problems_info = []
        for problem in range(problems):
            data = self.get_problem_info(problem['id'], problem['title'])
            if data:
                problems_info.append(data)
        return problems_info

    def get_solution_info(self, problem_id):
        """
        Get user solution's info

        :param problem_id: problem's id
        :return:           user solution's information {problem_id, sols[{id, success, memory, time, language, length}]}
        """

        url = self.BOJ_SUBMISSION_URL.format(problem_id, self.username)
        response = get_url(url)
        if response.status_code == 200:
            problems = parser.get_solution_info(response.text)
            info = {
                'problem_id': problem_id,
                'solutions':  problems
            }
            return info
        return None

    def get_source(self, solution_id):
        """
        Get solution source

        :param solution_id:  solution id
        :return:             solution source
        """
        url = self.BOJ_SOLUTION_URL.format(solution_id)
        response = get_url(url, cookie=self.cookie)

        if response.status_code == 200:
            return response.text
        return None
