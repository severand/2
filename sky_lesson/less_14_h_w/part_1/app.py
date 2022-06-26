from flask import Flask, jsonify
from less_14_h_w.part_1.utils import get_data_all_project

app = Flask(__name__)  # создаем экземпляр класса


@app.route('/movie/<title>')
def page(title):
    """Вывод поиск по названию фильма PART_1"""
    data = get_data_all_project(title)
    return jsonify(data)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Страниssца не найдена</h1><p>Поищите другую!</p>", 404


if __name__ == '__main__':
    app.run()