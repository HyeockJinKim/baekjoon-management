from os.path import join
from decocli.cli import CLI
from boj.boj import Boj, language_map
from boj.saver import Saver
from boj.checker import filter_solution
from git_tool.local import write_main_readme, write_readme
from util.file import mk_problem_dir


class Api:
    def __init__(self, username=None, home='.'):
        self.home = home
        self.username = username
        self.src_dir = ''
        self.boj = Boj(self.username)
        self.saver = Saver(self.home)
    
    def update_my_problem_info(self):
        """
        Update information on problem I've solved
        """
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
        """
        Update information on my solution
        """
        print('Update Solution')

        problems = self.saver.load_all_problem_info()
        print(problems)
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

    def update_source(self, password):
        """
        Update source code
        :param password:  password for login in boj
        """
        print('Update Solution')

        sols = self.saver.load_solution()
        sols = filter_solution(sols)

        self.boj.login(password)
        length = len(sols.keys())
        index = 0
        write_main_readme(self.home, self.username)
        for problem_id in sols.keys():
            sol_dir = mk_problem_dir(self.home, problem_id)
            write_readme(self.saver, sol_dir, problem_id, sols[problem_id])
            for sol in sols[problem_id]:
                filename = 'main'+language_map[sol[4]]
                source = self.boj.get_source(sol[0])
                if source:
                    with open(join(sol_dir, filename), 'w') as f:
                        f.write(source)
            index += 1
            print('진행: ', 100 * index // length, '%  current/total', index, '/', length)
        print('Source 업데이트 완료!!')
