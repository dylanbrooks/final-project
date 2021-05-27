from .db import db

class Translation(db.Model):
    __tablename__ = 'translations'

    id = db.Column(db.Integer, primary_key=True)
    translation = db.Column(db.String, nullable=False)
    startIndex = db.Column(db.Integer, nullable=False)
    stopIndex = db.Column(db.Integer, nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # songId = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'translation': self.translation,
            'startIndex': self.startIndex,
            'stopIndex': self.stopIndex,
            'userId': self.userId,
            # 'songId': self.songId
        }
