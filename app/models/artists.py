from .db import db


class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    imageUrl = db.Column(db.String(250), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'imageUrl': self.imageUrl
        }