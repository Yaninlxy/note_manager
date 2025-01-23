def display_notes(notes):
    """
    Отображает список заметок.
    """
    if not notes:
        print("Нет доступных заметок.")
        return

    for i, note in enumerate(notes, start=1):
        print(f"Заметка {i}:")
        print(f"  Имя пользователя: {note['username']}")
        print(f"  Заголовок: {note['title']}")
        print(f"  Описание: {note['content']}")
        print(f"  Статус: {note['status']}")
        print(f"  Дата создания: {note['created_date']}")
        print(f"  Дедлайн: {note['issue_date']}")
        print("---")


def add_new_note():
    """
    Добавляет новую заметку через ввод пользователя.
    """
    username = input("Введите имя пользователя: ")
    title = input("Введите заголовок заметки: ")
    content = input("Введите описание: ")
    status = input("Введите статус (новая, в процессе, выполнена): ")
    created_date = input("Введите дату создания (дд-мм-гггг): ")
    issue_date = input("Введите дедлайн (дд-мм-гггг): ")

    return {
        "username": username,
        "title": title,
        "content": content,
        "status": status,
        "created_date": created_date,
        "issue_date": issue_date,
    }
