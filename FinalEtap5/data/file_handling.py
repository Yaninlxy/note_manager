import os

def save_notes_to_file(notes, filename):
    """
    Сохраняет заметки в файл в формате YAML.
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
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")

def append_notes_to_file(notes, filename):
    """
    Добавляет новые заметки в существующий файл в формате YAML.
    """
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            for note in notes:
                file.write(f"Имя пользователя: {note['username']}\n")
                file.write(f"Заголовок: {note['title']}\n")
                file.write(f"Описание: {note['content']}\n")
                file.write(f"Статус: {note['status']}\n")
                file.write(f"Дата создания: {note['created_date']}\n")
                file.write(f"Дедлайн: {note['issue_date']}\n")
                file.write("---\n")
    except Exception as e:
        print(f"Ошибка при добавлении заметок в файл: {e}")

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
