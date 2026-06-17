from src.shared.constants import DATA_FOLDER

from pathlib import Path
from PySide6.QtSql import QSqlDatabase, QSqlQuery

def create_connection(conn_name=None):
    db = QSqlDatabase.addDatabase("QSQLITE", conn_name)
    db.setDatabaseName(str(Path(DATA_FOLDER) / "music_player.db"))
    
    if not db.open():
        raise RuntimeError(f"Database error: {db.lastError().text()}")
    
    return db

def cleanup_connection(conn_name):
    if QSqlDatabase.contains(conn_name):
        QSqlDatabase.removeDatabase(conn_name)

def create_tables(db):
    with open(Path(__file__).parent / "schema.sql", "r") as f:
        schema = f.read()
    query = QSqlQuery(db)
    query.exec(schema)