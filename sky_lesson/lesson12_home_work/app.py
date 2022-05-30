from flask import Flask, redirect, request, render_template, send_from_directory, url_for
import logging

logging.basicConfig(level=logging.INFO)

from lesson12_home_work.main.views import main_blueprint

from lesson12_home_work.loader.views import loader_blueprint

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024  # Ограничиваем размер файла здесь
app.config['JSON_AS_ASCII'] = False  # Чтобы заработала кириллица

app.register_blueprint(main_blueprint)  # Регистрируем блюпринт
app.register_blueprint(loader_blueprint)  # Регистрируем блюпринт


@app.route('/uploads/<path:path>')
def statik_dir(path):
    return send_from_directory("uploads", path)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Страница не найдена</h1><p>Поищите другую!</p>", 404


@app.errorhandler(413)
def page_not_found(e):
    return "<h1>Ваш файл превышает 2 Мб</h1><p>Поищите поменьше, плиз!</p>", 413


if __name__ == "__main__":
    app.run(debug=False)