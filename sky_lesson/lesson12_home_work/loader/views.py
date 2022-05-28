from flask import Flask, Blueprint

# app = Flask(__name__)

# Cоздаем блюпринт
loader_foto_blueprint = Blueprint('loader_foto', __name__)


@loader_foto_blueprint.route('/foto/', methods=["GET", "POST"])
def loader_foto_page():
    #
    # filename = pic.filename  # Получаем имя файла у загруженного файла
    # pic.save(f"./uploads/images/ {filename}")  # Сохраняем картинку под родным именем в папку /uploads/images/
    #
    # print("loader_foto_blueprint")

    return f"Я страничка для загрузки фото пользователя"

# app.run()