from bs4 import BeautifulSoup


def get_all_problems(response):
    """
    Get all problem's num, title through parsing html

    :param response: http response of request
    :return:         problem info {num, title}
    """

    html = BeautifulSoup(response, 'html.parser')
    html = html.find(attrs={'class': 'panel-body'})

    problems = {
        'num': html.find_all(attrs={'class': 'problem_number'}),
        'title': html.find_all(attrs={'class': 'problem_title'})
    }

    return problems


def get_problem_info(response):
    """
    Get problem's information

    :param response: http response of request
    :return:         problem info {description, input, output}
    """

    html = BeautifulSoup(response, 'html.parser')
    data = {
        'description': html.find(attrs={'id': 'problem_description'}).text,
        'input': html.find(attrs={'id': 'problem_input'}).text,
        'output': html.find(attrs={'id': 'problem_output'}).text
    }
    return data


def get_solution_info(response):
    """
    Get problem's solution

    :param response: http response of request
    :return:         problem
    """

    html = BeautifulSoup(response, 'html.parser')
    html = html.find('tbody')

    solutions = html.find_all('tr')

    sols = []
    for solution in solutions:
        sol = solution.find_all('td')
        sols.append({
            "link": sol[0].text,
            "solve": sol[3].text == '맞았습니다!!',
            "language": sol[6].text
        })

    print(sols)
    return sols
