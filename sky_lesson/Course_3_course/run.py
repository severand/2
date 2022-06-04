# coding=utf8
import logging
from Course_3_course.logs import logger

from flask import Flask

from Course_3_course.app.main.views import main_blueprint
from Course_3_course.app.post.views import post_blueprint
from Course_3_course.app.user.views import user_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(user_blueprint)

logger.create_logs()
logger = logging.getLogger("api_logs.txt")


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Страница не найдена</h1>"  "<a href='/' <p>Вернуться в ленту</p> </a>", 404


@app.errorhandler(500)
def page_not_found(e):
    return "<h1>Ошибка сервера</h1>"  "<a href='/'  <p>Вернуться на главную</p>  </a>", 500


if __name__ == "__main__":
    logger.debug("Приложение запущено")
    app.run(debug=True)