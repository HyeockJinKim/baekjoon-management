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
                 limit_time: int, limit_memory: int, category: str, description: str, inputs: str, outputs: str):
        self.id: int = problem_id
        self.title = title
        self.limit_time = limit_time
        self.limit_memory = limit_memory
        self.category = category
        self.description = description
        self.inputs = inputs
        self.outputs = outputs
        self.solutions = set()

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return self.id

    @classmethod
    def create(cls, *, problem_id: int, title: str,
               limit_time: int, limit_memory: int, description: str,
               category: str = None, inputs: str = None, outputs: str = None):
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
