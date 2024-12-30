#add_titles_loop.py
def add_titles():
    titles = []
    while True:
        title = input("Введите заголовок (или оставьте пустым для завершения): ").strip()
        if not title:
            break
        if title not in titles:  # Проверка на уникальность
            titles.append(title)
        else:
            print("Этот заголовок уже добавлен.")
    print("\nЗаголовки заметки:\n")
    for t in titles:
        print(f"- {t}")

if __name__ == "__main__":
    add_titles()

#update_status.py
def update_status():
    statuses = ["выполнено", "в процессе", "отложено"]
    current_status = "в процессе"
    print(f"Текущий статус заметки: \"{current_status}\"\n")
    print("Выберите новый статус заметки:")
    for i, status in enumerate(statuses, 1):
        print(f"{i}. {status}")
    
    choice = input("\nВаш выбор (число или название статуса): ").strip().lower()
    
    # Проверяем выбор пользователя
    if choice.isdigit():  # Выбор числом
        choice_num = int(choice)
        if 1 <= choice_num <= len(statuses):
            current_status = statuses[choice_num - 1]
            print(f"Статус заметки успешно обновлён на: \"{current_status}\"")
        else:
            print("Некорректный выбор числа.")
    elif choice in statuses:  # Выбор текстом
        current_status = choice
        print(f"Статус заметки успешно обновлён на: \"{current_status}\"")
    else:
        print("Некорректный ввод. Попробуйте снова.")
        
if __name__ == "__main__":
    update_status()

#check_deadline.py
from datetime import datetime

def check_deadline():
    today = datetime.now().strftime("%d-%m-%Y")
    print(f"Текущая дата: {today}\n")
    try:
        deadline = input("Введите дату дедлайна (в формате день-месяц-год): ").strip()
        deadline_date = datetime.strptime(deadline, "%d-%m-%Y")
        today_date = datetime.strptime(today, "%d-%m-%Y")
        delta = (deadline_date - today_date).days
        if delta < 0:
            print(f"Внимание! Дедлайн истёк {-delta} дней назад.")
        elif delta == 0:
            print("Дедлайн сегодня!")
        else:
            print(f"До дедлайна осталось {delta} дней.")
    except ValueError:
        print("Некорректный формат даты. Используйте день-месяц-год.")

if __name__ == "__main__":
    check_deadline()

#multiple_notes.py
def add_notes():
    notes = []
    while True:
        print("\nДобро пожаловать в 'Менеджер заметок'! Вы можете добавить новую заметку.")
        user = input("Введите имя пользователя: ").strip()
        title = input("Введите заголовок заметки: ").strip()
        description = input("Введите описание заметки: ").strip()
        status = input("Введите статус заметки (новая, в процессе, выполнено): ").strip()
        created_date = input("Введите дату создания (день-месяц-год): ").strip()
        deadline = input("Введите дедлайн (день-месяц-год): ").strip()
        
        notes.append({
            "Имя": user,
            "Заголовок": title,
            "Описание": description,
            "Статус": status,
            "Дата создания": created_date,
            "Дедлайн": deadline,
        })
        
        more = input("Хотите добавить ещё одну заметку? (да/нет): ").strip().lower()
        if more != "да":
            break

    print("\nСписок заметок:")
    for i, note in enumerate(notes, 1):
        print(f"\n{i}. Имя: {note['Имя']}\n   Заголовок: {note['Заголовок']}\n   Описание: {note['Описание']}\n   Статус: {note['Статус']}\n   Дата создания: {note['Дата создания']}\n   Дедлайн: {note['Дедлайн']}")

if __name__ == "__main__":
    add_notes()

#delete_note.py
def delete_note():
    notes = [
        {"Имя": "Алексей", "Заголовок": "Список покупок", "Описание": "Купить продукты на неделю"},
        {"Имя": "Мария", "Заголовок": "Учеба", "Описание": "Подготовиться к экзамену"},
    ]
    
    print("\nТекущие заметки:")
    for i, note in enumerate(notes, 1):
        print(f"\n{i}. Имя: {note['Имя']}\n   Заголовок: {note['Заголовок']}\n   Описание: {note['Описание']}")
    
    to_delete = input("\nВведите имя пользователя или заголовок для удаления заметки: ").strip()
    initial_length = len(notes)
    notes = [note for note in notes if note['Имя'] != to_delete and note['Заголовок'] != to_delete]
    
    if len(notes) < initial_length:
        print("\nУспешно удалено. Остались следующие заметки:")
        for i, note in enumerate(notes, 1):
            print(f"\n{i}. Имя: {note['Имя']}\n   Заголовок: {note['Заголовок']}\n   Описание: {note['Описание']}")
    else:
        print("\nЗаметка не найдена.")

if __name__ == "__main__":
    delete_note()
