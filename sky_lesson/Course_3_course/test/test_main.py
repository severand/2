# coding=utf8
import pytest
from Course_3_course.app.user.dao.user_dao import UserDAO

path = "../data/data.json"


@pytest.fixture()
def user_dao():
    user_dao_instance = UserDAO(path)
    return user_dao_instance


keys_for_main = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}


class TestMain:

    def test_api_get_all(self, user_dao):
        main = user_dao.get_all_posts()
        assert type(main) == list, "возвращается не список"
        assert set(main[0].keys()) == keys_for_main, "неверный список ключей"