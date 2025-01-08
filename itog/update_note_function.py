"""
update_note_function.py
Функция для обновления заметки.
"""

def update_note(note):
    """Обновление заметки."""
    print("\nТекущие данные заметки:")
    for key, value in note.items():
        print(f"{key.capitalize()}: {value}")

    field = input("Какое поле вы хотите обновить? (username, title, content, status, issue_date): ").strip()
    if field not in note:
        print("Некорректное поле.")
        return note

    new_value = input(f"Введите новое значение для {field}: ").strip()
    if field == "issue_date":
        from datetime import datetime
        try:
            new_value = datetime.strptime(new_value, "%d-%m-%Y").strftime("%d-%m-%Y")
        except ValueError:
            print("Неверный формат даты.")
            return note

    note[field] = new_value
    print("Заметка успешно обновлена!")
    return note

if __name__ == "__main__":
    note = {
        'username': 'Алексей',
        'title': 'Список покупок',
        'content': 'Купить продукты',
        'status': 'новая',
        'created_date': '27-11-2024',
        'issue_date': '30-11-2024'
    }
    updated_note = update_note(note)
    print("Обновлённая заметка:", updated_note)
