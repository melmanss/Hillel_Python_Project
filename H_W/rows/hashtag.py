import string


def create_hashtag(text: str) -> str:
    """
    Перетворює вхідний рядок на хештег у форматі CamelCase.

    Args:
        text (str): Вхідний рядок для обробки.

    Returns:
        str: Сформований хештег (макс. 140 символів).
    """
    clean_text = "".join(
        char for char in text if char not in string.punctuation
    )

    words = clean_text.split()
    capitalized_words = [word.capitalize() for word in words]

    hashtag = "#" + "".join(capitalized_words)

    if len(hashtag) > 140:
        hashtag = hashtag[:140]

    return hashtag


user_input = input("Введіть рядок для перетворення: ")
result = create_hashtag(user_input)

print(f"Ваш хештег: {result}")