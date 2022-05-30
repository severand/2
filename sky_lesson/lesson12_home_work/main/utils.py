import json
import logging

POST_PATH = "../posts.json"
UPLOAD_FOLDER = '../uploads/images/'  # файл для сохранения изображения

logging.basicConfig(level=logging.INFO)


def _load_data(path=POST_PATH):
    """Загружает файл список всех постов"""
    with open(path, "r", encoding='UTF-8-sig') as file:
        data = json.load(file)
    return data


def get_post(key_word):
    """Поиск постов по ключевому слову"""
    list_post = []
    for dict in _load_data():
        if dict['content'].count(key_word.strip()):
            list_post.append(dict)
            logging.info("Поиск выполнен")
    return list_post


def add_new_post(filename, content):
    """Функция создает новый словарь и выгружает в файл"""
    data = _load_data()  # загрузка файла со словарями
    new_dict = dict(zip(["pic", "content"], [filename, content]))  # создаем новый словарь из поста

    with open(POST_PATH, "w", encoding='utf-8-sig') as file:  # открываем файл с новыми постами
        if file:
            data.append(new_dict)  # добавление нового поста в словарь
            json.dump(data, file, indent=4, sort_keys=True, ensure_ascii=False)  # выгрузка и сортировка словаря
        else:
            logging.error("Data not found")


def add_new_pictures(pic):
    """Сохраняет изображение в файл"""
    filename = pic.filename  # Получаем имя файла у загруженного файла
    web_path = f"{UPLOAD_FOLDER}{filename}"  # формируем имя файла
    pic.save(web_path)  # Сохраняем картинку в директорию


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}  # Создаем множество расширений


def is_filename_allowed(filename):
    """Проверяет расширение картинки"""
    extension = filename.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        return True
    logging.info("File not pictures")

# pp(load_new_post(NEW_POST_PATH))