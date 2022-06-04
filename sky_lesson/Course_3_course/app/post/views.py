# coding=utf8
from flask import Blueprint, render_template, request
from Course_3_course.config import config

post_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates')


@post_blueprint.route('/post/<int:pk>')
def post(pk):
    """Вывод поста по рк"""
    user_data = config.user_dao.get_user_by_id(pk)
    post_data = config.post_dao.get_comments_user_by_id(pk)
    return render_template("post.html", user=user_data, user_comments=post_data, num=len(post_data))


@post_blueprint.route('/search/')
def search_post():
    """Вывод постов по ключевому слову"""
    key_word = request.values.get('s', None)
    if len(key_word) > 0:
        posts = config.post_dao.get_posts_by_key_word(key_word)
        return render_template("search.html", user_posts=posts, num=len(posts))