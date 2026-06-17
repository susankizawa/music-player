from src.shared.singleton import SingletonMeta
from src.shared.constants import PATHS, DEFAULT_CONFIG

import json

class ConfigManager(metaclass=SingletonMeta):
    def __init__(self):
        self.config_path = PATHS.get("config")

        self.config = self.load()
        
    
    def load(self):
        self.config_path.parent.mkdir(parents=True, exist_ok=True)

        if not self.config_path.exists():
            return DEFAULT_CONFIG.copy()
        
        saved_config = json.loads(self.config_path.read_text())

        config = DEFAULT_CONFIG.copy()
        config.update(saved_config)

        return config
    
    def save(self):
        self.config_path.parent.mkdir(parents=True, exist_ok=True)

        with open(self.config_path, "w") as f:
            json.dump(self.config, f, indent=2)
    
    def save_default(self):
        self.config = DEFAULT_CONFIG.copy()
        self.save()

    def update(self, data):
        self.config.update(data)