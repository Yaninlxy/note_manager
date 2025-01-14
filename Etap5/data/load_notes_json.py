import json
import os


def load_notes_json(filename):
    """
    Загружает заметки из файла в формате JSON.
    Возвращает список заметок.
    """
    if not os.path.exists(filename):
        print(f"Файл {filename} не найден. Создан новый файл.")
        open(filename, 'w').close()
        return []
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f"Ошибка: JSON-файл {filename} поврежден или пуст.")
        return []
    except Exception as e:
        print(f"Ошибка при чтении JSON-файла {filename}: {e}")
        return []
