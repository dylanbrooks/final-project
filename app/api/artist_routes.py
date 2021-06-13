from flask import Blueprint, jsonify, request
from app.models import db, Artist, Song, Translation
from flask_login import current_user, login_required

artist_routes = Blueprint("artists", __name__)

@artist_routes.route("/")
def artists():
    artists = Artist.query.all()
    return {"artists" : [artist.to_dict() for artist in artists]}

@artist_routes.route("/<int:id>")
def songs(id):
    artist = Artist.query.get(id)
    songs = Song.query.filter(Song.artistId == id).limit(10)
    return {
        "artist": artist.to_dict(),
        "songs": [song.to_dict() for song in songs]
    }
