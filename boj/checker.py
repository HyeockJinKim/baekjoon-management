

correct_list = ['맞았습니다!!', '맞았습니다!!\xa0(201/201)', '100점']


def check_solution(a, b) -> bool:
    """
    문제가 최근에 풀었던 문제보다 점수가 높은지 확인

    :param a: dict에 들어있는 문제
    :param b: 비교하려는 문제
    :return:  dict에 들어있는 문제보다 최신이거나 점수가 높은지 여부
    """
    if a[4] == b[4] and b[0] < a[0]:
        return False

    return True


def filter_solution(sols):
    """
    같은 문제에 대해서 가장 점수가 높은 풀이만을 남김
    풀이가 점수가 같을 경우 최근에 푼 문제를 선택

    :param sols: 유저의 모든 문제 풀이
    :return:     유저의 모든 문제 풀이 중 가장 점수가 높은 문제만 있는 풀이 리스트
    """
    sols = [sol for sol in sols if sol[2] in correct_list]
    solutions = {}
    for sol in sols:
        if not solutions.get(sol[1]):
            solutions[sol[1]] = sol

        elif check_solution(solutions[sol[1]], sol):
            solutions[sol[1]] = sol
    return solutions
