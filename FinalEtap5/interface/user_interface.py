def display_menu():
    print("1. Добавить заметку")
    print("2. Показать заметки")
    print("3. Выйти")
    return input("Выберите действие: ")

def display_notes(notes):
    if not notes:
        print("Заметок нет.")
    else:
        for idx, note in enumerate(notes, 1):
            print(f"{idx}. {note}")
