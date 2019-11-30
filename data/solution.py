from os.path import join

from boj.boj import language_map


class Solution:
    """
    # user's solution
            id        Integer, Primary key              : solution id
            problem   Integer, Foreign key(problem(id)) : foreign key for problem id
            success   boolean                           : whether problem is solved or not
            memory    Integer                           : used memory for solving problem
            language  VARCHAR(50)                       : language for solving problem
            time      Integer                           : used time for solving problem
            length    Integer                           : submitted code's byte
    """
    correct_list = ['맞았습니다!!', '맞았습니다!!\xa0(201/201)', '100점']

    def __init__(self, solution_id: int, problem_id: int, code: str, success: bool,
                 memory: int, language: str, time: int, length: int):
        self.id = solution_id
        self.problem_id = problem_id
        self.code = code
        self.success = success
        self.memory = memory
        self.language = language
        self.time = time
        self.length = length

    def __eq__(self, other):
        return self.problem_id == other.problem_id and self.language == other.language

    def __lt__(self, other):
        if self.time < other.time:
            return True
        elif self.time > other.time:
            return False

        if self.memory < other.memory:
            return True
        elif self.memory > other.memory:
            return False

        if self.code < other.code:
            return True

        return False

    def __hash__(self):
        return self.id

    def __repr__(self):
        return '{:5d}_{:8d}'.format(self.problem_id, self.id)

    def __str__(self):
        return '{:5d}_{:8d}'.format(self.problem_id, self.id)

    @classmethod
    def create(cls, problem_id: int=None, solution_id: int=None, code: str=None, success: bool=None,
               memory: int=None, language: str=None, time: int=None, length: int=None):
        solution = Solution(
            solution_id=solution_id,
            problem_id=problem_id,
            code=code,
            success=cls.is_success(success),
            memory=memory,
            language=language,
            time=time,
            length=length
        )
        return solution

    @classmethod
    def is_success(cls, success: bool or str) -> bool:
        if type(success) is bool:
            return success

        return success in cls.correct_list

    def crawl_source(self, boj):
        """
        Crawl problem information from boj
        :param boj:
        :return:
        """
        source = boj.get_source(self.id)
        if not source:
            return False

        self.code = source
        return True

    def lower_time(self, other):
        if self.time < other.time:
            return True

        if self.time == other.time:
            return self.id > other.id

        return False

    def lower_memory(self, other):
        if self.memory < other.memory:
            return True

        if self.memory == other.memory:
            return self.id > other.id

        return False

    def lower_code_byte(self, other):
        if self.code < other.code:
            return True

        if self.code == other.code:
            return self.id > other.id

        return False

    def src_file(self) -> str:
        return '{}.{}'.format(self.problem_id, self.language)

    def update(self, directory: str) -> bool:
        with open(join(directory, self.src_file())) as f:
            f.write(self.code)

        return True

    def write_code(self, directory: str) -> bool:
        with open(join(directory, self.src_file())) as f:
            f.write(self.code)

        return True
