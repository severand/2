from flask import Flask, redirect, request, render_template, send_from_directory, url_for
import logging

logging.basicConfig(level=logging.INFO)

from functions import get_post, dict_file_from_form, is_filename_allowed

from lesson12_home_work.main.views import view_foto_blueprint
from lesson12_home_work.loader.views import loader_foto_blueprint

POST_PATH = "posts.json"


app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024  # Ограничиваем размер файла здесь

app.config['JSON_AS_ASCII'] = False  # Чтобы заработала кириллица

app.register_blueprint(view_foto_blueprint)  # Регистрируем блюпринт

app.register_blueprint(loader_foto_blueprint)  # Регистрируем блюпринт


@app.route("/")
def page_index():
    """Вывод формы на главной странице"""
    return render_template('index.html')


@app.route('/search/')
def search_page():
    """Поиск постов по запросу"""
    s = request.args['s']
    if len(s) > 0:
        list_post = get_post(s)  # запуск фнкции - поиск по ключевому слову
        return render_template('post_list.html', list_post=list_post, s=s)
    return redirect(url_for('.page_index'))


UPLOAD_FOLDER = './uploads/images/'  # файл для сохранения изображения


@app.route("/upload", methods=["GET", "POST"])
def page_post_form():
    """Добавить новый пост"""
    if request.method == 'POST':
        pic = request.files.get("pic")  # Получаем объект картинки из формы
        content = request.form['content']  # Получаем текст из формы

        if len(content) > 0 and pic:  # если есть контент и картинка
            filename = pic.filename  # Получаем имя файла у загруженного файла

            check = is_filename_allowed(filename)  # Проверяем расширение файла

            if check:
                pic.save(f"{UPLOAD_FOLDER} {filename}")  # Сохраняем картинку под родным именем
                dict_file_from_form(filename, content)  # сохраняем пост - вызываем функцию

            return render_template('post_uploaded.html', check=check, filename=filename, pic=pic, content=content)
    return render_template('post_form.html')


@app.route("/uploads/<path:path>")
def static_dir(path):
    """Сохранить пост"""
    return send_from_directory("uploads", path)


@app.errorhandler(404)
def file_not_found(filename):
    check_ext = is_filename_allowed(filename)
    if check_ext:
        return "Ок"
    return "<h1>Страница не найдена</h1><p>Поищите другую!</p>"


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Страница не найдена</h1><p>Поищите другую!</p>", 404


@app.errorhandler(413)
def page_not_found(e):
    return "<h1>Ваш файл превышает 2 Мб</h1><p>Поищите поменьше, плиз!</p>", 413


if __name__ == "__main__":
    app.run()