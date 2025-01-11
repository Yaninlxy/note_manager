def delete_note():
    """
    Удаляет заметку по имени пользователя или заголовку, обрабатывая список корректно.
    """
    notes = [
        {"username": "Алексей", "title": "Список покупок", "content": "Купить продукты"},
        {"username": "Мария", "title": "Учёба", "content": "Подготовиться к экзамену"}
    ]

    print("\nТекущие заметки:")
    for idx, note in enumerate(notes, 1):
        print(f"{idx}. {note['title']} - {note['username']}")

    target = input("Введите заголовок или имя пользователя для удаления заметки: ").strip()
    found = False

    for note in notes[:]:  # Создаём копию списка для безопасного удаления
        if target.lower() in (note['title'].lower(), note['username'].lower()):
            notes.remove(note)
            found = True
            print("Заметка успешно удалена.")

    if not found:
        print("Заметка не найдена.")

    print("\nОставшиеся заметки:")
    for idx, note in enumerate(notes, 1):
        print(f"{idx}. {note}")

if __name__ == "__main__":
    delete_note()
