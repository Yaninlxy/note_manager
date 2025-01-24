import sqlite3

def create_connection(db_path):
    """
    Создает соединение с базой данных SQLite.
    
    :param db_path: путь к файлу базы данных
    :return: объект соединения SQLite или None в случае ошибки
    """
    try:
        conn = sqlite3.connect(db_path)
        print(f"Подключение к базе данных SQLite: {db_path} успешно установлено.")
        return conn
    except sqlite3.Error as e:
        print(f"Ошибка при подключении к базе данных SQLite: {e}")
        return None
