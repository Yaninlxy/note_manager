def search_notes(notes, keyword=None, status=None):
    """
    Ищет заметки по ключевому слову и/или статусу.

    :param notes: список заметок (список словарей)
    :param keyword: ключевое слово для поиска (строка)
    :param status: статус заметки для поиска (строка)
    :return: список найденных заметок
    """
    if not notes:
        print("Список заметок пуст.")
        return []
    
    # Результаты поиска
    results = []
    
    for note in notes:
        # Проверяем совпадение по ключевому слову
        matches_keyword = (
            keyword.lower() in note["title"].lower() or
            keyword.lower() in note["content"].lower() or
            keyword.lower() in note["username"].lower()
        ) if keyword else True

        # Проверяем совпадение по статусу
        matches_status = note["status"] == status if status else True

        # Добавляем заметку, если все условия совпадают
        if matches_keyword and matches_status:
            results.append(note)

    # Вывод результатов
    if not results:
        print("Заметки, соответствующие запросу, не найдены.")
    else:
        print("\nНайдены заметки:")
        for idx, note in enumerate(results, 1):
            print(f"\nЗаметка №{idx}:")
            print(f"Имя пользователя: {note['username']}")
            print(f"Заголовок: {note['title']}")
            print(f"Описание: {note['content']}")
            print(f"Статус: {note['status']}")
            print(f"Дата создания: {note['created_date']}")
            print(f"Дедлайн: {note['issue_date']}")

    return results


def interactive_search(notes):
    """
    Интерфейс для поиска заметок. Позволяет пользователю вводить критерии через консоль.
    """
    print("\nДобро пожаловать в поиск заметок!")
    print("Вы можете выполнить поиск по ключевому слову, статусу или обоим критериям.")
    
    keyword = input("Введите ключевое слово для поиска (нажмите Enter, чтобы пропустить): ").strip()
    status = input("Введите статус для поиска (нажмите Enter, чтобы пропустить): ").strip()
    
    # Если пользователь ничего не ввёл
    keyword = None if keyword == "" else keyword
    status = None if status == "" else status
    
    print("\nРезультаты поиска:")
    search_notes(notes, keyword=keyword, status=status)


# Пример работы функции
if __name__ == "__main__":
    notes = [
        {
            'username': 'Алексей',
            'title': 'Список покупок',
            'content': 'Купить продукты на неделю',
            'status': 'новая',
            'created_date': '27-11-2024',
            'issue_date': '30-11-2024'
        },
        {
            'username': 'Мария',
            'title': 'Учеба',
            'content': 'Подготовиться к экзамену',
            'status': 'в процессе',
            'created_date': '25-11-2024',
            'issue_date': '01-12-2024'
        },
        {
            'username': 'Иван',
            'title': 'План работы',
            'content': 'Завершить проект',
            'status': 'выполнено',
            'created_date': '20-11-2024',
            'issue_date': '26-11-2024'
        }
    ]

    # Запуск интерактивного поиска
    interactive_search(notes)
