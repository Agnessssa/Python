import pandas as pd
import json

def stats(data):
    data_1 = data[data['color'] == 'Color'].shape[0]
    num_rows = data.shape[0]
    quotient = data_1 / num_rows
    percent = quotient * 100

    directors = data["director_name"].value_counts()
    directors_1 = directors.head(5)

    durations = data['duration'].median()
    durations_2 = data['duration'].sum()
    middle = durations_2 / num_rows

    genres = data["genres"].value_counts()
    genres_1 = genres.head(5)

    print("Процент цветных фильмов:", percent, '\n')
    print("Топ-5 режиссеров:", '\n', directors_1, '\n')
    print("Среднее значение:", middle, '\n')
    print("Медианное значение:", durations, '\n')
    print("Топ-5 жанров:", '\n', genres_1, '\n')
    print("Содержат love, romance и imdb_score > 7:" , data.loc[((data[data['imdb_score'] > 7]).shape[0] & (data['plot_keywords'].str.contains('love', 'romance')).shape[0])].shape[0])



def df2json(data1, data2):
    meoaw = data1.to_dict(orient='records')
    func = list(meoaw)
    with open(data2, 'w') as output_file:
        json.dump(func, output_file, indent=4)


def main():
    data_file = pd.read_csv("https://raw.githubusercontent.com/aaaksenova/NLP-Homework/main/movie_metadata.csv", sep=",")
    stats(data_file)
    df2json(data_file, 'movie_metadata2.json')


if __name__ == "__main__":
    main()
