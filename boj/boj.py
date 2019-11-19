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
    'Rust': '.rs',
    'Ruby 2.5': '.rb',
    'Kotlin (JVM)': '.kt',
    'Kotlin (Native)': '.kt'
}

# URL for parsing
BOJ_URL = 'https://www.acmicpc.net'
# URL for user cookie
BOJ_LOGIN_URL = BOJ_URL + '/signin'
# URL for solution
BOJ_USER_URL = BOJ_URL + '/user/{}'  # username
BOJ_PROBLEM_URL = BOJ_URL + '/problem/{}'  # problem id
BOJ_SUBMISSION_URL = BOJ_URL + '/status?from_mine=1&problem_id={}&user_id={}'  # problem id, username
BOJ_SOLUTION_URL = BOJ_URL + '/source/download/{}'  # solution id


class Boj:

    def __init__(self, username=None):
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
        url = BOJ_LOGIN_URL
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

        url = BOJ_USER_URL.format(self.username)
        response = get_url(url)

        if response.status_code == 200:
            problems = parser.get_all_problems(response.text)
            return problems

        return None

    @staticmethod
    def get_problem_info(number, title):
        """
        Get information of problem

        :param number: problem_id
        :param title:  problem's title
        :return:       problem's information {id, title, limit_time, limit_memory, description, input, output}
        """

        url = BOJ_PROBLEM_URL.format(number)
        response = get_url(url)

        if response.status_code == 200:
            data = parser.get_problem_info(response.text)
            data.update({
                'id': number,
                'title': title,
            })
            return data
        return None

    @staticmethod
    def get_multiple_problems_info(problems):
        """
        Get information of user's problems

        :param problems: problem solved by user {id, title}
        :return:         problem's info {id, title, limit_time, limit_memory, description, input, output}
        """

        problems_info = []
        for problem in problems:
            data = Boj.get_problem_info(problem['id'], problem['title'])
            if data:
                problems_info.append(data)
        return problems_info

    def get_solution_info(self, problem_id):
        """
        Get user solution's info

        :param problem_id: problem's id
        :return:           user solution's information {problem_id, sols[{id, success, memory, time, language, length}]}
        """

        url = BOJ_SUBMISSION_URL.format(problem_id, self.username)
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
        url = BOJ_SOLUTION_URL.format(solution_id)
        response = get_url(url, cookie=self.cookie)

        if response.status_code == 200:
            return response.text
        return None
