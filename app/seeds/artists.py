# from werkzeug.security import generate_password_hash
from app.models import db, Artist


# Adds a demo user, you can add other users here if you want
def seed_artists():

    jao = Artist(
        name='Jao', imageUrl='https://images.genius.com/d0af812a25991286af3e1d3f2cf27def.1000x1000x1.png')
    stayc = Artist(
        name='STAYC', imageUrl='https://images.genius.com/f20b57fc8e0eec49da30d22acf7b5b46.766x766x1.png')
    ozuna = Artist(
        name='Ozuna', imageUrl='https://images.genius.com/80bdeecd185f21dcc0eed81d8bac27ee.918x918x1.png')
    anuel = Artist(
        name='Anuel AA', imageUrl='https://images.genius.com/dda934aaa976e32ef040db739b64ed68.1000x1000x1.png')
    rauw = Artist(
        name='Rauw Alejandro', imageUrl='https://images.genius.com/f553b78a0795edb547d2cef8b5be8b79.483x483x1.jpg')

    db.session.add(jao)
    db.session.add(stayc)
    db.session.add(ozuna)
    db.session.add(anuel)
    db.session.add(rauw)

    db.session.commit()

    
# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_artists():
    db.session.execute('TRUNCATE artists RESTART IDENTITY CASCADE;')
    db.session.commit()
