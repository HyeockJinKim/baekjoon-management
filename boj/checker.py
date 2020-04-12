from typing import List

from boj.solution import Solution

correct_list = ['맞았습니다!!', '맞았습니다!!\xa0(201/201)', '100점']


def check_solution(a: Solution, b: Solution) -> bool:
    """
    문제가 최근에 풀었던 문제보다 점수가 높은지 확인

    :param a: 최근 문제
    :param b: 점수가 높은지 비교하려는 문제
    :return:  dict에 들어있는 문제보다 최신이거나 점수가 높은지 여부
    """
    if a.success == b.success and b.id < a.id:
        return False

    return True


def filter_solution(sols: List[Solution]) -> Solution:
    """
    같은 문제에 대해서 가장 점수가 높은 풀이만을 남김
    풀이가 점수가 같을 경우 최근에 푼 문제를 선택

    :param sols: 유저의 모든 문제 풀이
    :return:     유저의 모든 문제 풀이 중 가장 점수가 높은 문제만 있는 풀이 리스트
    """
    sols = [sol for sol in sols if sol.success in correct_list]
    solution = None
    for sol in sols:
        if not solution:
            solution = sol

        elif check_solution(solution, sol):
            solution = sol
    return solution
