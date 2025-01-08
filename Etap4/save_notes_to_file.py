def save_notes_to_file(notes, filename):
    """
    Сохраняет список заметок в текстовый файл.
    :param notes: список заметок (список словарей)
    :param filename: имя файла для сохранения
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for note in notes:
                file.write(f"Имя пользователя: {note['username']}\n")
                file.write(f"Заголовок: {note['title']}\n")
                file.write(f"Описание: {note['content']}\n")
                file.write(f"Статус: {note['status']}\n")
                file.write(f"Дата создания: {note['created_date']}\n")
                file.write(f"Дедлайн: {note['issue_date']}\n")
                file.write("---\n")
        print("Заметки успешно сохранены в файл.")
    except Exception as e:
        print(f"Ошибка при сохранении заметок: {e}")
