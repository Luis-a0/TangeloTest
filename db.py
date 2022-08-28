import sqlite3
from sqlite3.dbapi2 import _Statement

DB_NAME = "country.db"

def get_db():
    conn = sqlite3.connect(DB_NAME)
    return conn

def create_tables():
    table = """
            CREATE TABLE IF NOT EXISTS country_stat(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            min REAL NOT NULL,
            mean REAL NOT NULL,
            max REAL NOT NULL,
            total REAL NOT NULL
        )
        """
    db = get_db()
    cursor = db.cursor()
    cursor.execute(table)

def insert_values(min, mean, max, total):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO country_stat(min, mean, max, total) values (?, ?, ?, ?)"
    cursor.execute(statement, [min, mean, max, total])
    db.commit()

    return True

def create_record(min, mean, max, total):
    create_tables()
    insert_values(min, mean, max, total)