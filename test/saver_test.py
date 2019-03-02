import unittest
import os
from boj.saver import Saver


class MySaverTest(unittest.TestCase):
    home = '.test'

    def remove_db(self):
        os.remove(os.path.join(self.home, 'info.db'))
        os.removedirs(self.home)

    def test_saver(self):
        saver = Saver(self.home)
        self.remove_db()

    def test_check_empty_problem(self):
        saver = Saver(self.home)
        problem = saver.check_problem(1000)
        self.assertEqual(problem, None)
        self.remove_db()

    def test_insert_problem(self):
        saver = Saver(self.home)
        info = {
                'id': 1000,
                'confirm': False,
                'limit_time': 1,
                'limit_memory': 128,
                'title': 'A+B',
                'category': None,
                'description': 'A와 B를 더하라.',
                'input': '\nA와 B가 주어짐\n',
                'output': 'A+B의 결과'
        }
        result = saver.insert_problem_info(info)
        self.assertTrue(result)
        self.remove_db()

    def test_insert_value_problem(self):
        saver = Saver(self.home)
        info = {
                'id': 1000,
                'confirm': False,
                'limit_time': 1,
                'limit_memory': 128,
                'title': 'A+B',
                'category': None,
                'description': 'A와 B를 더하라.',
                'input': '\nA와 B가 주어짐\n',
                'output': 'A+B의 결과'
        }
        expected = [(
            1000,
            0,
            'A+B',
            '1',
            '128',
            None,
            'A와 B를 더하라.',
            '\nA와 B가 주어짐\n',
            'A+B의 결과'
        )]
        saver.insert_problem_info(info)
        problem = saver.check_problem(1000)
        self.assertEqual(problem, expected)
        self.remove_db()
