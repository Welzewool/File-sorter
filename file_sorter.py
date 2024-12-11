"""Код для сортировки файлов по папкам"""
import time
from shutil import move
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from src.file_category import get_file_category
from src.extensions import file_extensions


home_directory = Path.home()  # Путь к домашнему каталогу
# подкаталоги относительно домашней папки
download_path = home_directory / "Загрузки"

images_path = home_directory / "Изображения"
music_path = home_directory / "Музыка"
video_path = home_directory / "Видео"
documents_path = home_directory / "Документы"

destinations = {
"image": images_path,
"audio": music_path,
"video": video_path,
"documents": documents_path,
}

# disk_usage_download = disk_usage(file_path_download)

def sort_files(file_path: Path):
    """
    Перемещает файлы в соответствующие папки на основе их категории.
    """
    category = get_file_category(file_path.name, file_extensions)
    if category and category in destinations:
        destination_path = destinations[category]
        destination_path.mkdir(parents=True, exist_ok=True)
        try:
            move(str(file_path), str(destination_path / file_path.name))
            print(f"Файл {file_path.name} перемещён в {destination_path}")
        except Exception as e:
            print(f"Ошибка при перемещении файла {file_path.name}: {e}")
    else:
        print(f"Файл {file_path.name} оставлен в {download_path}: расширение не определено")


class FileHandler(FileSystemEventHandler):
    """
    Класс для обработки файловых событий в папке.
    """
    def on_created(self, event):
        """
        Отслеживает появление нового файла.
        Проверяет, что это файл, а не папка, и вызывает функцию сортировки
        """
        if not event.is_directory:
            file_path = Path(event.src_path)
            sort_files(file_path)


if __name__ == '__main__':
    event_handler = FileHandler()  # Обработчик событий
    observer = Observer()  # Объект событий, следит за папкой
    observer.schedule(event_handler, str(download_path), recursive=False)  # Запуск обработчика событий

    try:
        print(f"Наблюдение за папкой {download_path} запущено...")
        observer.start()
        while True:
            time.sleep(1.5)
    except KeyboardInterrupt:
        print("Остановка скрипта")
        observer.stop()
    observer.join()  #
