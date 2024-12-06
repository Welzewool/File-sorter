"""Код для сортировки файлов по папкам"""
# import os
# import shutil
# from os import listdir, makedirs
# from os.path import isfile, join
from shutil import move
from pathlib import Path

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

def get_file_category(filename: str, extensions_dict: dict[str, str]) -> [str, None]:
    """
    Определяет категорию файла по его расширению.
    :param filename: Имя файла
    :param extensions_dict: Словарь категорий и расширений
    :return: Категория или None
    """
    extension = filename.split(".")[-1].lower()  # Получение расширения файла
    for category, extensions in extensions_dict.items():
        if extension in extensions:
            return category
    return None


def sort_files(files: list[Path], source_path: Path, destinations_dct: dict[str, Path], extensions_dict: dict[str, str]):
    """
    Перемещает файлы в соответствующие папки на основе их категории.
    :param files: Список файлов
    :param source_path: Путь к исходной папке
    :param destinations_dct: Словарь категорий и путей
    :param extensions_dict: Словарь категорий и расширений
    """
    for file in files:
        category = get_file_category(file.name, extensions_dict)
        if category and category in destinations_dct:
            destination_path = destinations_dct[category]
            destination_path.mkdir(parents=True, exist_ok=True)  # создает папку, если её нет
            try:
                move(str(file), str(destination_path / file.name))     # перемещает файл
                print(f"Файл {file} был перемещен в папку {destination_path}")
            except Exception as e:
                print(f"Ошибка при перемещении файла {file.name}: {e}")
        else:
            print(f"Файл {file.name} оставлен в {source_path}, не определено расширение файла")


if __name__ == '__main__':
    # Получение списка файлов
    files_in_path = [file for file in download_path.iterdir() if file.is_file()]
    if not files_in_path:
        print("Каталог пуст")
    else:
        print(f"Каталог содержит {len(files_in_path)} файла(-ов): {[file.name for file in files_in_path]}")
        sort_files(files_in_path, download_path, destinations, file_extensions)

