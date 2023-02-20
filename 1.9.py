# импорт пандаса
import pandas as pd
# импорт джейсона
import json

# создание первой функции
def stats(data):
    # посчет количества цветных фильмов
    data_1 = data[data['color'] == 'Color'].shape[0]
    # подсчет фильмов
    num_rows = data.shape[0]
    # делим
    quotient = data_1 / num_rows
    # получаем процент цветных фильмов
    percent = quotient * 100

    # все режиссеры
    directors = data["director_name"].value_counts()
    # 5 самых топовых!
    directors_1 = directors.head(5)

    # медианное значение
    durations = data['duration'].median()
    # durations_1 = durations.sum()
    # суммируем все длины фильмов
    durations_2 = data['duration'].sum()
    # получаем среднее значение
    middle = durations_2 / num_rows

    # какие есть жанры
    genres = data["genres"].value_counts()
    # 5 самых популярных!
    genres_1 = genres.head(5)

    # выводим процент цветных фильмов
    print("Процент цветных фильмов:", percent, '\n')
    # выводим топ-5 режиссеров
    print("Топ-5 режиссеров:", '\n', directors_1, '\n')
    # выводим среднее значение
    print("Среднее значение:", middle, '\n')
    # выводим медианное значение
    print("Медианное значение:", durations, '\n')
    # выводим топ-5 жанров
    print("Топ-5 жанров:", '\n', genres_1, '\n')
    # выводим фильмы c нужными словами и нужной оценкой
    print("Содержат love, romance и imdb_score > 7:" , data.loc[((data[data['imdb_score'] > 7]).shape[0] & (data['plot_keywords'].str.contains('love', 'romance')).shape[0])].shape[0])



# создание второй функции
def df2json(data1, data2):
    # разбиение таблицы на словари заданного формата
    meoaw = data1.to_dict(orient='records')
    # добавление словарей в список
    func = list(meoaw)
    # открываем конечный файл
    with open(data2, 'w') as output_file:
        # сохраняем туда все
        json.dump(func, output_file, indent=4)


# создание третьей функции
def main():
    # создание таблицы из csv
    data_file = pd.read_csv("https://raw.githubusercontent.com/aaaksenova/NLP-Homework/main/movie_metadata.csv", sep=",")
    # вызов первой функции
    stats(data_file)
    # вызов второй функции
    df2json(data_file, 'movie_metadata2.json')


# указание точки входа
if __name__ == "__main__":
    # вызываем третью функцию
    main()
