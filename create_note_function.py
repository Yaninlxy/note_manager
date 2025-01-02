from datetime import datetime

def validate_date(date_str):
    """Проверяет корректность формата даты 'день-месяц-год'."""
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False

def create_note():
    """
    Создаёт новую заметку, запрашивая данные у пользователя.
    Возвращает словарь с полями заметки.
    """
    print("Создание новой заметки:")
    username = input("Введите имя пользователя: ").strip()
    title = input("Введите заголовок заметки: ").strip()
    content = input("Введите описание заметки: ").strip()

    # Выбор статуса из фиксированного списка
    statuses = ["новая", "в процессе", "выполнено"]
    while True:
        status = input(f"Введите статус заметки ({', '.join(statuses)}): ").strip().lower()
        if status in statuses:
            break
        print(f"Некорректный статус. Выберите из {statuses}.")

    # Автоматическое добавление текущей даты
    created_date = datetime.now().strftime("%d-%m-%Y")

    # Запрос даты дедлайна с проверкой формата
    while True:
        issue_date = input("Введите дату дедлайна (день-месяц-год): ").strip()
        if validate_date(issue_date):
            break
        print("Некорректный формат даты. Используйте формат 'день-месяц-год'.")

    # Формирование и возврат словаря
    note = {
        "username": username,
        "title": title,
        "content": content,
        "status": status,
        "created_date": created_date,
        "issue_date": issue_date,
    }
    return note

if __name__ == "__main__":
    new_note = create_note()
    print("\nЗаметка создана:", new_note)
