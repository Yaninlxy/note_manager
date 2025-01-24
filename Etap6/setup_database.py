import sqlite3

def create_connection(db_file):
    """ Создает соединение с базой данных SQLite. """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Подключение к базе данных SQLite: {db_file} успешно установлено.")
    except sqlite3.Error as e:
        print(f"Ошибка при подключении к базе данных SQLite: {e}")
    return conn

# Пример использования
if __name__ == '__main__':
    database = 'note_manager.db'  # имя базы данных
    conn = create_connection(database)

import sqlite3

def create_table():
    """ Создает таблицу `notes` в базе данных SQLite. """
    database = 'note_manager.db'
    conn = sqlite3.connect(database)
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
        if conn:
            conn.close()

# Пример использования
if __name__ == '__main__':
    create_table()

import sqlite3

def check_table_exists():
    """ Проверяет существование таблицы `notes` в базе данных. """
    database = 'note_manager.db'
    conn = sqlite3.connect(database)
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='notes';")
        if cursor.fetchone():
            print("Таблица `notes` существует.")
        else:
            print("Таблица `notes` не существует.")
    except sqlite3.Error as e:
        print(f"Ошибка при проверке существования таблицы: {e}")
    finally:
        if conn:
            conn.close()

# Пример использования
if __name__ == '__main__':
    check_table_exists()

import sqlite3

def save_note_to_db(note, db_path):
    """
    Сохраняет заметку в базу данных SQLite.
    
    :param note: словарь с данными заметки (username, title, content, status, created_date, issue_date)
    :param db_path: путь к базе данных SQLite
    """
    try:
        # Подключение к базе данных
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        
        # Выполнение SQL-запроса для вставки данных
        cursor.execute("""
            INSERT INTO notes (username, title, content, status, created_date, issue_date)
            VALUES (?, ?, ?, ?, ?, ?);
        """, (note['username'], note['title'], note['content'], note['status'], note['created_date'], note['issue_date']))
        
        # Сохранение изменений
        connection.commit()
        print("Заметка успешно сохранена в базу данных.")
    
    except sqlite3.Error as e:
        print(f"Ошибка при сохранении заметки в базу данных: {e}")
    
    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    # Путь к базе данных
    db_path = 'note_manager.db'

    # Пример заметки
    note = {
        "username": "Alexey",
        "title": "Пример заметки",
        "content": "Это описание заметки.",
        "status": "В процессе",
        "created_date": "23-01-2025",
        "issue_date": "23-01-2025"
    }
    
    # Сохранение заметки в базу данных
    save_note_to_db(note, db_path)

def get_all_notes(db_path):
    """
    Извлекает все заметки из таблицы `notes`.
    
    :param db_path: путь к базе данных SQLite
    :return: список заметок
    """
    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        
        cursor.execute("SELECT * FROM notes;")
        notes = cursor.fetchall()
        return notes
    
    except sqlite3.Error as e:
        print(f"Ошибка при чтении данных из базы: {e}")
        return []
    
    finally:
        if connection:
            connection.close()

# Проверка
if __name__ == "__main__":
    db_path = 'note_manager.db'
    all_notes = get_all_notes(db_path)
    print("Заметки в базе данных:")
    for note in all_notes:
        print(note)

import sqlite3

def load_notes_from_db(db_path):
    """
    Загружает все заметки из базы данных SQLite.
    
    :param db_path: путь к базе данных SQLite
    :return: список заметок в виде словарей
    """
    try:
        # Подключение к базе данных
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        
        # Выполнение SQL-запроса для получения всех данных из таблицы
        cursor.execute("SELECT * FROM notes;")
        rows = cursor.fetchall()
        
        # Преобразование результата в список словарей
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
        if connection:
            connection.close()

if __name__ == "__main__":
    # Путь к базе данных
    db_path = 'note_manager.db'
    
    # Загрузка заметок из базы данных
    notes = load_notes_from_db(db_path)
    
    if notes:
        print("Загруженные заметки:")
        for note in notes:
            print(note)
    else:
        print("В базе данных нет заметок.")

import sqlite3

def update_note_in_db(note_id, updates, db_path):
    """
    Обновляет указанную заметку в базе данных.
    
    :param note_id: ID заметки для обновления
    :param updates: словарь с обновленными полями ('title', 'content', 'status', 'issue_date')
    :param db_path: путь к базе данных SQLite
    """
    try:
        # Подключение к базе данных
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        # Выполнение SQL-запроса для обновления заметки
        cursor.execute("""
            UPDATE notes
            SET title = ?, content = ?, status = ?, issue_date = ?
            WHERE id = ?;
        """, (updates['title'], updates['content'], updates['status'], updates['issue_date'], note_id))

        # Фиксация изменений
        connection.commit()
        print(f"Заметка с ID {note_id} успешно обновлена.")

    except sqlite3.Error as e:
        print(f"Ошибка при обновлении заметки в базе данных: {e}")
    
    finally:
        if connection:
            connection.close()

import sqlite3

def delete_note_from_db(note_id, db_path):
    """
    Удаляет заметку из базы данных по её ID.
    
    :param note_id: ID заметки для удаления
    :param db_path: путь к базе данных SQLite
    """
    try:
        # Подключение к базе данных
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        # Выполнение SQL-запроса для удаления заметки
        cursor.execute("DELETE FROM notes WHERE id = ?;", (note_id,))

        # Фиксация изменений
        connection.commit()
        print(f"Заметка с ID {note_id} успешно удалена.")

    except sqlite3.Error as e:
        print(f"Ошибка при удалении заметки из базы данных: {e}")
    
    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    # Путь к базе данных
    db_path = 'note_manager.db'

    # Пример данных для обновления
    note_id = 1
    updates = {
        'title': 'Обновленный заголовок',
        'content': 'Обновленное описание заметки',
        'status': 'Завершено',
        'issue_date': '25-01-2025'
    }

    # Обновление заметки
    update_note_in_db(note_id, updates, db_path)

    # Удаление заметки
    delete_note_from_db(note_id, db_path)
