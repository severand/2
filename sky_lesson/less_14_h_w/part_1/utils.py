import sqlite3


def get_data_all():
    """Подключение к базе и получение данных"""
    with sqlite3.connect("../../lesson_14/netflix.db") as connection:
        cur = connection.cursor()
    sqlite_query = """
                SELECT title, country, release_year, listed_in, description, date_added
                FROM netflix
                WHERE title != '' AND country != '' AND release_year != '' AND listed_in != '' 
                AND description != '' AND date_added != ''
                ORDER BY date_added DESC                
                """
    cur.execute(sqlite_query)
    executed_query = cur.fetchall()
    data = executed_query
    return data


def get_data_all_project(title):
    """Поиск по названию фильма"""
    data = []
    data_title = get_data_all()
    for i in data_title:
        if i[0] == title:
            new_dict = dict(zip(["title",
                                 "country",
                                 "release_year",
                                 "genre",
                                 "description",
                                 "date_added"],
                                [i[0], i[1], i[2], i[3], i[4], i[5]]))  # создаем новый словарь
            data.append(new_dict)

    return data

# if __name__ == '__main__':
#     print(get_data_all_project('10 Days in Sun City'))