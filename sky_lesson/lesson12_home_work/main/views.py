from flask import Blueprint
from flask import redirect, request, render_template, url_for

from lesson12_home_work.main.utils import get_post

main_blueprint = Blueprint('view_foto_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def page_index():
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_page():
    s = request.values.get("s", None)
    if len(s) > 0:
        list_post = get_post(s)  # запуск фнкции - поиск по ключевому слову
        return render_template('post_list.html', list_post=list_post, s=s)
    return redirect(url_for('.page_index'))  # возврат на главную страницу