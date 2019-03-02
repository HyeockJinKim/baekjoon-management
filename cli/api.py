from os import mkdir
from os.path import isdir, join

from boj.boj import Boj, language_map
from boj.saver import Saver


def check_solution(sol_list, solution):
    for sol in sol_list:
        if sol[4] == solution[4] and solution[0] < sol[0]:
            return False

    return True


def filter_solution(sols):
    correct_list = ['맞았습니다!!', '맞았습니다!!\xa0(201/201)', '100점']
    sols = [sol for sol in sols if sol[2] in correct_list]
    solutions = {}
    for sol in sols:
        if not solutions.get(sol[1]):
            solutions[sol[1]] = [sol]

        elif check_solution(solutions[sol[1]], sol):
            solutions[sol[1]].append(sol)
    return solutions


class Api:
    def __init__(self, username=None, home='.'):
        self.home = home
        self.username = username

        self.src_dir = ''
        self.boj = Boj(self.username)
        self.saver = Saver(self.home)

    def update_my_problem_info(self):
        print('Update Problem')


        problems = self.boj.load_user_problems()
        length = len(problems)
        index = 0
        for problem in problems:
            if not self.saver.check_problem(problem['problem_id']):
                info = self.boj.get_problem_info(problem['problem_id'], problem['title'])
                info.update({
                    'confirm': False,
                    'category': None,
                })
                self.saver.insert_problem_info(info)
            index += 1
            print('진행: ', 100*index//length, '%  current/total', index, '/', length)
        print('문제 업데이트 완료!!')

    def update_my_solution_info(self):
        print('Update Solution')

        problems = self.saver.load_all_problem_info()
        length = len(problems)
        index = 0
        for problem in problems:
            sol = self.boj.get_solution_info(problem[0])
            for solution in sol['solutions']:
                if not self.saver.check_solution(solution['id']):
                    info = solution
                    info.update({
                        'problem': problem[0]
                    })
                    self.saver.insert_solution_info(info)
            index += 1
            print('진행: ', 100*index//length, '%  current/total', index, '/', length)
        print('Solution 리스트 업데이트 완료!!')

    def mkdir_src_dir(self):
        self.src_dir = join(self.home, 'src')
        if not isdir(self.src_dir):
            mkdir(self.src_dir)

    def mkdir_sol_dir(self, problem_id):
        self.mkdir_src_dir()
        sol_dir = join(self.src_dir, str(problem_id))
        if not isdir(sol_dir):
            mkdir(sol_dir)
        return sol_dir
    
    def write_readme(self, filepath, problem_id, solution_list):
        info = self.saver.check_problem(problem_id)[0]
        category = info[5]
        if not info[5]:
            category = '미분류'
        content = '# {}\n' \
                  '#### 시간 제한\n' \
                  '> {}\n' \
                  '#### 메모리 제한\n' \
                  '> {}\n' \
                  '### 문제 내용\n' \
                  '{}\n' \
                  '### 입력\n' \
                  '{}\n' \
                  '### 출력\n' \
                  '{}\n' \
                  '### 분류\n' \
                  '{}\n' \
                  '> This problem is in [Boj {} problem]({})\n\n' \
                  '## Solution\n'.format(info[2], info[3], info[4], info[6], info[7], info[8], category,
                                         str(problem_id), self.boj.BOJ_PROBLEM_URL.format(problem_id))
        for sol in solution_list:
            content += '### [{}-language Solution]({})\n' \
                       '#### 걸린 시간\n' \
                       '> {}\n' \
                       '#### 사용한 메모리\n' \
                       '> {}\n' \
                       '#### 코드 Byte\n' \
                       '> {}\n'.format(sol[4], './main'+language_map[sol[4]], str(sol[5])+' ms',
                                       str(sol[3])+' KB', str(sol[6])+' B')
        with open(join(filepath, 'README.md'), 'w') as f:
            f.write(content)

    def write_main_readme(self):
        content = '# My [Boj]({}) Algorithm Solution Code\n' \
                  'This is my Boj [Submission]({})'.format(self.boj.BOJ_URL, self.boj.BOJ_USER_URL.format(self.username))
        with open(join(self.home, 'README.md'), 'w') as f:
            f.write(content)

    def update_source(self, password):
        print('Update Solution')

        sols = self.saver.load_solution()
        sols = filter_solution(sols)

        self.boj.login(password)
        length = len(sols.keys())
        index = 0
        self.write_main_readme()
        for problem_id in sols.keys():
            sol_dir = self.mkdir_sol_dir(problem_id)
            self.write_readme(sol_dir, problem_id, sols[problem_id])
            for sol in sols[problem_id]:
                filename = 'main'+language_map[sol[4]]
                source = self.boj.get_source(sol[0])
                if source:
                    with open(join(sol_dir, filename), 'w') as f:
                        f.write(source)
            index += 1
            print('진행: ', 100 * index // length, '%  current/total', index, '/', length)
        print('Source 업데이트 완료!!')
