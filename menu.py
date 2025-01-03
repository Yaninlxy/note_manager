def main_menu():
    """
    Меню действий для управления заметками.
    """
    notes = []  # Список заметок
    while True:
        print("\nМеню действий:")
        print("1. Создать новую заметку")
        print("2. Поиск заметок")
        print("3. Отобразить все заметки")
        print("4. Выход")

        choice = input("Выберите действие: ")
        if choice == "1":
            # Вызов функции создания заметки (не включена в текущем примере)
            print("Функция создания заметок пока не реализована.")
        elif choice == "2":
            keyword = input("Введите ключевое слово для поиска (оставьте пустым для пропуска): ")
            status = input("Введите статус для поиска (новая, в процессе, выполнено, оставьте пустым для пропуска): ")
            search_notes(notes, keyword if keyword else None, status if status else None)
        elif choice == "3":
            if not notes:
                print("Заметок нет.")
            else:
                print("\nВсе заметки:")
                for idx, note in enumerate(notes, 1):
                    print(f"\nЗаметка №{idx}:")
                    print(f"Имя пользователя: {note['username']}")
                    print(f"Заголовок: {note['title']}")
                    print(f"Описание: {note['content']}")
                    print(f"Статус: {note['status']}")
                    print(f"Дата создания: {note['created_date']}")
                    print(f"Дедлайн: {note['issue_date']}")
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

# Запуск меню
if __name__ == "__main__":
    main_menu()
