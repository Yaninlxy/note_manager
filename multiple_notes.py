from datetime import datetime

def create_multiple_notes():
    """
    Создаёт несколько заметок через ввод данных и проверяет состояние дедлайнов.
    """
    notes = []
    print("Добавление новых заметок в менеджер. Оставьте пустым для завершения.")

    while True:
        username = input("Введите имя пользователя: ").strip()
        if not username:
            break
        title = input("Введите заголовок заметки: ").strip()
        content = input("Введите описание заметки: ").strip()
        status = input("Введите статус заметки (новая, в процессе, выполнено): ").strip()
        created_date = input("Введите дату создания (день-месяц-год): ").strip()
        issue_date = input("Введите дедлайн (день-месяц-год): ").strip()

        try:
            issue_datetime = datetime.strptime(issue_date, "%d-%m-%Y")
            current_date = datetime.now()
            delta = (issue_datetime - current_date).days

            if delta < 0:
                print(f"Внимание! Дедлайн истёк {abs(delta)} дней назад.")
            else:
                print(f"До дедлайна осталось {delta} дней.")

            note = {
                "username": username,
                "title": title,
                "content": content,
                "status": status,
                "created_date": created_date,
                "issue_date": issue_date,
            }
            notes.append(note)
            print("Заметка добавлена.")
        except ValueError:
            print("Ошибка: неверный формат даты дедлайна. Заметка не была добавлена.")
    
    print("\nВсе заметки:")
    for idx, note in enumerate(notes, 1):
        print(f"{idx}. {note}")

if __name__ == "__main__":
    create_multiple_notes()
