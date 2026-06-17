from src.shared.singleton import SingletonMeta
from src.shared.constants import PATHS, DEFAULT_SESSION

import json

class SessionManager(metaclass=SingletonMeta):
    def __init__(self):
        self.session_path = PATHS.get("session")

        self.session = self.load()
    
    def load(self):
        self.session_path.parent.mkdir(parents=True, exist_ok=True)

        if not self.session_path.exists():
            return DEFAULT_SESSION.copy()
        
        saved_session = json.loads(self.session_path.read_text())

        session = DEFAULT_SESSION.copy()
        session.update(saved_session)

        return session
    
    def save(self):
        self.session_path.parent.mkdir(parents=True, exist_ok=True)

        with open(self.session_path, "w") as f:
            json.dump(self.session, f, indent=2)

    def update(self, data):
        self.session.update(data)
    