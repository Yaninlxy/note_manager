# Файл: multiple_notes.py

def add_note(notes, name, title, description, status, creation_date, deadline):
    """Добавляет заметку в список."""
    note = {
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
    for i, note in enumerate(notes, start=1):
        print(f"{i}. Имя: {note['Имя']}")
        print(f"   Заголовок: {note['Заголовок']}")
        print(f"   Описание: {note['Описание']}")
        print(f"   Статус: {note['Статус']}")
        print(f"   Дата создания: {note['Дата создания']}")
        print(f"   Дедлайн: {note['Дедлайн']}\n")

def delete_note(notes, identifier):
    """Удаляет заметку по имени пользователя или заголовку."""
    for i, note in enumerate(notes):
        if note['Имя'] == identifier or note['Заголовок'] == identifier:
            del notes[i]
            print(f"Заметка '{identifier}' удалена.")
            return
    print(f"Заметка с именем или заголовком '{identifier}' не найдена.")

def main():
    """Главная функция для управления заметками."""
    notes = []
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

            add_note(notes, name, title, description, status, creation_date, deadline)

        elif action == "удалить":
            identifier = input("Введите имя пользователя или заголовок заметки для удаления: ")
            delete_note(notes, identifier)

        elif action == "показать":
            display_notes(notes)

        elif action == "выход":
            break

        else:
            print("Неверная команда. Пожалуйста, выберите 'добавить', 'удалить', 'показать' или 'выход'.")

if __name__ == "__main__":
    main()
