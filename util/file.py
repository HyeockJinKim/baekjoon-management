from os import mkdir
from os.path import join, isdir


def mkdir_src_dir(home):
    src_dir = join(home, 'src')
    if not isdir(src_dir):
        mkdir(src_dir)
    return src_dir


def mkdir_sol_dir(home, problem_id):
    src_dir = mkdir_src_dir(home)
    sol_dir = join(src_dir, str(problem_id))
    if not isdir(sol_dir):
        mkdir(sol_dir)
    return sol_dir
