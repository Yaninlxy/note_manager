from datetime import datetime

def check_deadline():
    """
    Проверяет, истёк ли дедлайн, и сообщает, сколько дней осталось или прошло, исключая текущий день.
    """
    current_date = datetime.now()
    print(f"Текущая дата: {current_date.strftime('%d-%m-%Y')}")

    deadline_input = input("Введите дату дедлайна (в формате день-месяц-год): ").strip()
    try:
        deadline_date = datetime.strptime(deadline_input, "%d-%m-%Y")
        delta = (deadline_date.date() - current_date.date()).days

        if delta > 0:
            print(f"До дедлайна осталось {delta} дней.")
        elif delta == 0:
            print("Дедлайн сегодня! Успейте завершить работу.")
        else:
            print(f"Дедлайн истёк {abs(delta) - 1} дней назад.")
    except ValueError:
        print("Ошибка: неверный формат даты. Укажите в формате день-месяц-год.")

if __name__ == "__main__":
    check_deadline()
