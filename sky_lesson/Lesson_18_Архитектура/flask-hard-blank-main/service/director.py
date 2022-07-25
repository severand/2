from typing import List

from dao.model.models import Director
from dao.director import DirectorDAO


class DirectorService:

    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_directors(self) -> List[Director]:
        return self.director_dao.get_all_directors()

    def get_director_by_id(self, id):
        return self.director_dao.get_director_by_id(id)