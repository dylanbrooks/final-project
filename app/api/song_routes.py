from flask import Blueprint, jsonify, request
from app.models import db, Artist, Song, Translation
from flask_login import current_user, login_required

song_routes = Blueprint("songs", __name__)


@song_routes.route("/<int:id>")
def lyrics(id):
    song = Song.query.get(id)
    return {
        "song": song.to_dict()
    }
