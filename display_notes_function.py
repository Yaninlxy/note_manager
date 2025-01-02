from datetime import datetime

def validate_date(date_str):
    """Проверяет, является ли строка корректной датой в формате 'день-месяц-год'."""
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False

def update_note(note):
    """Обновляет указанное поле в заметке."""
    print("Текущие данные заметки:")
    for key, value in note.items():
        print(f"{key}: {value}")

    updatable_fields = ["username", "title", "content", "status", "issue_date"]
    print("\nВы можете обновить следующие поля:", ", ".join(updatable_fields))

    while True:
        field = input("Введите имя поля для обновления (или оставьте пустым для выхода): ").strip()
        if not field:
            print("Обновление завершено.")
            break

        if field not in updatable_fields:
            print("Некорректное поле. Попробуйте снова.")
            continue

        current_value = note.get(field)
        print(f"Текущее значение поля '{field}': {current_value}")

        new_value = input(f"Введите новое значение для '{field}' (или оставьте пустым, чтобы не менять): ").strip()
        if not new_value:
            print(f"Поле '{field}' осталось без изменений.")
            continue

        if field == "status" and new_value.lower() not in ["новая", "в процессе", "выполнено"]:
            print("Некорректный статус. Выберите из: 'новая', 'в процессе', 'выполнено'.")
            continue

        if field == "issue_date" and not validate_date(new_value):
            print("Некорректный формат даты. Используйте формат 'день-месяц-год'.")
            continue

        confirmation = input(f"Вы уверены, что хотите обновить '{field}'? (да/нет): ").strip().lower()
        if confirmation == "да":
            note[field] = new_value
            print(f"Поле '{field}' успешно обновлено.")
        else:
            print(f"Поле '{field}' не было изменено.")

    print("\nОбновлённая заметка:")
    for key, value in note.items():
        print(f"{key}: {value}")

    return note

# Пример использования
example_note = {
    "username": "Алексей",
    "title": "Список покупок",
    "content": "Купить продукты на неделю",
    "status": "новая",
    "created_date": "27-11-2024",
    "issue_date": "30-11-2024"
}

update_note(example_note)
