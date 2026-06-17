from abc import ABC, abstractmethod
from PySide6.QtCore import QObject, Signal

class PySideABCMeta(type(QObject), type(ABC)):
    pass

class BaseWorker(QObject, ABC, metaclass=PySideABCMeta):
    finished = Signal(object)
    error = Signal(str)

    def __init__(self, parent = None):
        super().__init__(parent)

    def safe_execute(self):
        try:
            result = self._execute()
            self.finished.emit(result)
        except Exception as e:
            self.error.emit(str(e))
    
    @abstractmethod
    def _execute(self):
        pass