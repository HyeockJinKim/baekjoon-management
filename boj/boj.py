import json
from os.path import join
from typing import List

from boj import parser
from boj.boj_url import BOJUrl
from boj.checker import filter_solution
from boj.net import post_url, process_cookie, get_url, fast_get_multiple_url
from boj.problem import Problem
from boj.solution import Solution


def read_user_info(path: str) -> (str, str):
    """
    유저의 로그인을 위한 정보를 json에서 읽음
    :param path: .userinfo.json 파일이 있는 경로
    :return: .userinfo.json 에 적혀있는 유저 로그인 정보 (아이디, 비밀번호)
    """
    if not path.endswith('.userinfo.json'):
        path = join(path, '.userinfo.json')
    with open(path, 'r') as f:
        data = json.load(f)
        return data['boj']['id'], data['boj']['password']


def login(username: str = None, password: str = None) -> str:
    """
    BOJ 로그인 후 로그인 세션을 저장

    :param username: 로그인을 위한 ID
    :param password: 로그인을 위한 비밀번호
    :return: 로그인 세션 쿠키
    """

    url = BOJUrl.LOGIN_URL
    login_info = {
        'login_user_id': username,
        'login_password': password
    }

    res = post_url(url, data=login_info)
    return process_cookie(res.headers['Set-Cookie'])


def load_user_problems(username: str) -> List[Problem]:
    """
    유저가 푼 문제 리스트를 전부 읽어옴

    :param username: BOJ 아이디
    :return: 유저가 푼 문제 전체 {num, title}
    """

    url = BOJUrl.USER_URL.format(username)
    response = get_url(url)

    if response.status_code == 200:
        problems = parser.get_all_problems(response.text)
        return problems
    return []


def get_problem_info(problem: Problem):
    """
    문제 번호를 통해 문제 전체 정보를 읽어옴

    :param problem: id 값과 title 값만 저장된 문제 정보
    """

    url = BOJUrl.PROBLEM_URL.format(str(problem.id))
    response = get_url(url)

    if response.status_code == 200:
        parser.get_problem_info(response.text, problem)


def get_multiple_problems_info(problems: List[Problem]):
    """
    여러 개의 문제 정보를 읽어옴
    call by reference 이므로 수정된 값 parameter를 통해 전달

    :param problems: id 값과 title 값만 저장된 문제 정보
    """

    url_list = [BOJUrl.PROBLEM_URL.format(str(problem.id)) for problem in problems]
    response_list = fast_get_multiple_url(url_list)

    for i, response in enumerate(response_list):
        parser.get_problem_info(response, problems[i])


def get_solutions_info(problem_id: str or int, username: str) -> List[Solution]:
    """
    유저의 문제 풀이에 대한 정보를 가져옴

    :param problem_id: 문제 번호
    :param username: Boj 아이디
    :return: 유저가 푼 문제 Solution
    """

    url = BOJUrl.SUBMISSION_URL.format(problem_id, username)
    response = get_url(url)
    if response.status_code == 200:
        solutions = parser.get_solution_info(response.text)
        return solutions
    return []


def get_multiple_solutions(problems: List[Problem], username: str) -> List[Solution]:
    """
    여러 개의 문제에 대한 Solution 정보를 가져옴

    :param problems: 풀었던 문제 리스트
    :param username: Boj 아이디
    :return: 풀었던 Solution 리스트
    """
    url_list = [BOJUrl.SUBMISSION_URL.format(problem.id, username) for problem in problems]
    response_list = fast_get_multiple_url(url_list)

    solutions = []
    for i, response in enumerate(response_list):
        sols = parser.get_solution_info(response)
        solution = filter_solution(sols)
        solutions.append(solution)
    return solutions


def get_source(solution_id, cookie) -> str:
    """
    문제 풀이 소스코드

    :param solution_id:  문제 번호
    :param cookie: 로그인 세션이 저장된 쿠키
    :return:             solution source
    """
    url = BOJUrl.SOLUTION_URL.format(solution_id)
    response = get_url(url, cookie=cookie)

    if response.status_code == 200:
        return response.text


def get_multiple_source(solutions: List[Solution], cookie: str) -> List[str]:
    """
    여러 개의 문제 풀이 소스 코드를 가져옴

    :param solutions: 풀었던 solution에 대한 정보
    :param cookie: 로그인 정보
    :return: 소스코드 리스트
    """
    url_list = [BOJUrl.SOLUTION_URL.format(str(solution.id)) for solution in solutions]
    response_list = fast_get_multiple_url(url_list, cookie)
    return response_list
