from dataclasses import dataclass


@dataclass
class Problem:
    """
    id           : 문제 번호
    title        : 문제 제목
    limit_time   : 제한 시간
    limit_memory : 제한 메모리
    description  : 문제 설명
    input        : 문제 입력 예시
    output       : 문제 출력 예시
    """
    id: int
    title: str
    limit_time: str = ''
    limit_memory: str = ''
    description: str = ''
    input: str = ''
    output: str = ''

    def __eq__(self, other: "Problem") -> bool:
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
