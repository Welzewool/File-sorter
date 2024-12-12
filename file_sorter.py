"""Код для сортировки файлов по папкам"""
import time
from pathlib import Path
from watchdog.observers import Observer
from src.event_handler import FileHandler


if __name__ == '__main__':
    home_directory = Path.home()
    download_path = home_directory / "Загрузки"

    event_handler = FileHandler(download_path)  # Обработчик событий
    observer = Observer()  # Объект событий, следит за папкой
    observer.schedule(event_handler, str(download_path), recursive=False)  # Настройка обработчика событий

    try:
        print(f"Наблюдение за папкой {download_path} запущено...")
        observer.start()
        while True:
            time.sleep(1.5)
    except KeyboardInterrupt:
        print("Остановка скрипта")
        observer.stop()
    observer.join()
