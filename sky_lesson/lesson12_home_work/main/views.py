from flask import Flask, Blueprint

# app = Flask(__name__)

# Cоздаем новый блюпринт, выбираем для него имя
view_foto_blueprint = Blueprint('view_foto_blueprint', __name__)


# Создаем вьюшку, используя в декораторе блюпринт вместо app
@view_foto_blueprint.route('/foto/<int:user_id>')
def foto_page(file_foto):
    """Для показывания фото"""

    # webbrowser.open(r"D:\{file_foto}")
    # return f"Я foto пользователя {user_id}"