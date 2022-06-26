from flask import Flask, jsonify
from less_14_h_w.part_2.utils import get_films_range

app = Flask(__name__)  # создаем экземпляр класса


@app.route('/movie/<int:year_start>/to/<int:year_end>')
def json_page_films_from_range(year_start, year_end):
    """Вывод всех результатов  в формате json PART_2 -
    поиск фильмов находящихся в диапазоне дат"""
    data = get_films_range(year_start, year_end)
    return jsonify(data)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Страница не найдена</h1><p>Поищите другую!</p>", 404


if __name__ == '__main__':
    app.run()