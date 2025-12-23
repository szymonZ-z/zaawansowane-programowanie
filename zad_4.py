from flask import Flask
from flask_restful import Resource, Api
import csv

app = Flask(__name__)
api = Api(app)
path_to_movies = 'data/movies.csv'
movies_list = []

path_to_links = 'data/links.csv'
links_list = []

path_to_ratings = 'data/ratings.csv'
ratings_list = []

path_to_tags = 'data/tags.csv'
tags_list = []


class LinksModel:
    def __init__(self, movieId, imdbId, tmdbId):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId


class RatingsModel:
    def __init__(self, userId, movieId, rating, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp


class MovieModel:
    def __init__(self, id, title, genres):
        self.id = id
        self.title = title
        self.genres = genres


class TagsModel:
    def __init__(self, userId, movieId, tag, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp


class Movie(Resource):
    def get(self):
        return [movie.__dict__ for movie in movies_list]


class Link(Resource):
    def get(self):
        return [link.__dict__ for link in links_list]


class Rating(Resource):
    def get(self):
        return [rating.__dict__ for rating in ratings_list]


class Tag(Resource):
    def get(self):
        return [tag.__dict__ for tag in tags_list]


def load_movies():
    with open(path_to_movies, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            movies_list.append(MovieModel(row[0], row[1], row[2]))


def load_links():
    with open(path_to_links, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            links_list.append(LinksModel(row[0], row[1], row[2]))


def load_ratings():
    with open(path_to_ratings, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            ratings_list.append(RatingsModel(row[0], row[1], row[2], row[3]))


def load_tags():
    with open(path_to_tags, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            tags_list.append(TagsModel(row[0], row[1], row[2], row[3]))


load_movies()
load_ratings()
load_tags()
load_links()


api.add_resource(Movie, '/movies')
api.add_resource(Link, '/links')
api.add_resource(Tag, '/tags')
api.add_resource(Rating, '/ratings')


if __name__ == '__main__':
    app.run(debug=True)
