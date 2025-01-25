from dbm import sqlite3
from db_connection import create_connection

def create_table(db_path):
    """
    Создает таблицу `notes` в базе данных SQLite.
    
    :param db_path: путь к базе данных SQLite
    """
    conn = create_connection(db_path)
    if conn is None:
        print("Ошибка: не удалось установить соединение с базой данных.")
        return

    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                status TEXT NOT NULL,
                created_date TEXT NOT NULL,
                issue_date TEXT NOT NULL
            );
        """)
        conn.commit()
        print("Таблица `notes` успешно создана.")
    except sqlite3.Error as e:
        print(f"Ошибка при создании таблицы `notes`: {e}")
    finally:
        conn.close()


def save_note_to_db(note, db_path):
    """
    Сохраняет заметку в базу данных SQLite.
    
    :param note: словарь с данными заметки
    :param db_path: путь к базе данных SQLite
    """
    conn = create_connection(db_path)
    if conn is None:
        print("Ошибка: не удалось установить соединение с базой данных.")
        return

    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO notes (username, title, content, status, created_date, issue_date)
            VALUES (?, ?, ?, ?, ?, ?);
        """, (note['username'], note['title'], note['content'], note['status'], note['created_date'], note['issue_date']))
        conn.commit()
        print("Заметка успешно сохранена в базу данных.")
    except sqlite3.Error as e:
        print(f"Ошибка при сохранении заметки в базу данных: {e}")
    finally:
        conn.close()


def load_notes_from_db(db_path):
    """
    Загружает все заметки из базы данных SQLite.
    
    :param db_path: путь к базе данных SQLite
    :return: список заметок в виде словарей
    """
    conn = create_connection(db_path)
    if conn is None:
        print("Ошибка: не удалось установить соединение с базой данных.")
        return []

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM notes;")
        rows = cursor.fetchall()
        notes = [
            {
                'id': row[0],
                'username': row[1],
                'title': row[2],
                'content': row[3],
                'status': row[4],
                'created_date': row[5],
                'issue_date': row[6],
            }
            for row in rows
        ]
        return notes
    except sqlite3.Error as e:
        print(f"Ошибка при загрузке заметок из базы данных: {e}")
        return []
    finally:
        conn.close()


def update_note_in_db(note_id, updates, db_path):
    """
    Обновляет указанную заметку в базе данных.
    
    :param note_id: ID заметки для обновления
    :param updates: словарь с обновленными полями
    :param db_path: путь к базе данных SQLite
    """
    conn = create_connection(db_path)
    if conn is None:
        print("Ошибка: не удалось установить соединение с базой данных.")
        return

    try:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE notes
            SET title = ?, content = ?, status = ?, issue_date = ?
            WHERE id = ?;
        """, (updates['title'], updates['content'], updates['status'], updates['issue_date'], note_id))
        conn.commit()
        print(f"Заметка с ID {note_id} успешно обновлена.")
    except sqlite3.Error as e:
        print(f"Ошибка при обновлении заметки в базе данных: {e}")
    finally:
        conn.close()


def delete_note_from_db(note_id, db_path):
    """
    Удаляет заметку из базы данных по её ID.
    
    :param note_id: ID заметки для удаления
    :param db_path: путь к базе данных SQLite
    """
    conn = create_connection(db_path)
    if conn is None:
        print("Ошибка: не удалось установить соединение с базой данных.")
        return

    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM notes WHERE id = ?;", (note_id,))
        conn.commit()
        print(f"Заметка с ID {note_id} успешно удалена.")
    except sqlite3.Error as e:
        print(f"Ошибка при удалении заметки из базы данных: {e}")
    finally:
        conn.close()

def search_notes_by_keyword(keyword, db_path):
    """
    Ищет заметки, где ключевое слово встречается в title или content.
    
    :param keyword: ключевое слово для поиска
    :param db_path: путь к базе данных SQLite
    :return: список заметок в виде словарей
    """
    conn = create_connection(db_path)
    if conn is None:
        print("Ошибка: не удалось установить соединение с базой данных.")
        return []

    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM notes
            WHERE title LIKE ? OR content LIKE ?;
        """, (f"%{keyword}%", f"%{keyword}%"))
        rows = cursor.fetchall()
        return [
            {
                'id': row[0],
                'username': row[1],
                'title': row[2],
                'content': row[3],
                'status': row[4],
                'created_date': row[5],
                'issue_date': row[6],
            }
            for row in rows
        ]
    except sqlite3.Error as e:
        print(f"Ошибка при поиске заметок: {e}")
        return []
    finally:
        conn.close()

def filter_notes_by_status(status, db_path):
    """
    Возвращает заметки с указанным статусом.
    
    :param status: статус для фильтрации
    :param db_path: путь к базе данных SQLite
    :return: список заметок в виде словарей
    """
    conn = create_connection(db_path)
    if conn is None:
        print("Ошибка: не удалось установить соединение с базой данных.")
        return []

    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM notes WHERE status = ?;
        """, (status,))
        rows = cursor.fetchall()
        return [
            {
                'id': row[0],
                'username': row[1],
                'title': row[2],
                'content': row[3],
                'status': row[4],
                'created_date': row[5],
                'issue_date': row[6],
            }
            for row in rows
        ]
    except sqlite3.Error as e:
        print(f"Ошибка при фильтрации заметок: {e}")
        return []
    finally:
        conn.close()