from utils.validators import validate_date, validate_status
from data import save_notes_to_file, load_notes_from_file
from interface import display_notes, add_new_note
from utils import generate_unique_id


FILENAME = "notes.txt"

def main():
    notes = load_notes_from_file(FILENAME)

    while True:
        print("\nМеню:")
        print("1. Показать заметки")
        print("2. Добавить заметку")
        print("3. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            display_notes(notes)
        elif choice == "2":
            new_note = add_new_note()
            if not validate_date(new_note["created_date"]):
                print("Некорректная дата создания.")
                continue
            if not validate_date(new_note["issue_date"]):
                print("Некорректный дедлайн.")
                continue
            if not validate_status(new_note["status"]):
                print("Некорректный статус.")
                continue

            new_note["id"] = generate_unique_id()
            notes.append(new_note)
            save_notes_to_file(notes, FILENAME)
            print("Заметка добавлена!")
        elif choice == "3":
            print("Выход.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
