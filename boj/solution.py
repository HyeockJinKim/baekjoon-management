

correct_list = ['맞았습니다!!', '맞았습니다!!\xa0(201/201)', '100점']


def check_solution(sol_list, solution):
    for sol in sol_list:
        if sol[4] == solution[4] and solution[0] < sol[0]:
            return False

    return True


def filter_solution(sols):
    sols = [sol for sol in sols if sol[2] in correct_list]
    solutions = {}
    for sol in sols:
        if not solutions.get(sol[1]):
            solutions[sol[1]] = [sol]

        elif check_solution(solutions[sol[1]], sol):
            solutions[sol[1]].append(sol)
    return solutions

