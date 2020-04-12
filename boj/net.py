from typing import List

import requests
import asyncio
from aiohttp import ClientSession


def get_url(url: str, cookie: str = None):
    """
    Get 요청을 url로 보냄

    :param url:    요청할 url
    :param cookie: http 통신할 때 같이 보낼 쿠키 값
    :return:       요청 후 받은 http response
    """

    if cookie is not None:
        cookie = {'Cookie': cookie}
    return requests.get(url, headers=cookie)


async def async_get_url(url: str, session: ClientSession, cookie: str = None):
    """
    Network 통신의 async 작업을 수행

    :param url: 파싱할 url
    :param session: async 통신을 위한 aiohttp session
    :param cookie: network 통신에 필요한 로그인 세션
    :return: async read 결과
    """
    if cookie is not None:
        cookie = {'Cookie': cookie}  # TODO: 쿠키 값을 request에 넣어야 함
    async with session.get(url) as response:
        return await response.read()


async def get_multiple_url(url_list: List[str], cookie: str = None):
    """
    Network 작업이 느린 것을 async 작업으로 받아온 값을 합침

    :param url_list: 파싱할 url list
    :param cookie: network 통신에 필요한 로그인 세션
    :return: url list의 파싱 async 결과
    """
    tasks = []
    async with ClientSession() as session:
        for url in url_list:
            res = asyncio.ensure_future(async_get_url(url, session, cookie))
            tasks.append(res)

        return await asyncio.gather(*tasks)


def fast_get_multiple_url(url_list: List[str], cookie: str = None) -> List[str]:
    """
    Network 작업이 느린 것을 multi-thread 로 값을 받아옴으로서 속도를 향상시킴

    :param url_list: 파싱할 url list
    :param cookie: network 통신에 필요한 로그인 세션
    :return: url list의 파싱 결과 리스트
    """
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(get_multiple_url(url_list, cookie))
    res = loop.run_until_complete(future)
    return res


def post_url(url: str, data):
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
