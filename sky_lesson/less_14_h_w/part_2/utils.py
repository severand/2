import sqlite3


def data_films(year1, year2):
    """Подключение к базе и фильтрация данных"""
    with sqlite3.connect("../netflix.db") as connection:
        cur = connection.cursor()
    sqlite_query = f"""
                   SELECT title, country, release_year, listed_in, description, date_added
                   FROM netflix
                   WHERE release_year != '' 
                   AND release_year BETWEEN {year1} AND {year2}
                   ORDER BY release_year DESC             
                   LIMIT 10
                   """
    cur.execute(sqlite_query)
    executed_query = cur.fetchall()
    data = executed_query
    print(data)
    return data


data_films(2016, 2018)


def get_films_range(year_start, year_end):
    """Поиск фильмов в диапазоне по дате выпуска"""
    data = []
    films = data_films()
    for i in films:
        if i[2] >= int(year_start) and i[2] <= int(year_end):
            new_dict = dict(zip(["title", "release_year"], [i[0], i[2]]))  # создаем новый словарь
            data.append(new_dict)

    return data

# if __name__ == '__main__':
#     print(get_films_range('2016', '2017'))