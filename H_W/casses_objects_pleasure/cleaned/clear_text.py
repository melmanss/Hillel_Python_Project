import re


def delete_html_tags(input_file: str, output_file: str = "cleaned.txt") -> None:
    """
    Зчитати HTML-файл, видалити всі теги та зберегти результат в інший файл.

    Аргументи:
        назва_вхідного_файлу: Шлях до файлу, який потрібно очистити.
        назва_вихідного_файлу: Шлях до файлу для запису (за замовчуванням "cleaned.txt").
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content: str = file.read()

        tag_pattern: str = r'<[^>]*>'
        cleaned_text: str = re.sub(tag_pattern, '', content)

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(cleaned_text)

    except FileNotFoundError:
        print(f"Помилка: Файл {input_file} не знайдено.")


delete_html_tags('draft.html')