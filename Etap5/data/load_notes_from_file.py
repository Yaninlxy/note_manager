import os


def load_notes_from_file(filename):
    """
    Загружает заметки из файла в формате YAML.
    Возвращает список заметок в виде словарей.
    """
    notes = []
    if not os.path.exists(filename):
        print(f"Файл {filename} не найден. Создан новый файл.")
        open(filename, 'w').close()
        return notes
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            note = {}
            for line in file:
                line = line.strip()
                if line == "---":
                    if note:
                        notes.append(note)
                        note = {}
                elif line:
                    key, value = line.split(": ", 1)
                    note[key.lower().replace(" ", "_")] = value
            if note:  # Добавить последнюю заметку, если есть
                notes.append(note)
    except Exception as e:
        print(f"Ошибка при чтении файла {filename}: {e}")
    return notes
