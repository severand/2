# coding=utf8
import pytest
from Course_3_course.app.user.dao.user_dao import UserDAO

path = "../data/data.json"


@pytest.fixture()
def user_dao():
    user_dao_instance = UserDAO(path)
    return user_dao_instance


keys_for_all_users = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}
keys_for_user = {'poster_name', 'pic', 'views_count', 'pk', 'poster_avatar', 'likes_count', 'content'}


class TestUserDAO:

    def test_api_get_all(self, user_dao):
        all_user = user_dao.get_all_posts()
        assert type(all_user) == list, "возвращается не список"
        assert set(all_user[0].keys()) == keys_for_all_users, "неверный список ключей"

    def test_api_get_user(self, user_dao):
        user = user_dao.get_user_by_id(1)
        assert type(user) == dict, "возвращается не словарь"
        assert set(user) == keys_for_user, "неверный список ключей"