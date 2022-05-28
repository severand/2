POST_PATH = "posts.json"
import json
import logging

logging.basicConfig(level=logging.INFO)


def _load_data(path=POST_PATH):
	"""Загружает файл - список постов"""
	with open(path, "r", encoding='UTF-8') as file:
		data = json.load(file)
	return data


def get_post(key_word):
	"""Поиск постов по ключевому слову"""
	list_post = []
	for dict in _load_data():
		if len(key_word.title()) != 0 and dict.get("content").count(key_word):
			list_post.append(dict)
			logging.info("Поиск выполнен")
	return list_post


def load_new_post():
	"""Загружает файл - список постов"""
	with open("uploads/posts_new.json", "r", encoding='utf-8-sig') as file:
		# data = file.read()
		data = json.load(file)
		logging.info("Файл загружен - данные получены")
		return data

	# if type(data) is not list:
	# 	logging.info("Файл загружен - данные получены")
	# 	data = json.load(file)
	# 	return data
	# logging.error("Ошибка загрузки файла - данных нет")
	# new_file()


# # 	logging.info("Файл загружен - данные получены")
# # 	print(data[0])
# # if data[0]:
# 	data = json.load(file)
# if not EOFError:
# 	logging.info("Файл загружен - данные получены")
# 	return data
# logging.error("Ошибка загрузки файла - данных нет")
# new_file()
# logging.info("Файл загружен - данные получены")
# return data


# def new_file():
# 	"""Создает словарь в пустом файле"""
# 	new_dict = [dict(zip(["pic", "content"], ["pic","content"]))]
# 	with open("uploads/posts_new.json", "w", encoding='utf-8-sig') as file:
# 		json.dump(new_dict, file, indent=4, sort_keys=True, ensure_ascii=False)
# 		load_new_post()


def dict_file_from_form(filename, content):
	"""Функция создает новый словарь и выгружает в файл"""
	data = load_new_post()  # загрузка файла со словарями
	new_dict = dict(zip(["pic", "content"], [filename, content]))  # создаем новый словарь из поста

	with open("uploads/posts_new.json", "w", encoding='utf-8-sig') as file:  # открываем файл с новыми постами
		if file:
			data.append(new_dict)  # добавление нового словаря в файл
			json.dump(data, file, indent=4, sort_keys=True, ensure_ascii=False)  # выгрузка и сортировка словаря
		logging.error("Словарь не создан")


# 'txt', 'pdf', 'png', 'jpg', 'jpeg' 'gif'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}  # Создаем множество расширений


def is_filename_allowed(filename):
	"""Проверяет расширение картинки"""
	extension = filename.split(".")[-1]
	if extension in ALLOWED_EXTENSIONS:
		return True
	logging.info("Загруженный файл не картинка")