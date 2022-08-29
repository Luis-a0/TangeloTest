import sqlite3

DB_NAME = "country.db"

def get_db():
    """
    Función encargada de realizar la conexión de la base de datos.
    Returns:
        -  conn:  | conexión a la base de datos
    """
    conn = sqlite3.connect(DB_NAME)
    return conn

def create_tables():
    """
    Función encargada de crear la tabla country_stat en la base de datos
    Args:
        - data: JSON| información sin procesar
    Returns:
        -  : dict | información procesada
    """
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

def insert_values(list_values):
    """
    Función encargada agregar registros a la base de datos
    Args:
        - list_values: list| Lista de valores a insertar
    Returns:
        -  : bool | ejecución exitosa
    """
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO country_stat(min, mean, max, total) values (?, ?, ?, ?)"
    cursor.execute(statement, list_values)
    db.commit()
    db.close()

    return True

def create_record(list_values):
    """
    Función encargada de servir de conexion con la función principal
    Args:
        - list_values: list| Lista de valores a insertar
    """
    create_tables()
    insert_values(list_values)