from typing import List, Dict


def popular_words(text: str, words: List[str]) -> Dict[str, int]:
    """
    Підрахувати кількість входжень певних слів у заданому тексті.

    Пошук не залежить від регістру, а результат повертається у вигляді словника.
    """
    lower_text_words: List[str] = text.lower().split()
    result: Dict[str, int] = {
        word: lower_text_words.count(word)
        for word in words
    }

    return result


input_text: str = '''
When I was One
I had just begun
When I was Two
I was nearly new
'''
search_list: List[str] = ['i', 'was', 'three', 'near']

word_counts: Dict[str, int] = popular_words(input_text, search_list)
print(word_counts)
