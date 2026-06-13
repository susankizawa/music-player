from src.shared.singleton import SingletonMeta

class Config(metaclass=SingletonMeta):
    def __init__(self):
        self.volume = 1.0