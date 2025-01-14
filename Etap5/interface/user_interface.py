def show_menu():
    """
    Отображает главное меню и возвращает выбор пользователя.
    """
    print("=== Меню ===")
    print("1. Просмотреть заметки")
    print("2. Добавить заметку")
    print("3. Удалить заметку")
    print("4. Поиск заметки")
    print("5. Выход")
    
    while True:
        choice = input("Выберите действие (1-5): ")
        if choice in {"1", "2", "3", "4", "5"}:
            return int(choice)
        print("Ошибка: Введите число от 1 до 5.")

def display_notes(notes):
    """
    Отображает список заметок в удобном формате.
    """
    if not notes:
        print("Заметок нет.")
        return
    
    print("=== Заметки ===")
    for idx, note in enumerate(notes, start=1):
        print(f"{idx}. {note['title']} (Статус: {note['status']})")
        print(f"   Пользователь: {note['username']}")
        print(f"   Создано: {note['created_date']} | Дедлайн: {note['issue_date']}")
        print(f"   Описание: {note['content']}")
        print("---")

def get_new_note():
    """
    Запрашивает у пользователя данные для новой заметки.
    """
    print("=== Добавление новой заметки ===")
    username = input("Введите имя пользователя: ").strip()
    title = input("Введите заголовок заметки: ").strip()
    content = input("Введите описание заметки: ").strip()
    status = input("Введите статус (новая/в процессе/завершена): ").strip()
    created_date = input("Введите дату создания (дд-мм-гггг): ").strip()
    issue_date = input("Введите дедлайн (дд-мм-гггг): ").strip()
    
    return {
        "username": username,
        "title": title,
        "content": content,
        "status": status,
        "created_date": created_date,
        "issue_date": issue_date
    }

def get_note_id_for_deletion():
    """
    Запрашивает у пользователя ID заметки для удаления.
    """
    return input("Введите ID заметки, которую хотите удалить: ").strip()

def search_note_by_title(notes):
    """
    Позволяет пользователю искать заметку по заголовку.
    """
    search_query = input("Введите заголовок для поиска: ").strip().lower()
    results = [note for note in notes if search_query in note["title"].lower()]
    
    if not results:
        print("Заметки с таким заголовком не найдены.")
    else:
        print("=== Найденные заметки ===")
        display_notes(results)
