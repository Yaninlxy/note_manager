from colorama import Fore, Style, init
from create_note_function import create_note
from update_note_function import update_note
from display_notes_function import display_notes
from search_notes_function import search_notes

# Инициализация библиотеки colorama
init(autoreset=True)

# Глобальный список заметок
notes = []

def menu():
    """Главное меню программы."""
    while True:
        print(Fore.CYAN + "\nМеню действий:")
        print(Fore.GREEN + "1. Создать новую заметку")
        print("2. Показать все заметки")
        print("3. Обновить заметку")
        print("4. Удалить заметку")
        print("5. Найти заметки")
        print(Fore.RED + "6. Выйти из программы")

        try:
            choice = input(Fore.YELLOW + "\nВаш выбор: ").strip()

            if choice == "1":
                handle_create_note()
            elif choice == "2":
                handle_display_notes()
            elif choice == "3":
                handle_update_note()
            elif choice == "4":
                handle_delete_note()
            elif choice == "5":
                handle_search_notes()
            elif choice == "6":
                print(Fore.MAGENTA + "Программа завершена. Спасибо за использование!")
                break
            else:
                print(Fore.RED + "Неверный выбор. Пожалуйста, выберите действие из списка.")
        except Exception as e:
            print(Fore.RED + f"Ошибка: {e}. Попробуйте снова.")

def handle_create_note():
    """Обработчик создания новой заметки."""
    print(Fore.BLUE + "\n--- Создание новой заметки ---")
    note = create_note()
    if note:
        notes.append(note)
        print(Fore.GREEN + "Заметка успешно создана!")

def handle_display_notes():
    """Обработчик отображения всех заметок."""
    print(Fore.BLUE + "\n--- Показ всех заметок ---")
    display_notes(notes)

def handle_update_note():
    """Обработчик обновления заметки."""
    if not notes:
        print(Fore.RED + "Нет доступных заметок для обновления.")
        return

    print(Fore.BLUE + "\n--- Обновление заметки ---")
    display_notes(notes)
    try:
        index = int(input(Fore.YELLOW + "Введите номер заметки для обновления: ")) - 1
        if 0 <= index < len(notes):
            notes[index] = update_note(notes[index])
            print(Fore.GREEN + "Заметка успешно обновлена!")
        else:
            print(Fore.RED + "Некорректный номер заметки.")
    except ValueError:
        print(Fore.RED + "Введите числовое значение.")

def handle_delete_note():
    """Обработчик удаления заметки."""
    if not notes:
        print(Fore.RED + "Нет доступных заметок для удаления.")
        return

    print(Fore.BLUE + "\n--- Удаление заметки ---")
    display_notes(notes)
    try:
        index = int(input(Fore.YELLOW + "Введите номер заметки для удаления: ")) - 1
        if 0 <= index < len(notes):
            confirm = input(Fore.YELLOW + "Вы уверены, что хотите удалить заметку? (да/нет): ").strip().lower()
            if confirm == "да":
                del notes[index]
                print(Fore.GREEN + "Заметка успешно удалена!")
            else:
                print(Fore.CYAN + "Удаление отменено.")
        else:
            print(Fore.RED + "Некорректный номер заметки.")
    except ValueError:
        print(Fore.RED + "Введите числовое значение.")

def handle_search_notes():
    """Обработчик поиска заметок."""
    if not notes:
        print(Fore.RED + "Нет доступных заметок для поиска.")
        return

    print(Fore.BLUE + "\n--- Поиск заметок ---")
    keyword = input(Fore.YELLOW + "Введите ключевое слово для поиска (или оставьте пустым): ").strip()
    status = input(Fore.YELLOW + "Введите статус для поиска (или оставьте пустым): ").strip()
    found_notes = search_notes(notes, keyword=keyword if keyword else None, status=status if status else None)
    display_notes(found_notes)

if __name__ == "__main__":
    menu()
