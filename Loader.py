import ssl
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

BOJ_URL = 'https://www.acmicpc.net'
BOJ_USER_URL = BOJ_URL + '/user/'


def load_user_solution(user):
    url = BOJ_USER_URL+user
    refer_head = 'http://www.google.com/'
    connection_head = 'keep-alive'
    user_head = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome'

    context = ssl._create_unverified_context()
    request = Request(url)
    request.add_header('User-Agent', user_head)
    request.add_header('referer', refer_head)
    request.add_header('Connection', connection_head)

    response = urlopen(request, context=context).read()
    html = BeautifulSoup(response, 'html.parser')
    html = html.find(attrs={'class': 'panel-body'})
    number = html.find_all(attrs={'class': 'problem_number'})
    title = html.find_all(attrs={'class': 'problem_title'})

    data = []
    print(len(number))
    for index in range(len(number)):
        urls = BOJ_URL+number[index].a['href']
        refer_head = 'http://www.google.com/'
        connection_head = 'keep-alive'
        user_head = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome'

        context = ssl._create_unverified_context()
        request = Request(urls)
        request.add_header('User-Agent', user_head)
        request.add_header('referer', refer_head)
        request.add_header('Connection', connection_head)

        response = urlopen(request, context=context).read()
        html = BeautifulSoup(response, 'html.parser')
        data.append({
            'num': number[index].text,
            'title': title[index].text,
            'link': urls,
            'description': html.find(attrs={'id': 'problem_description'}).text,
            'input': html.find(attrs={'id': 'problem_input'}).text,
            'output': html.find(attrs={'id': 'problem_output'}).text
        })

    return data


print(load_user_solution('gurwls9628'))

