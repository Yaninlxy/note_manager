from datetime import datetime

# Получает текущую дату без времени
def get_current_date():
    return datetime.now().date()

# Парсит даты в объект datetime, поддерживая разные форматы
def parse_date(date_str):
    for fmt in ("%d-%m-%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(date_str, fmt).date()  # Возвращаем только дату
        except ValueError:
            continue
    raise ValueError("Неверный формат даты. Используйте 'день-месяц-год' или 'год-месяц-день'.")

# Проверяет дедлайны для всех заметок.
def check_deadlines(issues):
    current_date = get_current_date()
    
    for issue in issues:
        # Преобразуем строку даты в объект date
        issue_date = parse_date(issue['issue_date'])
        days_left = (issue_date - current_date).days
        
        if days_left < 0:
            print(f"Дедлайн заметки '{issue['title']}' истёк!")
        elif days_left == 0:
            print(f"Дедлайн заметки '{issue['title']}' истекает сегодня!")
        else:
            print(f"У вас осталось {days_left} дней до дедлайна заметки '{issue['title']}'.")

def main():
    issues = []
    
    while True:
        title = input("Введите название заметки (или 'выход' для завершения): ")
        if title.lower() == 'выход':
            break
            
        while True:  # Вложенный цикл для повторного запроса даты
            issue_date = input("Введите дедлайн заметки (день-месяц-год или год-месяц-день): ")
            try:
                # Проверяем дату перед добавлением в список
                parsed_date = parse_date(issue_date)
                # Сохраняем дату в строковом формате для дальнейшего использования
                issues.append({'title': title, 'issue_date': issue_date})
                break  # Выходим из внутреннего цикла, если дата корректна
            except ValueError as e:
                print(e)  # Выводим сообщение об ошибке и запрашиваем ввод снова
    
    check_deadlines(issues)

if __name__ == "__main__":
    main()
