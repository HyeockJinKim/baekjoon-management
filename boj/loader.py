import ssl
from urllib.parse import urlencode
from urllib.request import urlopen, Request


def add_header(request, cookie=None):
    """
    Add Header to request
    :param request: http request
    :param cookie:  cookie for http
    """

    refer_head = 'http://www.google.com/'
    connection_head = 'keep-alive'
    user_head = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome'

    request.add_header('User-Agent', user_head)
    request.add_header('referer', refer_head)
    request.add_header('Connection', connection_head)
    if cookie is not None:
        request.add_header('Cookie', cookie)


def request_url(url, data=None, cookie=None):
    """
    Request to url for parsing page

    :param url:    url for parsing page
    :param data:   post data
    :param cookie: cookie for http
    :return:       html
    """

    context = ssl._create_unverified_context()

    request = Request(url)
    add_header(request, cookie=cookie)

    if data is not None:
        data = urlencode(data)
        data = data.encode('utf-8')
    response = urlopen(request, data=data, context=context)
    return response

