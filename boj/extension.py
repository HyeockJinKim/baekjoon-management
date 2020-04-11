import enum


class Extension(enum.Enum):
    C = '.c'
    CPP = '.cpp'
    JAVA = '.java'
    PYTHON = '.py'
    GO = '.go'
    RUST = '.rs'
    RUBY = '.rb'
    KOTLIN = '.kt'

    @staticmethod
    def from_language(lang: str):
        """
        언어에서 확장자를 얻어내는 함수

        :param lang: 프로그래밍 언어
        :return:     프로그래밍 언어와 매칭되는 확장자 enum
        """
        if lang in ['C', 'C11', 'C (Clang)', 'C11 (Clang)']:
            return Extension.C

        if lang in ['C++', 'C++11', 'C++14', 'C++17', 'C++ (Clang)', 'C++11 (Clang)', 'C++14 (Clang)', 'C++17 (Clang)']:
            return Extension.CPP

        if lang in ['Java', 'Java (OpenJDK)', 'Java 11']:
            return Extension.JAVA

        if lang in ['Python 2', 'Python 3', 'PyPy2', 'PyPy3']:
            return Extension.PYTHON

        if lang == 'Go':
            return Extension.GO

        if lang == 'Rust':
            return Extension.RUST

        if lang == 'Ruby 2.5':
            return Extension.RUBY

        if lang in ['Kotlin (JVM)', 'Kotlin (Native)']:
            return Extension.KOTLIN
