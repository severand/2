# coding=utf8
USER_PATH = "./data/data.json"
POST_PATH = "./data/comments.json"

# импорт класса для работы с юзером
from Course_3_course.app.user.dao.user_dao import UserDAO

user_dao = UserDAO(USER_PATH)  # экземпляр класса  UserDAO

# импорт класса для работы с постами и комментами
from Course_3_course.app.post.dao.dao_post import PostDAO

post_dao = PostDAO(POST_PATH)