#Функция для отображения текущего статуса заметки
def display_current_status(note):
       print(f'Текущий статус заметки: "{note["status"]}"')

#Функция для запроса нового статуса у пользователя с проверкой корректности.
def get_new_status():
    allowed_statuses = ["выполнено", "в процессе", "отложено", "до следующего года"]
    
    print("\nВыберите новый статус заметки:")
    for index, status in enumerate(allowed_statuses, start=1):
        print(f"{index}. {status}")
    
    while True:
        choice = input("Ваш выбор (введите номер или статус): ").strip()
        
        # Проверяем, является ли введенный выбор числом
        if choice.isdigit():
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(allowed_statuses):
                return allowed_statuses[choice_index]
            else:
                print("Некорректный номер. Пожалуйста, выберите из предложенных вариантов.")
        elif choice in allowed_statuses:
            return choice
        else:
            print("Некорректный ввод. Пожалуйста, введите номер или один из доступных статусов.")


def main():
    # Инициализация заметки с текущим статусом
    note = {
        "title": "Заметка 1",
        "status": "в процессе"  # Статус по умолчанию
    }
    
    # Отображаем текущий статус заметки
    display_current_status(note)

    # Запрашиваем у пользователя новый статус
    new_status = get_new_status()
    
    # Обновляем статус заметки
    note["status"] = new_status

    # Выводим обновленный статус
    print(f"\nСтатус заметки успешно обновлён на: \"{note['status']}\"")


# Запуск программы
if __name__ == "__main__":
    main()
