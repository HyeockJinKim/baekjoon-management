from os import mkdir
from os.path import join, isdir


def mk_src_dir(home):
    src_dir = join(home, 'src')
    if not isdir(src_dir):
        mkdir(src_dir)
    return src_dir


def mk_problem_dir(home: str, problem_id: int, title: str = None) -> str:
    src_dir = mk_src_dir(home)
    if title:
        sol_dir = join(src_dir, str(problem_id) + '_' + title)
    else:
        sol_dir = join(src_dir, str(problem_id))
    if not isdir(sol_dir):
        mkdir(sol_dir)
    return sol_dir
