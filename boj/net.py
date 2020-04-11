import requests


def get_url(url, cookie=None):
    """
    Get 요청을 url로 보냄

    :param url:    요청할 url
    :param cookie: http 통신할 때 같이 보낼 쿠키 값
    :return:       요청 후 받은 http response
    """

    if cookie is not None:
        cookie = {'Cookie': cookie}
    return requests.get(url, headers=cookie)


def post_url(url, data):
    """
    Post 요청을 url로 보냄

    :param url:    요청할 url
    :param data:   url로 보낼 data
    :return:       요청 후 받은 http response
    """

    return requests.post(url, data, allow_redirects=False)


def process_cookie(cookie: str) -> str:
    """
    로그인 세션을 위한 cookie 설정

    :param cookie: 'Set-Cookie' 값에 있던 로그인 세션 정보
    :return:       로그인 세션이 포함된 'Cookie' 헤더
    """

    login_cookie = []
    for cook in cookie.split(' '):
        if '__cfduid=' in cook:
            login_cookie.append(cook)
            login_cookie.append(' ')
        elif 'OnlineJudge=' in cook:
            login_cookie.append(cook)
    return ''.join(login_cookie)
