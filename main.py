"""Код для сортировки файлов по папкам"""
from os import listdir
from os.path import isfile, join

file_path_download = "/home/dima/Загрузки"

destinations = {
"image": "/home/dima/Изображения",
"audio": "/home/dima/Музыка",
"video": "/home/dima/Видео",
"documents": "/home/dima/Документы",
}


# Получение списка файлов
files_in_path = [file for file in listdir(file_path_download) if isfile(join(file_path_download, file))]
print(files_in_path)

# disk_usage_download = disk_usage(file_path_download)

# Функция для определения категории файла
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













