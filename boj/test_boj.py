from boj.boj import get_problem_info, get_solutions_info, get_multiple_problems_info
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


def test_boj_get_multiple_problem():
    problems = [Problem(1001, 'a'), Problem(1002, 'ab'), Problem(1003, 'ac')]
    get_multiple_problems_info(problems)
    res = [
        Problem(
            id=1001,
            title='a',
            limit_time='2 초',
            limit_memory='128 MB',
            description='\n두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.\n',
            input='\n첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)\n', output='\n첫째 줄에 A-B를 출력한다.\n'
        ),
        Problem(
            id=1002,
            title='ab',
            limit_time='2 초',
            limit_memory='128 MB',
            description='\n조규현과 백승환은 터렛에 근무하는 직원이다. 하지만\xa0워낙 존재감이 없어서 인구수는 차지하지 않는다. 다음은 조규현과 백승환의 사진이다.\n\n이석원은 조규현과 백승환에게 상대편 마린(류재명)의 위치를 계산하라는 명령을 내렸다. 조규현과 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다.\n조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고, 조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때, 류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.\n',
            input='\n첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 이루어져 있다.\n한 줄에 x1, y1, r1, x2, y2, r2가 주어진다. x1, y1, x2, y2는 -10,000보다 크거나 같고, 10,000보다 작거나 같은 정수이고, r1, r2는 10,000보다 작거나 같은 자연수이다.\n',
            output='\n각 테스트 케이스마다 류재명이 있을 수 있는 위치의 수를 출력한다. 만약 류재명이 있을 수 있는 위치의 개수가 무한대일 경우에는 -1을 출력한다.\n'),
        Problem(
            id=1003,
            title='ac',
            limit_time='0.25 초 (추가 시간 없음)',
            limit_memory='128 MB',
            description='\n다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.\n\r\nint fibonacci(int n) {\r\n    if (n == 0) {\r\n        printf("0");\r\n        return 0;\r\n    } else if (n == 1) {\r\n        printf("1");\r\n        return 1;\r\n    } else {\r\n        return fibonacci(n‐1) + fibonacci(n‐2);\r\n    }\r\n}\r\n\nfibonacci(3)을 호출하면 다음과 같은 일이 일어난다.\n\nfibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.\nfibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.\n두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.\nfibonacci(0)은 0을 출력하고, 0을 리턴한다.\nfibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.\n첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.\nfibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.\n\n1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.\n',
            input='\n첫째 줄에 테스트 케이스의 개수 T가 주어진다.\n각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.\n',
            output='\n각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.\n'
        )
    ]

    for i in range(3):
        assert problems[i].id == res[i].id
        assert problems[i].title == res[i].title
        assert problems[i].limit_time == res[i].limit_time
        assert problems[i].limit_memory == res[i].limit_memory
        assert problems[i].description == res[i].description
        assert problems[i].input == res[i].input
        assert problems[i].output == res[i].output
