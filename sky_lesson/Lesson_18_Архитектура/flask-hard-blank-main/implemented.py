# файл для создания DAO и сервисов чтобы импортировать их везде

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO

from service.director import DirectorService
from service.movie import MovieService
from service.genre import GenreService

from setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao=movie_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao=genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao=director_dao)