import sqlite3

def create_connection(db_file):
    """Создание соединения с базой данных SQLite"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Соединение с базой данных установлено.")
        return conn
    except sqlite3.Error as e:
        print(f"Ошибка при подключении к базе данных: {e}")
    return conn


def create_table(conn):
    """Создание таблицы для хранения матчей"""
    try:
        sql_create_matches_table = '''CREATE TABLE IF NOT EXISTS matches (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        home_team TEXT NOT NULL,
                                        away_team TEXT NOT NULL,
                                        home_score INTEGER,
                                        away_score INTEGER,
                                        status TEXT
                                      );'''
        conn.execute(sql_create_matches_table)
        print("Таблица создана успешно.")
    except sqlite3.Error as e:
        print(f"Ошибка при создании таблицы: {e}")

def insert_match(conn, match):
    """Добавление данных о матче в базу данных"""
    sql = '''INSERT INTO matches (home_team, away_team, home_score, away_score, status)
             VALUES (?, ?, ?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, match)
    conn.commit()
    print(f"Матч {match[0]} - {match[1]} добавлен в базу данных.")

def fetch_matches(conn):
    """Получение всех матчей из базы данных"""
    cur = conn.cursor()
    cur.execute("SELECT * FROM matches")
    rows = cur.fetchall()
    return rows
