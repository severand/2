# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

from dao.model.models import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all_movies(self):
        """Получить все фильмы """
        return self.session.query(Movie).all()

    def get_movie_by_id(self, id):
        """Получить фильм по id"""
        return self.session.query(Movie).filter(Movie.id == id).one()

    def get_movie_by_director_id(self, director_id):
        """Получить все фильмы режиссера"""
        return self.session.query(Movie).filter(Movie.director_id == director_id).all()

    def get_movie_by_genre_id(self, genre_id):
        """Получить все фильмы жанра"""
        return self.session.query(Movie).filter(Movie.genre_id == genre_id).all()

    def get_movie_by_year(self, year):
        """Получить все фильмы за год"""
        return self.session.query(Movie).filter(Movie.year == year).all()

    def get_movie_by_many_filter(self, **kwargs):
        """Универсальная функция"""
        return self.session.query(Movie).filter_by(
            **{key: value for key, value in kwargs.items() if value is not None}
        ).all()

    def create(self, **kwargs) -> bool:
        """Создать новый фильм"""
        try:
            self.session.add(
                Movie(
                    **kwargs
                )
            )
            self.session.commit()
            return True
        except Exception as e:
            print(f'Не удалось добавить новый фильм\n{e}')
            self.session.rollback()
            return False

    def update(self, id, **kwargs):
        """Изменить данные о фильме"""
        try:
            self.session.query(Movie).filter(Movie.id == id).update(**kwargs)
            self.session.commit()

        except Exception as e:
            print(f'Не удалось изменить данные\n{e}')
            self.session.rollback()

    def delete(self, id):
        """Удалить фильм по id"""
        try:
            self.session.query(Movie).filter(Movie.id == id).delete()
            self.session.commit()

        except Exception as e:
            print(f'Не удалось удалить фильм\n{e}')
            self.session.rollback()