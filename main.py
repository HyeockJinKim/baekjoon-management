from boj import parser
from boj.boj import Boj


if __name__ == '__main__':
    username = input()
    password = input()
    boj = Boj(username)
    # problem = boj.load_user_problems()
    # info = boj.get_problems_info(problem)
    # for num in info['num']:
    #     boj.get_solution_info(num)

    boj.login(password)
    # sol = boj.get_solution_info(6996)
    boj.get_solution(6107160)

