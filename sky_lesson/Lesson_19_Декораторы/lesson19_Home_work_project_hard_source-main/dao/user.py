from dao.model.user import User


class UserDAO():
    def __init__(self, session):
        self.session = session

    def create_user(self, user_data):
        """Создать user"""
        ent = User(**user_data)
        self.session.add(ent)
        self.session.commit()
        return ent

    def get_all_users(self):
        return self.session.query(User).all()

    def get_one_user(self, user_id):
        return self.session.query(User).get(user_id)

    def get_by_username(self, username):
        return self.session.query(User).filter(User.username == username).one()

    def update_user(self, user_data):
        user = self.get_one_user(user_data.get('id'))
        if user_data.get('name'):
            user.name = user_data.get('name')
        if user_data.get('role'):
            user.role = user_data.get('role')
        if user_data.get('password'):
            user.role = user_data.get('password')
        self.session.add(user)
        self.session.commit()

    def delete_user(self, user_id):
        user = self.get_one_user(user_id)
        self.session.delete(user)
        self.session.commit()