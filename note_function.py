import datetime

def validate_date(date_str):
    """Проверяет формат даты (день-месяц-год)."""
    try:
        datetime.datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False


def update_note(note):
    """
    Обновляет указанное поле заметки.
    
    Аргументы:
        note (dict): Словарь с данными заметки.
    
    Возвращает:
        dict: Обновлённый словарь заметки.
    """
    if not isinstance(note, dict):
        raise ValueError("Ожидается словарь в качестве заметки.")
    
    print("Текущие данные заметки:")
    for key, value in note.items():
        print(f"{key}: {value}")

    fields = ["username", "title", "content", "status", "issue_date"]
    while True:
        field = input(f"Какие данные вы хотите обновить? ({', '.join(fields)}): ").strip()
        if field not in fields:
            print("Некорректное имя поля. Пожалуйста, выберите из доступных.")
            continue
        
        new_value = input(f"Введите новое значение для {field}: ").strip()
        
        if field == "issue_date":
            if not validate_date(new_value):
                print("Некорректный формат даты. Укажите дату в формате 'день-месяц-год'.")
                continue
        
        note[field] = new_value
        print("\nЗаметка обновлена:")
        for key, value in note.items():
            print(f"{key}: {value}")
        
        confirm = input("Хотите обновить ещё одно поле? (да/нет): ").strip().lower()
        if confirm != "да":
            break

    return note


# Демонстрация работы
if __name__ == "__main__":
    example_note = {
        'username': 'Алексей',
        'title': 'Список покупок',
        'content': 'Купить продукты на неделю',
        'status': 'новая',
        'created_date': '27-11-2024',
        'issue_date': '30-11-2024'
    }
    
    updated_note = update_note(example_note)
    print("\nИтоговая версия заметки:")
    for key, value in updated_note.items():
        print(f"{key}: {value}")
