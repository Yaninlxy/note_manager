from data import save_notes_to_file, load_notes_from_file
from interface import display_notes, add_new_note
from utils import generate_unique_id

FILE_PATH = "notes.json"

def main():
    notes = load_notes_from_file(FILE_PATH)

    while True:
        print("1. Показать заметки")
        print("2. Добавить заметку")
        print("3. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            display_notes(notes)
        elif choice == "2":
            new_note = add_new_note()
            new_note["id"] = generate_unique_id()
            notes.append(new_note)
            save_notes_to_file(notes, FILE_PATH)
        elif choice == "3":
            print("До свидания!")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
