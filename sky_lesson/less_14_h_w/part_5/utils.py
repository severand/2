import sqlite3


def data_films():
    """Подключение к базе и фильтрация данных"""
    with sqlite3.connect("../netflix.db") as connection:
        cur = connection.cursor()
    sqlite_query = """
                   SELECT "cast"
                   FROM netflix
                   WHERE 'cast' != "" 
                   AND "cast" LIKE '%Rose%McIver%' AND "cast" LIKE '%Ben%Lamb%'
                   GROUP BY 'Rose McIver' AND 'Ben Lamb'
                   LIMIT 1000
                   """
    cur.execute(sqlite_query)
    executed_query = cur.fetchall()
    data = executed_query
    return data


def get_actor(list_of_actors):
    """ Возвращает список актеров снимавшихся вместе
    с входящими актерами более 2 раз
    """
    actors = data_films()  # получаем данные
    for item in actors:
        data = ','.join(item).split(',')  # форматируем список актеров фильма
        return data

# if __name__ == '__main__':
#     print(get_actor('Rose McIver, Ben Lamb'))