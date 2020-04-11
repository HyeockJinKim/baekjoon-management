from dataclasses import dataclass


@dataclass
class Solution:
    """
    id           : 문제 번호
    success      : 성공 여부 및 점수
    time         : 걸린 시간
    memory       : 사용 메모리
    language     : 사용 프로그래밍 언어
    length       : 소스 코드 길이
    """
    id: int
    success: str
    time: str
    memory: str
    language: str
    length: str

    def __eq__(self, other: "Solution") -> bool:
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
