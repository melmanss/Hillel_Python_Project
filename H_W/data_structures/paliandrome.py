def is_palindrome(text):
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


user_input = input("Введіть рядок: ")
print(is_palindrome(user_input))
