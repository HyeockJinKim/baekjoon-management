import requests


def get_url(url, cookie=None):
    """
    Get request to url

    :param url:    url for parsing page
    :param data:   post data
    :param cookie: cookie for http
    :return:       http response
    """

    if cookie is not None:
        cookie = {'Cookie': cookie}
    return requests.get(url, headers=cookie)


def post_url(url, data):
    """
    Post request to url
    :param url:    url for parsing page
    :param data:   post data
    :param cookie: cookie for http
    :return:       http response
    """

    return requests.post(url, data, allow_redirects=False)


def process_cookie(cookie):
    """
    Make 'Set-Cookie' header's value to put in the 'Cookie' header

    :param cookie: 'Set-Cookie' header value
    :return:       'Cookie' header value
    """

    login_cookie = []
    for cook in cookie.split(' '):
        if '__cfduid=' in cook:
            login_cookie.append(cook)
            login_cookie.append(' ')
        elif 'OnlineJudge=' in cook:
            login_cookie.append(cook)
    return ''.join(login_cookie)
