from os.path import join


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
        return self.id == other.id

    def __hash__(self):
        return self.id

    @classmethod
    def create(cls, solution_id: int, problem_id: int, code: str, success: bool,
               memory: int, language: str, time: int, length: int):
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

    def src_file(self) -> str:
        return '{}.{}'.format(self.problem_id, self.language)

    def write_code(self, directory: str) -> bool:
        with open(join(directory, self.src_file())) as f:
            f.write(self.code)

        return True
