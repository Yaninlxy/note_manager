"""
menu.py
Меню действий для работы с заметками.
"""
from create_note_function import create_note
from display_notes_function import display_notes
from update_note_function import update_note
from search_notes_function import search_notes

notes = []

def menu():
    while True:
        print("""
        Меню действий:
        1. Создать новую заметку
        2. Показать все заметки
        3. Обновить заметку
        4. Найти заметки
        5. Выйти
        """)
        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            note = create_note()
            if note:
                notes.append(note)
        elif choice == "2":
            display_notes(notes)
        elif choice == "3":
            display_notes(notes)
            index = int(input("Введите номер заметки для обновления: ")) - 1
            if 0 <= index < len(notes):
                notes[index] = update_note(notes[index])
        elif choice == "4":
            keyword = input("Введите ключевое слово: ")
            status = input("Введите статус (или оставьте пустым): ")
            search_notes(notes, keyword, status)
        elif choice == "5":
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    menu()
