# coding=utf8
# from pprint import pprint as pp

import json


# класс по работе с пользователем
class UserDAO:

    def __init__(self, path):
        self.path = path

    def load_data(self):
        """Получает данные пользователей"""
        try:
            with open(self.path, "r", encoding='UTF-8-sig') as file:
                list_users = json.load(file)
                return list_users
        except FileNotFoundError:
            raise "Файл не найден"
        except JSONDecodeError:
            raise "Не удается преобразовать в формат JSON"

    def get_all_posts(self):
        """Возвращает список всех постов пользователей"""
        users = self.load_data()
        return users

    def get_user_by_id(self, pk):
        """Возвращает данные поста по id"""
        for user in self.load_data():
            if user["pk"] == pk:
                return user

# item_dao = UserDAO(path)
# pp(item_dao.get_all_posts_from_teg('лю'))