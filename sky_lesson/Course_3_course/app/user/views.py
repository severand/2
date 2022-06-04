# coding=utf8
from flask import Blueprint, render_template
from Course_3_course.config import config

user_blueprint = Blueprint('user_blueprint', __name__, template_folder='templates')


@user_blueprint.route('/users/<user_name>')
def user_posts(user_name):
    """Вывод постов пользователя"""
    user_posts = config.post_dao.get_posts_user(user_name)
    return render_template("user-feed.html", user_posts=user_posts)