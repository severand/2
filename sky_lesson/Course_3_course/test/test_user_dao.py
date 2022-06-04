# coding=utf8
import pytest

from Course_3_course.app.user.dao.user_dao import UserDAO

path = "../data/data.json"


@pytest.fixture()
def user_dao():
    user_dao_instance = UserDAO(path)
    return user_dao_instance


#  список ключей которые долны получить
keys_should_be = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


class TestUserDao:

    def test_load_data(self, user_dao):
        """проверка на вывод всех постов"""
        posts = user_dao.load_data()
        assert type(posts) == list, "возвращает не список "
        assert len(posts) > 0, "возвращается пустой список постов"

    def test_get_user_by_id(self, user_dao):
        """проверка на вывод юзера по PK"""
        user = user_dao.get_user_by_id(2)
        assert (user["pk"] == 2), "возвращается неправильный user"
        assert set(user.keys()) == keys_should_be, "неверный список ключей"