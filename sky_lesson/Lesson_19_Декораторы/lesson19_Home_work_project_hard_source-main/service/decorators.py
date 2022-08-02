import jwt
from flask import request, current_app

from implemented import user_service


def auth_required(func):
    """Проверяем наличие токена"""

    def wrapper(*args, **kwargs):
        if "Autorisation" not in request.headers:
            return "Вы не авторизовались", 401
        # token = request.headers.environ.get('HTTP_AUTHORISATION').replace('Bearer ', '')

        __data = request.json['Autorisation']
        token = __data.split("Bearer ")[-1]

        if not token:
            return "Токен отсутствует"

        try:
            jwt.decode(token,  # Декодируем токен
                       key=current_app.config['SECRET_KEY'],
                       algorithms=current_app.config['ALGORIHM'])
            return func(*args, **kwargs)
        except Exception:
            raise Exception

    return wrapper


def admin_required(func):
    """Проверяем роль пользователя"""

    def wrapper(*args, **kwargs):
        if "Autorisation" not in request.headers:
            return "Вы не авторизовались", 401

        __data = request.json['Autorisation']
        token = __data.split("Bearer ")[-1]

        # token = request.headers.environ.get('HTTP_AUTHORISATION').replace('Bearer ', '')

        if not token:
            raise Exception

        try:
            data = jwt.decode(token,  # Декодируем токен
                              key=current_app.config['SECRET_KEY'],
                              algorithms=current_app.config['ALGORIHM'])

            if user_service.get_by_name(data['username']).role == "admin":
                return func(*args, **kwargs)
            else:
                return "Нет прав"

        except Exception:
            raise Exception

    return wrapper