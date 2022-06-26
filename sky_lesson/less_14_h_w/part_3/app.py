from flask import Flask, jsonify

from less_14_h_w.part_3.utils import get_films_in_rating

app = Flask(__name__)  # создаем экземпляр класса


@app.route('/movie/<rating>')
def json_page_films(rating):
    """Вывод всех результатов  в формате json PART_3 -
    фильмы содержащие определенный рейтинг"""
    data = get_films_in_rating(rating)
    return jsonify(data)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>СтраниWWWWца не найдена</h1><p>Поищите другую!</p>", 404


if __name__ == '__main__':
    app.run()