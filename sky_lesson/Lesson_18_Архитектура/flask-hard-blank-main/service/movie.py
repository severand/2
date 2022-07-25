# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.

# Пример

from typing import List

from dao.model.models import Movie
from dao.movie import MovieDAO


class MovieService:

    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_movies(self) -> List[Movie]:
        return self.movie_dao.get_all_movies()

    def get_movie_by_id(self, id):
        return self.movie_dao.get_movie_by_id(id)

    def get_movie_by(self, **kwargs):
        return self.movie_dao.get_movie_by_many_filter(**kwargs)

    def add_file(self, data) -> None:
        return self.movie_dao.create(**data)

    def update_film(self, data: dict) -> None:
        return self.movie_dao.update(data)

    def delete_film(self, id) -> None:
        return self.movie_dao.delete(id)