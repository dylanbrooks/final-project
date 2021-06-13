from .db import db


class Comments(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String, nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    songId = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'comment': self.translation,
            'userId': self.userId,
            'songId': self.songId
        }
