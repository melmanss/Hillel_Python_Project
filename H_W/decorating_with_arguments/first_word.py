import re
from typing import Optional


def first_word(text: str) -> str:
    """
    Знайти перше слово у переданому рядку.

    Слово може містити літери та апостроф. Знаки пунктуації та пробіли
    на початку рядка ігноруються.
    """
    pattern: str = r"[a-zA-Zа-яА'ʼ]+"
    match: Optional[re.Match] = re.search(pattern, text)

    return match.group(0) if match else ""


print(f"{first_word('Hello world')}")
print(f"{first_word(' a word ')}")
print(f"{first_word('... and so on ...')}")
print(f"{first_word("don't touch it")}")
print(f"{first_word('greetings, friends')}")
print(f"{first_word('...and... ')}")
print(f"{first_word('only one')}")