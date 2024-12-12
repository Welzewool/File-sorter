from pathlib import Path
from watchdog.events import FileSystemEventHandler
from src.file_sorter import sort_files


class FileHandler(FileSystemEventHandler):
    """
    Класс для обработки файловых событий в папке.
    """
    def __init__(self, download_path: Path):
        super().__init__()
        self.download_path = download_path

    def on_created(self, event):
        """
        Отслеживает появление нового файла.
        Проверяет, что это файл, а не папка, и вызывает функцию сортировки
        """
        if not event.is_directory:
            file_path = Path(event.src_path)
            sort_files(file_path)
