def load_notes_from_file(filename):
    """
    Загружает заметки из текстового файла и возвращает их в виде списка словарей.
    :param filename: имя файла для загрузки
    :return: список заметок (список словарей)
    """
    notes = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            note = {}
            for line in file:
                line = line.strip()
                if not line:
                    continue
                if line == "---":
                    if note:  # Добавляем заметку в список, если она не пустая
                        notes.append(note)
                        note = {}
                else:
                    key, value = line.split(": ", 1)
                    if key == "Имя пользователя":
                        note["username"] = value
                    elif key == "Заголовок":
                        note["title"] = value
                    elif key == "Описание":
                        note["content"] = value
                    elif key == "Статус":
                        note["status"] = value
                    elif key == "Дата создания":
                        note["created_date"] = value
                    elif key == "Дедлайн":
                        note["issue_date"] = value
            if note:  # Добавляем последнюю заметку, если файл не заканчивается "---"
                notes.append(note)
        print("Заметки успешно загружены из файла.")
    except FileNotFoundError:
        print(f"Файл {filename} не найден. Возвращён пустой список.")
    except Exception as e:
        print(f"Ошибка при загрузке заметок: {e}")
    return notes
