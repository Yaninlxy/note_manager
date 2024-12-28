# Файл: multiple_notes.py

def add_note(notes, name, title, description, status, creation_date, deadline, note_id):
    """Добавляет заметку в список."""
    note = {
        'ID': note_id,
        'Имя': name,
        'Заголовок': title,
        'Описание': description,
        'Статус': status,
        'Дата создания': creation_date,
        'Дедлайн': deadline
    }
    notes.append(note)

def display_notes(notes):
    """Отображает все заметки в понятном формате."""
    if not notes:
        print("Список заметок пуст.")
        return
    print("Список заметок:")
    for note in notes:
        print(f"ID: {note['ID']}")
        print(f"Имя: {note['Имя']}")
        print(f"Заголовок: {note['Заголовок']}")
        print(f"Описание: {note['Описание']}")
        print(f"Статус: {note['Статус']}")
        print(f"Дата создания: {note['Дата создания']}")
        print(f"Дедлайн: {note['Дедлайн']}\n")

def delete_note_by_id(notes, note_id):
    """Удаляет заметку по ID."""
    for i, note in enumerate(notes):
        if note['ID'] == note_id:
            del notes[i]
            print(f"Заметка с ID '{note_id}' удалена.")
            return
    print(f"Заметка с ID '{note_id}' не найдена.")

def main():
    """Главная функция для управления заметками."""
    notes = []
    note_id = 1  # Идентификатор для первой заметки
    print("Добро пожаловать в 'Менеджер заметок'! Вы можете добавить новую заметку.")

    while True:
        action = input("Выберите действие (добавить/удалить/показать/выход): ").strip().lower()
        
        if action == "добавить":
            name = input("Введите имя пользователя: ")
            title = input("Введите заголовок заметки: ")
            description = input("Введите описание заметки: ")
            status = input("Введите статус заметки (новая, в процессе, выполнено): ")
            creation_date = input("Введите дату создания (день-месяц-год): ")
            deadline = input("Введите дедлайн (день-месяц-год): ")

            add_note(notes, name, title, description, status, creation_date, deadline, note_id)
            note_id += 1  # Увеличиваем ID для следующей заметки

        elif action == "удалить":
            delete_action = input("Удалить по (ID/имени): ").strip().lower()
            if delete_action == "id":
                try:
                    note_id_to_delete = int(input("Введите ID заметки для удаления: "))
                    delete_note_by_id(notes, note_id_to_delete)
                except ValueError:
                    print("Пожалуйста, введите корректный числовой ID.")
            elif delete_action == "имени":
                identifier = input("Введите имя пользователя или заголовок заметки для удаления: ")
                delete_note_by_identifier(notes, identifier)
            else:
                print("Неверный выбор. Пожалуйста, выберите 'ID' или 'имени'.")

        elif action == "показать":
            display_notes(notes)

        elif action == "выход":
            break

        else:
            print("Неверная команда. Пожалуйста, выберите 'добавить', 'удалить', 'показать' или 'выход'.")

if __name__ == "__main__":
    main()
