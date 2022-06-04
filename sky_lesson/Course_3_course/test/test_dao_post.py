# coding=utf8
import pytest
from Course_3_course.app.post.dao.dao_post import PostDAO

path = "../data/comments.json"

#  список ключей которые долны получить
keys_should_be = {'commenter_name', 'pk', 'comment', 'post_id'}


@pytest.fixture()
def post_dao():
    post_dao_instance = PostDAO(path)
    return post_dao_instance


class TestPostDao:

    def test_load_data_(self, post_dao):
        """проверка на Получает данные """
        comments = post_dao.load_data_()
        assert type(comments) == list, "возвращает не список "
        assert len(comments) > 0, "возвращается пустой список"
        assert set(comments[0].keys()) == keys_should_be, "неверный список ключей"