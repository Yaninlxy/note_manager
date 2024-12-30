def create_note():
    """Функция для создания новой заметки."""
    note = {}
    
    # Ввод данных о заметке
    note['username'] = input("Введите имя пользователя: ")
    note['title'] = input("Введите заголовок заметки: ")
    note['description'] = input("Введите описание заметки: ")
    
    # Проверка на пустые значения
    while not note['description']:
        print("Описание не может быть пустым. Пожалуйста, введите описание.")
        note['description'] = input("Введите описание заметки: ")
    
    note['status'] = input("Введите статус заметки (новая, в процессе, выполнено): ").lower()
    
    # Проверка на корректность статуса
    while note['status'] not in ['новая', 'в процессе', 'выполнено']:
        print("Статус должен быть одним из: новая, в процессе, выполнено.")
        note['status'] = input("Введите статус заметки (новая, в процессе, выполнено): ").lower()
    
    # Ввод даты создания и дедлайна
    note['created_date'] = input("Введите дату создания (день-месяц-год): ")
    note['deadline'] = input("Введите дедлайн (день-месяц-год): ")
    
    return note


def display_notes(notes):
    """Функция для отображения списка всех заметок."""
    if not notes:
        print("Список заметок пуст.")
        return
    
    print("\nСписок заметок:")
    for idx, note in enumerate(notes, start=1):
        print(f"{idx}.")
        print(f"   Имя: {note['username']}")
        print(f"   Заголовок: {note['title']}")
        print(f"   Описание: {note['description']}")
        print(f"   Статус: {note['status']}")
        print(f"   Дата создания: {note['created_date']}")
        print(f"   Дедлайн: {note['deadline']}")
        print()


def delete_note(notes):
    """Функция для удаления заметки по имени пользователя или заголовку."""
    criteria = input("Введите имя пользователя или заголовок заметки для удаления: ")
    
    # Поиск заметки
    found_notes = [note for note in notes if note['username'] == criteria or note['title'] == criteria]
    
    if found_notes:
        for idx, note in enumerate(found_notes, start=1):
            print(f"{idx}. Заголовок: {note['title']}, Имя пользователя: {note['username']}")
        
        # Запрос у пользователя, какую заметку удалить
        try:
            choice = int(input("Введите номер заметки для удаления: ")) - 1
            note_to_delete = found_notes[choice]
            notes.remove(note_to_delete)
            print(f"Заметка '{note_to_delete['title']}' удалена.")
        except (ValueError, IndexError):
            print("Неверный выбор. Заметка не была удалена.")
    else:
        print("Заметки с таким именем пользователя или заголовком не найдены.")


def main():
    """Основная функция программы для управления заметками."""
    notes = []
    
    print('Добро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.')
    
    while True:
        # Создание новой заметки
        note = create_note()
        notes.append(note)
        
        # Запрос на добавление еще одной заметки
        add_another = input("Хотите добавить ещё одну заметку? (да/нет): ").strip().lower()
        if add_another != 'да':
            break
    
    # Отображение всех заметок
    display_notes(notes)
    
    # Возможность удалить заметку
    if notes:
        delete_option = input("Хотите удалить заметку? (да/нет): ").strip().lower()
        if delete_option == 'да':
            delete_note(notes)
    
    # Финальный вывод списка заметок
    display_notes(notes)


if __name__ == "__main__":
    main()
