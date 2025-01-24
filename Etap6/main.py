from db_operations import create_table, save_note_to_db, load_notes_from_db, update_note_in_db, delete_note_from_db

def input_note():
    """
    Ввод данных новой заметки пользователем.
    :return: словарь с данными заметки
    """
    username = input("Введите имя пользователя: ")
    title = input("Введите заголовок заметки: ")
    content = input("Введите содержимое заметки: ")
    status = input("Введите статус (Например: В процессе, Завершено): ")
    created_date = input("Введите дату создания (в формате день-месяц-год): ")
    issue_date = input("Введите дедлайн (в формате день-месяц-год): ")

    return {
        "username": username,
        "title": title,
        "content": content,
        "status": status,
        "created_date": created_date,
        "issue_date": issue_date
    }

def add_note_handler(db_path):
    """
    Обработчик для добавления новой заметки.
    :param db_path: путь к базе данных SQLite
    """
    print("Добавление новой заметки:")
    note = input_note()
    save_note_to_db(note, db_path)

def update_note_handler(db_path):
    """
    Обработчик для обновления заметки.
    :param db_path: путь к базе данных SQLite
    """
    try:
        note_id = int(input("Введите ID заметки, которую хотите обновить: "))
        print("Введите новые данные для заметки:")
        updates = {
            "title": input("Новый заголовок: "),
            "content": input("Новое содержимое: "),
            "status": input("Новый статус (Например: В процессе, Завершено): "),
            "issue_date": input("Новый дедлайн (в формате день-месяц-год): ")
        }
        update_note_in_db(note_id, updates, db_path)
    except ValueError:
        print("Ошибка: ID должен быть числом.")

def delete_note_handler(db_path):
    """
    Обработчик для удаления заметки.
    :param db_path: путь к базе данных SQLite
    """
    try:
        note_id = int(input("Введите ID заметки, которую хотите удалить: "))
        delete_note_from_db(note_id, db_path)
    except ValueError:
        print("Ошибка: ID должен быть числом.")

def list_notes_handler(db_path):
    """
    Обработчик для отображения всех заметок.
    :param db_path: путь к базе данных SQLite
    """
    notes = load_notes_from_db(db_path)
    if notes:
        print("Список заметок:")
        for note in notes:
            print(f"ID: {note['id']}, Пользователь: {note['username']}, Заголовок: {note['title']}, Статус: {note['status']}, Дата создания: {note['created_date']}, Дедлайн: {note['issue_date']}")
    else:
        print("Заметок нет.")

def main():
    db_path = 'note_manager.db'
    create_table(db_path)

    while True:
        print("\nМеню:")
        print("1. Добавить заметку")
        print("2. Обновить заметку")
        print("3. Удалить заметку")
        print("4. Показать все заметки")
        print("5. Выйти")

        choice = input("Выберите действие (1-5): ")
        if choice == '1':
            add_note_handler(db_path)
        elif choice == '2':
            update_note_handler(db_path)
        elif choice == '3':
            delete_note_handler(db_path)
        elif choice == '4':
            list_notes_handler(db_path)
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Ошибка: выберите действие от 1 до 5.")

if __name__ == "__main__":
    main()
