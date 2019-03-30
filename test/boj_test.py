import unittest
from boj.boj import Boj


class MyBojTest(unittest.TestCase):
    username = 'gurwls9628'

    def test_load_user_problems_len(self):
        boj = Boj(self.username)
        problems = boj.load_user_problems()
        self.assertIsNotNone(problems)

    def test_get_problems_info(self):
        boj = Boj(self.username)
        info = {
            'problem_id': [1000, ],
            'title': ['A+B', ]
        }
        info = boj.get_multiple_problems_info(info)
        expected = [{
            'limit_time': '2 초',
            'limit_memory': '128 MB',
            'description': '\n두 정수 A와 B를 입력받은 다음,\xa0A+B를 출력하는 프로그램을 작성하시오.\n',
            'input': '\n첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)\n',
            'output': '\n첫째 줄에 A+B를 출력한다.\n',
            'problem_id': 1000,
            'title': 'A+B'
        }]

        self.assertEqual(info, expected)

    def test_get_solution_info(self):
        boj = Boj(self.username)
        info = boj.get_solution_info(1000)
        expected = {
            'problem_id': 1000,
            'solutions': [{
                'id': '6107157',
                'success': '맞았습니다!!',
                'memory': '1116',
                'time': '0',
                'language': 'C',
                'length': '93'
            }]}

        self.assertEqual(info, expected)


if __name__ == '__main__':
    unittest.main()
