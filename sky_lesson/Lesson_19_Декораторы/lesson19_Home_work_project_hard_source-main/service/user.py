from dao.user import UserDAO
from service.auth import generate_password_hash


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def create(self, data):
        data['password'] = generate_password_hash(password=data['password'])
        return self.dao.create_user(data)

    def get_all(self):
        return self.dao.get_all_users()

    def get_one(self, user_id):
        return self.dao.get_one_user(user_id)

    def get_by_name(self, username):
        return self.dao.get_by_user_name(username)

    def update(self, user_data):
        self.dao.update(user_data)
        return self.dao

    def delete(self, user_id):
        self.dao.delete_user(user_id)