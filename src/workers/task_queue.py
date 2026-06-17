from src.shared.singleton import SingletonMeta
from src.workers.background_task_builder import BackgroundTaskBuilder

from collections import deque
from PySide6.QtCore import Qt

class TaskQueue(metaclass=SingletonMeta):
    def __init__(self):
        self._queue = deque()
        self._is_running = False
    
    def enqueue(self, worker, success_func=None, error_func=None):
        self._queue.append((worker, success_func, error_func))
        self._process_next()
    
    def _process_next(self):
        if self._is_running or not self._queue:
            return
        
        self._is_running = True
        worker, success_func, error_func = self._queue.popleft()

        builder = (BackgroundTaskBuilder()
                   .use_worker(worker)
                   .on_success(success_func)
                   .on_error(error_func))

        self._worker, self._thread = builder.execute()

        print(f"worker_{hex(id(self._worker))} running on thread {hex(id(self._thread))}")

        self._thread.finished.connect(self._on_task_finished, Qt.SingleShotConnection)
        self._thread.finished.connect(
            lambda: print(f"thread {hex(id(self._thread))} finished")
        )

        self._worker.finished.connect(
            lambda *args: print(f"worker {hex(id(self._worker))} finished")
        )

        self._worker.error.connect(
            lambda e: print(f"worker error: {e}")
        )
    
    def _on_task_finished(self):
        self._is_running = False
        self._worker = None
        self._thread = None
        self._process_next()
        
