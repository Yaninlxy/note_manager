def add_titles_loop():
    """
    Запрашивает у пользователя заголовки заметок и возвращает список уникальных заголовков.
    """
    titles = set()
    print("Добавляйте заголовки заметок. Оставьте пустым для завершения.")

    while True:
        title = input("Введите заголовок или оставьте пустым и нажмите 'Enter' для выхода: ").strip()
        if not title:
            break
        if title.lower() in map(str.lower, titles):
            print("Заголовок уже существует. Попробуйте другой.")
        else:
            titles.add(title)
            print("Заголовок добавлен.")

    print("\nИтоговые заголовки:")
    for idx, title in enumerate(titles, 1):
        print(f"{idx}. {title}")

if __name__ == "__main__":
    add_titles_loop()
