from pathlib import Path
from shutil import move
from src.extensions import file_extensions, destinations
from src.file_categorizer import get_file_category


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
        print(f"Файл {file_path.name} оставлен в папке: расширение не определено")
