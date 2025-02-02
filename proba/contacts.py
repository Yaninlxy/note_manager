import sqlite3
from db import create_connection

def add_contact(name, phone, email, db_path):
    """Добавляет новый контакт в базу данных."""
    conn = create_connection(db_path)
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
        conn.commit()
        print(f"Контакт {name} добавлен.")
    except sqlite3.Error as e:
        print(f"Ошибка при добавлении контакта: {e}")
    finally:
        conn.close()

def get_all_contacts(db_path):
    """Получает все контакты из базы данных."""
    conn = create_connection(db_path)
    if conn is None:
        return []

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contacts")
        contacts = cursor.fetchall()
        return contacts
    except sqlite3.Error as e:
        print(f"Ошибка при получении контактов: {e}")
        return []
    finally:
        conn.close()

def search_contact(keyword, db_path):
    """Ищет контакты по имени или номеру телефона."""
    conn = create_connection(db_path)
    if conn is None:
        return []

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contacts WHERE name LIKE ? OR phone LIKE ?", (f"%{keyword}%", f"%{keyword}%"))
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        print(f"Ошибка при поиске контактов: {e}")
        return []
    finally:
        conn.close()

def delete_contact(contact_id, db_path):
    """
    Удаляет контакт по ID и сбрасывает автоинкремент, если список пуст.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Удаляем контакт
    cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    conn.commit()

    # Проверяем, остались ли контакты
    cursor.execute("SELECT COUNT(*) FROM contacts;")
    count = cursor.fetchone()[0]

    # Если контактов нет, сбрасываем автоинкремент
    if count == 0:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='contacts';")
        conn.commit()

    print(f"Контакт с ID {contact_id} удален.")
    conn.close()


# Проверка работы
if __name__ == "__main__":
    db_path = "contacts.db"

    # Добавление контакта
    add_contact("Алексей", "+79307805559", "Alex@example.com", db_path)

    # Вывод всех контактов
    contacts = get_all_contacts(db_path)
    print("Все контакты:", contacts)

    # Поиск контакта
    found = search_contact("Иван", db_path)
    print("Результаты поиска:", found)

    # Удаление контакта
    if contacts:
        delete_contact(contacts[0][0], db_path)
