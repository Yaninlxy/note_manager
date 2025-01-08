"""
create_note_function.py
Функция для создания заметки.
"""
from datetime import datetime

def create_note():
    """Создание новой заметки."""
    username = input("Введите имя пользователя: ").strip()
    title = input("Введите заголовок заметки: ").strip()
    content = input("Введите содержание заметки: ").strip()
    status = input("Введите статус заметки (например, новая, выполнена): ").strip()

    issue_date = input("Введите дату завершения (дд-мм-гггг): ").strip()
    try:
        issue_date = datetime.strptime(issue_date, "%d-%m-%Y").strftime("%d-%m-%Y")
    except ValueError:
        print("Неверный формат даты. Используйте формат дд-мм-гггг.")
        return None

    note = {
        "username": username,
        "title": title,
        "content": content,
        "status": status,
        "created_date": datetime.now().strftime("%d-%m-%Y"),
        "issue_date": issue_date
    }
    print("Заметка успешно создана!")
    return note

if __name__ == "__main__":
    note = create_note()
    print("Созданная заметка:", note)
