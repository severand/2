from flask import Blueprint, request, render_template

from lesson12_home_work.main.utils import add_new_post, is_filename_allowed, add_new_pictures

loader_blueprint = Blueprint('loader_', __name__, template_folder='templates')


@loader_blueprint.route("/upload", methods=["GET", "POST"])
def page_post_form():
    """Добавить новый пост"""
    if request.method == 'POST':
        pic = request.files.get("pic")  # Получаем объект картинки из формы
        content = request.form['content']  # Получаем текст из формы

        if len(content) > 0 and pic:  # если есть контент и картинка
            filename = pic.filename  # Получаем имя файла у загруженного файла
            check = is_filename_allowed(filename)  # Проверяем расширение файла

            if check:
                add_new_pictures(pic)  # Сохраняем картинку в директорию
                add_new_post(filename, content)  # сохраняем пост - вызываем функцию

            return render_template('post_uploaded.html', check=check, filename=filename, pic=pic, content=content)
    return render_template('post_form.html')