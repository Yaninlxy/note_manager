# Обработка уже встроена в функции выше.
# Пример использования:
if __name__ == "__main__":
    try:
        notes = load_notes_from_file("missing_file.txt")
    except Exception as e:
        print(f"Ошибка: {e}")
