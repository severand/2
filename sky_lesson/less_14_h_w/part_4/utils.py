import sqlite3
import json


def data_films():
    """Подключение к базе и фильтрация данных - свежие фильмы"""
    with sqlite3.connect("../../lesson_14/netflix.db") as connection:
        cur = connection.cursor()
    sqlite_query = """
                   SELECT title, description, listed_in, date_added
                   FROM netflix
                   WHERE date_added != '' AND listed_in != '' AND title != '' AND description != ''
                   ORDER BY date_added DESC 
                                                 
                   LIMIT 1000
                   """
    cur.execute(sqlite_query)
    executed_query = cur.fetchall()
    data = executed_query
    print(data)
    return data


def get_films_by_genre(genre):
    """Поиск фильмов по жанру"""
    data = []
    films = data_films()
    for item in films:
        if genre in item[2] and len(data) <= 9:
            new_dict = dict(zip(["title", "description"], [item[0], item[2]]))  # создаем новый словарь
            data.append(new_dict)

    return data


if __name__ == '__main__':
    print(get_films_by_genre('Dramas'))