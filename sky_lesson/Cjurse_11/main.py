from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)  # создаем экземпляр класса


@app.route('/image/')
def image():
    """Выводит картинку для первой части Д/З"""
    return render_template("image.html")


@app.route('/')
def all_candidates():
    """Выводит список имен всех кандидатов"""
    list_name = load_candidates_from_json()  # все словари кандидатов
    return render_template('list.html', list_name=list_name)


@app.route('/candidate/<int:x>/')
def candidate(x):
    """Выводит данные кандидата по  id """
    dict = get_candidate(x)  # получаем словарь по id
    return render_template('card.html',
                           name=dict['name'],
                           age=dict['age'],
                           position=dict['position'],
                           picture=dict['picture'],
                           skills=dict['skills']
                           )


@app.route('/search/<candidate_name>/')
def search_candidate_name(candidate_name):
    """Выводит кандидатов, в имени у которых содержится candidate_name """
    list_count_name = get_candidates_by_name(candidate_name)  # список совпадений
    num = len(list_count_name)
    return render_template('search.html', list_count_name=list_count_name, num=num)


@app.route('/skill/<skill_name>/')
def skill_name(skill_name):
    """Выводит кандидатов, в списке навыков у которых содержится skill"""
    list_skill_name = get_candidates_by_skill(skill_name)  # список кандидатов
    num = len(list_skill_name)  # количество кандидатов
    return render_template('skill.html', list_skill_name=list_skill_name, skill_name=skill_name, num=num)


if __name__ == '__main__':
    app.run()
