# coding=utf8
# from pprint import pprint as pp
import json
from Course_3_course.config import config


class PostDAO():

    def __init__(self, path):  # post_all):
        self.path = path

    def data(self):
        data = config.UserDAO(config.USER_PATH).load_data()
        return data

    def load_data_(self):
        """Получает данные """
        try:
            with open(self.path, "r", encoding='UTF-8-sig') as file:
                list_posts = json.load(file)
                return list_posts
        except FileNotFoundError:
            raise "Файл не найден"
        except JSONDecodeError:
            raise "Не удается преобразовать в формат JSON"

    def get_all_comments(self):
        """Возвращает все комменты"""
        return self.load_data_()

    def get_comment_user(self, user_name):
        """Возвращает комменты определенного пользователя"""
        try:
            list_comment_user_name = []
            comments = self.get_all_comments()
            for item in comments:
                if item['commenter_name'] == user_name.strip():
                    list_comment_user_name.append(item["comment"])
            return list_comment_user_name
        except ValueError:
            return f'Пользователя нет!'

    def get_posts_user(self, user_name):
        """Возвращает посты (словари)  определенного пользователя"""
        try:
            list_post_user_name = []
            for item in self.data():
                if item['poster_name'] == user_name.strip():
                    list_post_user_name.append(item)
            return list_post_user_name
        except ValueError:
            return f'Пользователя нет!'

    def get_comments_user_by_id(self, post_id):
        """Возвращает комментарии к посту по post_id"""
        list_comment = []
        for item in self.load_data_():
            if item['post_id'] == post_id:
                list_comment.append(item)
        return list_comment

    def get_posts_by_key_word(self, key_word):
        """Возвращает список постов по ключевому слову"""
        list_post = []
        for dict in self.data():
            if dict['content'].count(key_word.strip()):
                list_post.append(dict)
        return list_post

# path = "../data/comments.json"
# item_dao = PostDAO(path, 'leo')
# pp(item_dao.get_comment_user())