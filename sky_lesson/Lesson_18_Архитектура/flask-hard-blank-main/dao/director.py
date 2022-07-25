from dao.model.models import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all_directors(self):
        """Получить всех режиссеров"""
        return self.session.query(Director).all()

    def get_director_by_id(self, id):
        """Получить режиссера по id"""
        return self.session.query(Director).filter(Director.id == id).one()