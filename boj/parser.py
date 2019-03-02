from bs4 import BeautifulSoup


def get_all_problems(response):
    """
    Get all problem's num, title through parsing html

    :param response: http response of request
    :return:         problem info [{problem_id, title}]
    """

    html = BeautifulSoup(response, 'html.parser')
    html = html.find(attrs={'class': 'panel-body'})
    problem_ids = [num.text for num in html.find_all(attrs={'class': 'problem_number'})]
    titles = [title.text for title in html.find_all(attrs={'class': 'problem_title'})]

    problems = []
    for i in range(len(problem_ids)):
        problems.append({
            'problem_id': problem_ids[i],
            'title': titles[i]
        })

    return problems


def get_problem_info(response):
    """
    Get problem's information

    :param response: http response of request
    :return:         problem info {limit_time, limit_memory, description, input, output}
    """

    html = BeautifulSoup(response, 'html.parser')
    tds = html.find('tbody').find('tr').find_all('td')
    data = {
        'limit_time': tds[0].text,                                           # time limit
        'limit_memory': tds[1].text,                                         # memory limit
        'description': html.find(attrs={'id': 'problem_description'}).text,  # html
    }
    try:
        data['input'] = html.find(attrs={'id': 'problem_input'}).text        # input description (string)
    except:
        data['input'] = None
    try:
        data['output'] = html.find(attrs={'id': 'problem_output'}).text      # output description (string)
    except:
        data['output'] = None

    return data


def get_solution_info(response):
    """
    Get problem's solution

    :param response: http response of request
    :return:         solutions' info {id, success, memory, time, language, length}
    """

    html = BeautifulSoup(response, 'html.parser')
    html = html.find('tbody')

    solutions = html.find_all('tr')

    sols = []
    for solution in solutions:
        sol = solution.find_all('td')
        sols.append({
            "id":       sol[0].text,  # solution id
            "success":  sol[3].text,  # whether success or not
            "memory":   sol[4].text,  # used memory
            "time":     sol[5].text,  # used time
            "language": sol[6].text,  # language for solving problem
            "length":   sol[7].text,  # length of solution code
        })

    return sols
