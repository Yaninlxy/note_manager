from contacts import add_contact, get_all_contacts, search_contact, delete_contact

DB_PATH = "contacts.db"

def main():
    while True:
        print("\n--- Меню управления контактами ---")
        print("1. Добавить контакт")
        print("2. Показать все контакты")
        print("3. Найти контакт")
        print("4. Удалить контакт")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Введите имя: ")
            phone = input("Введите номер телефона: ")
            email = input("Введите email: ")
            add_contact(name, phone, email, DB_PATH)

        elif choice == "2":
            contacts = get_all_contacts(DB_PATH)
            if contacts:
                print("\n--- Список контактов ---")
                for contact in contacts:
                    print(f"ID: {contact[0]}, Имя: {contact[1]}, Телефон: {contact[2]}, Email: {contact[3]}")
            else:
                print("Список контактов пуст.")

        elif choice == "3":
            keyword = input("Введите имя или номер для поиска: ")
            results = search_contact(keyword, DB_PATH)
            if results:
                print("\n--- Найденные контакты ---")
                for contact in results:
                    print(f"ID: {contact[0]}, Имя: {contact[1]}, Телефон: {contact[2]}, Email: {contact[3]}")
            else:
                print("Контакты не найдены.")

        elif choice == "4":
            contact_id = input("Введите ID контакта для удаления: ")
            if contact_id.isdigit():
                delete_contact(int(contact_id), DB_PATH)
            else:
                print("Ошибка: ID должен быть числом.")

        elif choice == "5":
            print("Выход из программы...")
            break

        else:
            print("Ошибка: неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()
