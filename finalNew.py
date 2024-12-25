# Запрашиваем у пользователя информацию о заметке
username = input("Введите имя пользователя: ")
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки: ")
created_date = input("Введите дату создания заметки в формате 'день-месяц-год': ")
issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")

# Запрашиваем заголовки
headings = []
for i in range(3):  # Предлагаем ввести 3 заголовка
    heading = input(f"Введите заголовок {i + 1}: ")
    headings.append(heading)

# Создаем словарь для хранения информации о заметке
note = {
    "username": username,
    "title": title,
    "content": content,
    "status": status,
    "created_date": created_date,
    "issue_date": issue_date,
    "titles": headings  # Список заголовков
}

# Изменяем формат даты для вывода (без года)
temp_created_date = created_date[0:5]  # Получаем "день-месяц"
temp_issue_date = issue_date[0:5]      # Получаем "день-месяц"

# Вывод значений переменных
print("\n--- Информация о заметке ---")
print("Имя пользователя:", note["username"])
print("Заголовок заметки:", note["title"])
print("Описание заметки:", note["content"])
print("Статус заметки:", note["status"])
print("Дата создания заметки (без года):", temp_created_date)
print("Дата истечения заметки (без года):", temp_issue_date)
print("Заголовки заметки:")
for h in note["titles"]:  # Доступ к списку заголовков
    print("-", h)
