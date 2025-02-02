import sqlite3

def create_connection(db_path):
    """Создает и возвращает соединение с базой данных SQLite."""
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None

def create_table(db_path):
    """Создает таблицу contacts, если она не существует."""
    conn = create_connection(db_path)
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT
            );
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Ошибка при создании таблицы: {e}")
    finally:
        conn.close()

# Проверка работы
if __name__ == "__main__":
    db_path = "contacts.db"
    create_table(db_path)
