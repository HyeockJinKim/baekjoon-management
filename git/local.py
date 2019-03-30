from os.path import join

from boj.boj import BOJ_URL, BOJ_USER_URL, BOJ_PROBLEM_URL, language_map


def write_main_readme(home, username):
    content = '# My [Boj]({}) Algorithm Solution Code\n' \
              'This is my Boj [Submission]({})'.format(BOJ_URL, BOJ_USER_URL.format(username))
    with open(join(home, 'README.md'), 'w') as f:
        f.write(content)


def write_readme(saver, filepath, problem_id, solution_list):
    info = saver.check_problem(problem_id)[0]
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
                                     str(problem_id), BOJ_PROBLEM_URL.format(problem_id))
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

