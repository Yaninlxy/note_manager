from note_functions import (
    create_note, display_notes, update_note, delete_note, search_notes
)
from colorama import Fore, Style, init

# Инициализация библиотеки colorama
init(autoreset=True)

def menu():
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
    print(Fore.BLUE + "\n--- Создание новой заметки ---")
    create_note()

def handle_display_notes():
    print(Fore.BLUE + "\n--- Показ всех заметок ---")
    display_notes()

def handle_update_note():
    print(Fore.BLUE + "\n--- Обновление заметки ---")
    update_note()

def handle_delete_note():
    print(Fore.BLUE + "\n--- Удаление заметки ---")
    confirm = input(Fore.YELLOW + "Вы уверены, что хотите удалить заметку? (да/нет): ").strip().lower()
    if confirm == "да":
        delete_note()
    else:
        print(Fore.CYAN + "Удаление отменено.")

def handle_search_notes():
    print(Fore.BLUE + "\n--- Поиск заметок ---")
    keyword = input(Fore.YELLOW + "Введите ключевое слово для поиска (или оставьте пустым): ").strip()
    status = input(Fore.YELLOW + "Введите статус для поиска (или оставьте пустым): ").strip()
    search_notes(keyword=keyword if keyword else None, status=status if status else None)

if __name__ == "__main__":
    menu()
