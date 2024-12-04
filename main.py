"""Код для сортировки файлов по папкам"""
# import os
# import shutil
from os import listdir, makedirs
from os.path import isfile, join
from shutil import move

from src.extensions import file_extensions


file_path_download = "/home/dima/Загрузки"

destinations = {
"image": "/home/dima/Изображения",
"audio": "/home/dima/Музыка",
"video": "/home/dima/Видео",
"documents": "/home/dima/Документы",
}


# Получение списка файлов
files_in_path = [file for file in listdir(file_path_download) if isfile(join(file_path_download, file))]
if not files_in_path:
    print("Каталог пуст")
else:
    print(f"Каталог содержит {len(files_in_path)} файла(-ов), \nфайлы: {files_in_path}")


# disk_usage_download = disk_usage(file_path_download)

def get_file_category(filename: str, extensions_dict: dict[str, str]) -> [str, None]:
    """
    Функция принимает имя файла и словарь с расширениями, определяя к какой категории файл относится.
    Если расширение не найден, то файл остается в исходной папке.
    :param filename:
    :param extensions_dict:
    :return:
    """
    extension = filename.split(".")[-1].lower()  # Получение расширения файла
    for category, extensions in extensions_dict.items():
        if extension in extensions:
            return category
    return None


def sort_files(files: list[str], source_path: str, destinations_path: dict[str, str], extensions_dict: dict[str, str]):
    """
    Функция определяет категорию каждого файла, перемешает его в соответсвующую папку
    :param files:
    :param source_path:
    :param destinations_path:
    :param extensions_dict:
    :return:
    """
    for file in files:
        category = get_file_category(file, extensions_dict)
        if category and category in destinations_path:
            destination_path = destinations[category]
            makedirs(destination_path, exist_ok=True)  # создает папку, если её нет
            try:
                move(join(source_path, file), join(destination_path, file))     # перемещает файл
                print(f"Файл {file} был перемещен в папку {destination_path}")
            except Exception as e:
                print(f"Ошибка при перемещении файла: {e}")
        else:
            print(f"Файл {file} оставлен в {source_path}, не определено расширение файла")


if __name__ == '__main__':
    sort_files(files_in_path, file_path_download, destinations, file_extensions)

