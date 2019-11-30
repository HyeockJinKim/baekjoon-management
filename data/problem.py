from os.path import join

from boj.boj import BOJ_PROBLEM_URL, language_map
from util.file import mk_problem_dir


class Problem:
    """
    # Algorithm problem in boj
            id           Integer, Primary key           : problem id
            confirm      Integer, Default 0             : whether this problem is already checked or not
            title        VARCHAR(50)                    : problem's title
            limit_time   VARCHAR(20)                    : problem's limited time
            limit_memory VARCHAR(20)                    : problem's limited memory
            category     VARCHAR(50)                    : problem's category
            description  text                           : problem's description
            input        text                           : problem's input description
            output       text                           : problem's output description

            solutions    dict{ key=lang: val=Solution } : problem's solutions
    """
    def __init__(self, problem_id: int, title: str,
                 limit_time: int=None, limit_memory: int=None, category: str=None,
                 description: str=None, inputs: str=None, outputs: str=None):
        self.id: int = problem_id
        self.title = title
        self.limit_time = limit_time
        self.limit_memory = limit_memory
        self.category = category
        self.description = description
        self.inputs = inputs
        self.outputs = outputs
        self.solutions = {}

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return self.id

    def __repr__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)

    @classmethod
    def create(cls, *, problem_id: int, title: str,
               limit_time: int, limit_memory: int, description: str,
               category: str, inputs: str, outputs: str):
        """
        Create Problem Object
        :param problem_id:
        :param title:
        :param limit_time:
        :param limit_memory:
        :param description:
        :param category:
        :param inputs:
        :param outputs:
        :return:
        """
        category = category if category else '미분류'

        problem = Problem(
            problem_id=problem_id,
            title=title,
            limit_time=limit_time,
            limit_memory=limit_memory,
            category=category,
            description=description,
            inputs=inputs,
            outputs=outputs
        )
        return problem

    def crawl_problem_info(self, boj):
        """
        Crawl problem information from boj
        :param boj:
        :return:
        """
        if not self.is_checked():
            info = boj.get_problem_info(self.id, self.title)
            if not info:
                return False

            self.update(
                limit_time=info['limit_time'],
                limit_memory=info['limit_memory'],
                description=info['description'],
                inputs=info['input'],
                outputs=info['output']
            )
        return True

    def crawl_solution(self, boj):
        """
        Crawl problem information from boj
        :param boj:
        :return:
        """
        solutions = boj.get_solution_info(self.id)
        if not solutions:
            return False

        for solution in solutions:
            if self.solutions[solution.length]:
                self.solutions[solution.length] = solution
            elif solution < self.solutions[solution.length]:
                self.solutions[solution.length] = solution

        return True

    def is_checked(self):
        """
        Whether problem information is checked or not
        :return:
        """
        return self.limit_time is not None

    def readme(self) -> str:
        """
        Get README.md contents

        :return: README.md contents string
        """
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
                  '## Solution\n'.format(self.title, self.limit_time, self.limit_memory, self.description,
                                         self.inputs, self.outputs, self.category,
                                         self.id, BOJ_PROBLEM_URL.format(self.id))
        for sol in self.solutions:
            content += '### [{}-language Solution]({})\n' \
                       '#### 걸린 시간\n' \
                       '> {}\n' \
                       '#### 사용한 메모리\n' \
                       '> {}\n' \
                       '#### 코드 Byte\n' \
                       '> {}\n'.format(sol[4], './main' + language_map[sol[4]], str(sol[5]) + ' ms',
                                       str(sol[3]) + ' KB', str(sol[6]) + ' B')

        return content

    def update(self, problem_id: int=None, title: str=None,
               limit_time: int=None, limit_memory: int=None, description: str=None,
               category: str=None, inputs: str=None, outputs: str=None):
        """
        Update info
        :param problem_id:
        :param title:
        :param limit_time:
        :param limit_memory:
        :param description:
        :param category:
        :param inputs:
        :param outputs:
        :return:
        """
        if problem_id:
            self.id = problem_id
        if title:
            self.title = title
        if limit_time:
            self.limit_time = limit_time
        if limit_memory:
            self.limit_memory = limit_memory
        if description:
            self.description = description
        if category:
            self.category = category
        if inputs:
            self.inputs = inputs
        if outputs:
            self.outputs = outputs

    def write_problem(self, home: str) -> bool:
        directory = mk_problem_dir(home, self.id, self.title)
        if not self.write_readme(directory):
            return False

        for lang, solution in self.solutions:
            if not solution.write_code(directory):
                return False

        return True

    def write_readme(self, directory: str) -> bool:
        readme = self.readme()
        with open(join(directory, "README.md")) as f:
            f.write(readme)
        return True
