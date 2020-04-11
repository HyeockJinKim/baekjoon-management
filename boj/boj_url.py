import enum


class BOJUrl(enum.Enum):
    # URL for parsing
    BASE_URL = 'https://www.acmicpc.net'
    # URL for user cookie
    LOGIN_URL = BASE_URL + '/signin'
    # URL for solution
    USER_URL = BASE_URL + '/user/{}'  # username
    PROBLEM_URL = BASE_URL + '/problem/{}'  # problem id
    SUBMISSION_URL = BASE_URL + '/status?from_mine=1&problem_id={}&user_id={}'  # problem id, username
    SOLUTION_URL = BASE_URL + '/source/download/{}'  # solution id
