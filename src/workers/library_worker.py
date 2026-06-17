from src.database.sql_db import cleanup_connection, create_connection
from src.workers.base_worker import BaseWorker
from src.repositories.library_repository import LibraryRepository

class LibraryWorker(BaseWorker):
    def __init__(self, action, payload=None):
        super().__init__()
        self.action = action
        self.payload = payload
    
    def _execute(self):
        conn_name = f"worker_{hex(id(self))}"
        db = create_connection(conn_name)
        repository = LibraryRepository(db)

        try:
            match self.action:
                case "get_song":
                    result = repository.get_song(self.payload)
                case "get_all_songs":
                    result = repository.get_all_songs()
                case "add_song":
                    result = repository.add_song(self.payload)
                case "soft_delete_song":
                    result = repository.soft_delete_song(self.payload)
                case _:
                    raise ValueError(f"Unknown worker action: {self.action}")
            return result
        finally:
            del repository
            del db
            cleanup_connection(conn_name)