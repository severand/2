from typing import List

from dao.model.models import Genre
from dao.genre import GenreDAO


class GenreService:

    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_all_genres(self) -> List[Genre]:
        return self.genre_dao.get_all_genres()

    def get_genry_by_id(self, id):
        return self.genre_dao.get_genry_by_id(id)