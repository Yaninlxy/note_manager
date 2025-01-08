from load_notes_from_file import load_notes_from_file

if __name__ == "__main__":
    # Имя файла с заметками
    filename = "notes.txt"

    # Загрузка заметок из файла
    loaded_notes = load_notes_from_file(filename)

    # Вывод загруженных заметок
    if loaded_notes:
        print("Загруженные заметки:")
        for note in loaded_notes:
            print(note)
    else:
        print("Файл пуст или отсутствуют заметки.")
