from .db import db


class Song(db.Model):
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    albumArtUrl = db.Column(db.String(250), nullable=False)
    lyrics = db.Column(db.String, nullable=False)
    artistId = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'albumArtUrl': self.albumArtUrl,
            'lyrics': self.lyrics,
            'artistId': self.artistId,
            'userId': self.userId
        }
