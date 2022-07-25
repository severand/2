from dao.model.models import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all_genres(self):
        """Получить все жанры"""
        return self.session.query(Genre).all()

    def get_genry_by_id(self, id):
        """Получить жанр по id"""
        return self.session.query(Genre).filter(Genre.id == id).one()