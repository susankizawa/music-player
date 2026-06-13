from src.shared.constants import DATA_FOLDER

from pathlib import Path
from PySide6.QtSql import QSqlDatabase, QSqlQuery

def create_connection():
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(str(Path(DATA_FOLDER) / "music_player.db"))
    
    if not db.open():
        raise RuntimeError(f"Database error: {db.lastError().text()}")
    
    create_tables()

    return True

def cleanup_connections():
    QSqlDatabase.removeDatabase(QSqlDatabase.defaultConnection)

def create_tables():
    with open(Path(__file__).parent / "schema.sql", "r") as f:
        schema = f.read()
    query = QSqlQuery()
    query.exec(schema)