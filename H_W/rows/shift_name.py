import string
import keyword


def is_valid_variable_name(name: str) -> bool:
    """
    Перевіряє, чи може цей рядок бути ім'ям змінної, згідно зі специфічними правилами.

    Правила включають: заборона починати з цифри,
    відсутність великих літер, пробілів та знаків пунктуації (крім підкреслення),
    а також обмеження на кількість знаків підкреслення.

    Args:
        name (str): Рядок, який потрібно перевірити.

    Returns:
        bool: True, якщо таке ім'я змінної допустимо, або False - якщо ні.
    """
    if name in keyword.kwlist:
        return False

    if name[0].isdigit():
        return False

    for char in name:
        if char.isupper() or char.isspace():
            return False

    forbidden_punctuation = string.punctuation.replace("_", "")
    for char in name:
        if char in forbidden_punctuation:
            return False

    if name.count("_") > 1:
        return False

    return True


user_input = input("Введіть ім'я змінної: ")
print(is_valid_variable_name(user_input))