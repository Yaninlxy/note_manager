def collect_note_titles():
    notes = {}  # Словарь для хранения заголовков и их статусов
    while True:
        title = input("Введите заголовок заметки (или 'стоп' для завершения): ")
        if title.lower() == 'стоп' or title == '':
            break
        if title.strip():  # Проверяем, что заголовок не пустой
            if title not in notes:  # Проверка на уникальность
                notes[title] = "Не выполнено"  # Устанавливаем статус по умолчанию
            else:
                print("Этот заголовок уже добавлен. Пожалуйста, введите другой.")
    return notes

def change_note_status(notes):
    while True:
        title = input("Введите заголовок заметки для изменения статуса (или 'стоп' для завершения): ")
        if title.lower() == 'стоп' or title == '':
            break
        if title in notes:
            new_status = input("Введите новый статус (например, 'Выполнено' или 'Не выполнено'): ")
            notes[title] = new_status  # Обновляем статус заметки
        else:
            print("Такой заголовок не найден.")

# Вызов функции для сбора заголовков и вывод их со статусами
note_titles = collect_note_titles()
print("\nДобавленные заголовки заметок и их статусы:")
for title, status in note_titles.items():
    print(f"{title}: {status}")

# Изменение статусов заметок
change_note_status(note_titles)

# Вывод обновленных заголовков и статусов
print("\nОбновленные заголовки заметок и их статусы:")
for title, status in note_titles.items():
    print(f"{title}: {status}")
