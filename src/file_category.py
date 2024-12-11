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
