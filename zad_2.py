from flask import Flask
from flask_restful import Resource, Api
import csv

app = Flask(__name__)
api = Api(app)
path_to_movies = 'data/movies.csv'
movies_list = []


class MovieModel:
    def __init__(self, id, title, genres):
        self.id = id
        self.title = title
        self.genres = genres


class Movie(Resource):
    def get(self):
        return [movie.__dict__ for movie in movies_list]


def load_movies():
    with open(path_to_movies, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            movies_list.append(MovieModel(row[0], row[1], row[2]))


load_movies()

api.add_resource(Movie, '/movies')


if __name__ == '__main__':
    app.run(debug=True)
