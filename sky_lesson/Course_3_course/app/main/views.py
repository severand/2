# coding=utf8
import logging
from Course_3_course.logs import logger
from Course_3_course.config import config
from flask import Blueprint, render_template, jsonify

logger.create_logs()
logger = logging.getLogger("api_logs.txt")

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def page_index():
    """Вывод всех постов - лента"""
    data = config.user_dao.get_all_posts()
    return render_template('index.html', data=data)


@main_blueprint.route('/api/posts/')
def json_page_all_posts():
    """Вывод всех постов в формате json"""
    data = config.user_dao.get_all_posts()
    logger.debug(f"Запрос  {'/api/posts/'}")
    return jsonify(data)


@main_blueprint.route('/api/posts/<int:post_id>')
def json_page_post_by_id(post_id):
    """Вывод поста в формате json ПО id"""
    data = config.user_dao.get_user_by_id(post_id)
    logger.debug(f"Запрос  /api/posts/{post_id}")
    return jsonify(data)