import sqlite3
import json


def data_films():
    """Подключение к базе и фильтрация данных"""
    with sqlite3.connect("../netflix.db") as connection:
        cur = connection.cursor()
    sqlite_query = """
                   SELECT title, rating, description
                   FROM netflix
                   WHERE rating != '' 
                   AND rating LIKE 'G' OR rating LIKE 'PG' OR rating LIKE 'PG-13' OR rating LIKE 'R' OR rating LIKE 'PNC-17'                           
                   LIMIT 1000
                   """
    cur.execute(sqlite_query)
    executed_query = cur.fetchall()
    data = executed_query
    return data


def get_films_in_rating(rating):
    """Поиск фильмов по рейтингу"""
    data = []
    films = data_films()
    for i in films:
        if rating == 'children' and 'G' in i[1]:
            new_dict = dict(zip(["title", "rating", "description"], [i[0], i[1], i[2]]))  # создаем новый словарь
            data.append(new_dict)
        elif rating == 'family' and i[1] in ['G', 'PG', 'PG-13']:
            new_dict = dict(zip(["title", "rating", "description"], [i[0], i[1], i[2]]))
            data.append(new_dict)
        elif rating == 'adult' and i[1] in ['R', 'NC-17']:
            new_dict = dict(zip(["title", "rating", "description"], [i[0], i[1], i[2]]))
            print(i[1])
            data.append(new_dict)

    return data

# if __name__ == '__main__':
#     print(get_films_in_rating('children'))