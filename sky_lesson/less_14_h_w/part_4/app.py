from flask import Flask, jsonify

from less_14_h_w.part_4.utils import get_films_by_genre

app = Flask(__name__)  # создаем экземпляр класса


@app.route('/genre/<genre>')
def json_page_films(genre):
    """Вывод всех результатов  в формате json PART_4 -
    фильмы определенного жанра"""
    data = get_films_by_genre(genre)
    return jsonify(data)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Страница не найдена</h1><p>Поищите другую!</p>", 404


if __name__ == '__main__':
    app.run()