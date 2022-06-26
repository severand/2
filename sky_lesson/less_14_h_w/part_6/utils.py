import sqlite3
import json


def data_films():
    """Подключение к базе и фильтрация данных"""
    with sqlite3.connect("../netflix.db") as connection:
        cur = connection.cursor()
    sqlite_query = """
                   SELECT type, release_year, listed_in, title, description
                   FROM netflix
                   WHERE title != "" AND type != '' AND release_year != '' AND listed_in != '' AND description != ''
                   AND type == 'Movie' OR type == 'TV Show' 
                   GROUP BY title, release_year, description     
                   LIMIT 1000
                   """
    cur.execute(sqlite_query)
    executed_query = cur.fetchall()
    data = executed_query
    return data


def get_title_and_descr(typ, release_year, genre):
    """Возвращает словарь с названием и описанием фильма в словаре"""
    data = []
    films = data_films()
    for item in films:
        if typ in item[0]:  # поиск по типу
            if int(release_year) == int(item[1]):  # поиск по году релиза
                if genre in item[2]:  # поиск по жанру
                    new_dict = dict(zip(["title", "description"], [item[3], item[4]]))  # создаем новый словарь
                    data.append(new_dict)

    return json.dumps(data)

# if __name__ == '__main__':
#     print(get_title_and_descr('Movie', '2010', 'Dramas'))