import string


def create_hashtag(text):
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