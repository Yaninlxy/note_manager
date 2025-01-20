from FinalEtap5.data import save_notes_to_file, load_notes_from_file
from FinalEtap5.utils import validate_date, validate_status, generate_unique_id
from FinalEtap5.interface import display_menu, display_notes

def main():
    notes = load_notes_from_file("notes.txt")
    while True:
        choice = display_menu()
        if choice == '1':
            title = input("Введите заголовок: ")
            content = input("Введите содержание: ")
            status = input("Введите статус (новая/в процессе/выполнена): ")
            if validate_status(status):
                note_id = generate_unique_id()
                note = {"id": note_id, "title": title, "content": content, "status": status}
                notes.append(note)
                save_notes_to_file(notes, "notes.txt")
                print("Заметка добавлена.")
            else:
                print("Неверный статус.")
        elif choice == '2':
            display_notes(notes)
        elif choice == '3':
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
