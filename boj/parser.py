from typing import List

from bs4 import BeautifulSoup

from boj.problem import Problem
from boj.solution import Solution


def get_all_problems(response):
    """
    유저가 푼 모든 문제 번호 파싱

    :param response: http 요청 결과 받은 response 값
    :return:         문제 정보
                     [
                         Problem:
                             id: 문제 번호      : str,
                             title: 문제 제목   : str,
                     ]
    """

    html = BeautifulSoup(response, 'html.parser')
    html = html.find(attrs={'class': 'panel-body'})
    problem_ids = [num.text for num in html.find_all(attrs={'class': 'problem_number'})]
    titles = [title.text for title in html.find_all(attrs={'class': 'problem_title'})]

    problems = []
    for i in range(len(problem_ids)):
        problem = Problem(int(problem_ids[i]), titles[i])
        problems.append(problem)

    return problems


def get_problem_info(response, problem: Problem):
    """
    문제에 대한 정보 파싱

    :param response: http 요청 결과 받은 response 값
    :param problem: 문제 정보 { id, title }
    """

    html = BeautifulSoup(response, 'html.parser')
    tds = html.find('tbody').find('tr').find_all('td')
    problem.limit_time = tds[0].text
    problem.limit_memory = tds[1].text
    problem.description = html.find(attrs={'id': 'problem_description'}).text

    try:
        problem.input = html.find(attrs={'id': 'problem_input'}).text
    except AttributeError:
        pass
    try:
        problem.output = html.find(attrs={'id': 'problem_output'}).text
    except AttributeError:
        pass


def get_solution_info(response) -> List[Solution]:
    """
    유저가 푼 문제에 대한 정보를 파싱

    :param response: http 요청 결과 받은 response 값
    :return:         문제 풀이 정보
                     [
                         {
                             solution_id: 문제 번호        : str,
                             success: 문제 풀이 여부        : str,
                             memory: 풀이 메모리 사용량       : str,
                             time: 풀이 시간 (ms)          : str,
                             language: 풀이 프로그래밍 언어   : str,
                             length: 풀이 코드 길이         : str,
                         }
                     ]
    """

    html = BeautifulSoup(response, 'html.parser')
    html = html.find('tbody')

    solutions = html.find_all('tr')

    sols = []
    for solution in solutions:
        sol = solution.find_all('td')

        sols.append(Solution(
            id=int(sol[0].text),
            success=sol[3].text,
            time=sol[5].text,
            memory=sol[4].text,
            language=sol[6].text,
            length=sol[7].text
        ))

    return sols
