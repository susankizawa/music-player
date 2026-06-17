from PySide6.QtCore import QThread

class BackgroundTaskBuilder:
    def __init__(self):
        self._worker = None
        self._success_func = None
        self._error_func = None
    
    def use_worker(self, worker):
        self._worker = worker
        return self
    
    def on_success(self, func):
        self._success_func = func
        return self
    
    def on_error(self, func):
        self._error_func = func
        return self
    
    def execute(self, parent=None):
        if not self._worker:
            raise ValueError("Builder requires a worker instance before execution.")

        thread = QThread(parent)

        self._worker.moveToThread(thread)

        thread.started.connect(self._worker.safe_execute)

        self._worker.finished.connect(thread.quit)
        self._worker.error.connect(thread.quit)
        
        thread.finished.connect(self._worker.deleteLater)
        thread.finished.connect(thread.deleteLater)

        if self._success_func:
            self._worker.finished.connect(self._success_func)
        if self._error_func:
            self._worker.error.connect(self._error_func)

        thread.start()

        return self._worker, thread
