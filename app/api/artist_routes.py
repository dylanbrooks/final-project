from flask import Blueprint, jsonify, request
from app.models import db, Artist, Song

artist_routes = Blueprint("artists", __name__)
song_routes = Blueprint("songs", __name__)

@artist_routes.route("/")
def artists():
    artists = Artist.query.all()
    return {"artists" : [artist.to_dict() for artist in artists]}

@artist_routes.route("/<int:id>")
def songs(id):
    artist = Artist.query.get(id)
    songs = Song.query.filter(Song.artistId == id).limit(10)
    print('whatever i want')
    return {
        "artist": artist.to_dict(),
        "songs": [song.to_dict() for song in songs]
    }


@song_routes.route("/<int:id>")
def lyrics(id):
    song = Song.query.get(id)
    print('whatever i want')
    return {
        "song": song.to_dict()
    }
