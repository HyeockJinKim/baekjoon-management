from boj.boj import get_problem_info, get_solutions_info
from boj.problem import Problem
from boj.solution import Solution


def test_boj_get_problem_info():
    problem = Problem(1000, 'abc')
    get_problem_info(problem)
    res = Problem(
        id=1000,
        title='abc',
        limit_time='2 초',
        limit_memory='128 MB',
        description='\n두 정수 A와 B를 입력받은 다음,\xa0A+B를 출력하는 프로그램을 작성하시오.\n',
        input='\n첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)\n',
        output='\n첫째 줄에 A+B를 출력한다.\n'
    )
    assert problem.id == res.id
    assert problem.title == res.title
    assert problem.limit_time == res.limit_time
    assert problem.limit_memory == res.limit_memory
    assert problem.description == res.description
    assert problem.input == res.input
    assert problem.output == res.output


def test_boj_get_solution_info():
    problem_id = 1000
    username = 'gurwls9628'
    solutions = get_solutions_info(problem_id, username)
    res = Solution(
        id=6107157,
        success='맞았습니다!!',
        time='0',
        memory='1116',
        language='C',
        length='88'
    )
    assert solutions[0].id == res.id
    assert solutions[0].success == res.success
    assert solutions[0].time == res.time
    assert solutions[0].memory == res.memory
    assert solutions[0].language == res.language
    assert solutions[0].length == res.length
