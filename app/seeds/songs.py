# from werkzeug.security import generate_password_hash
from app.models import db, Song

def seed_songs():

    me_beija_com_raiva = Song(
        name='Me Beija Com Raiva', albumArtUrl='https://images.genius.com/744fef9d5c19f101b2c505bb569a6d35.640x640x1.jpg',
        lyrics='[Verso 1]<br>De sonhadores a inimigos<br>Você tá indo, vai me deixar aqui perdido<br>Cê já contou pros seus amigos de nós?<br><br>[Verso 2]<br>No chão do quarto, com nossos vícios<br>É coisa pura de tanto amar virou loucura<br>De tantas brigas, amargura entre nós<br><br>[Pré-refrão]<br>Errei, larguei, não nego não<br>Mas lembra do que eu disse, então<br>Amar é muito melhor que ter razão<br>Luta por mim, desiste não<br>E lembra do que eu disse, então<br>Amar é muito melhor que ter razão<br><br>[Refrão]<br>Joga tua verdade toda na minha cara<br>Mas antes de ir embora eu te impeço, para<br>E me beija com raiva, me beija com raiva<br>Como fodemos o maior amor do mundo?<br>Sei lá se esse é o nosso ultimo segundo<br>Então me beija com raiva, me beija com raiva',
        artistId='1', userId='1')
    amor_pirata = Song(
        name='AMOR PIRATA', albumArtUrl='https://images.genius.com/904b7c7ca19a7943d8bd38d9e26dc8b6.1000x1000x1.jpg',
        lyrics='[Verso 1]<br>Eu não tô fazendo nada<br>Alta noite, madrugada<br>Diz aí você (Diz aí você)<br>Eu posso passar na tua casa<br>Com essa minha cara-lavada<br>De quem sabe o que dizer? (Eu sei o que dizer)<br><br>[Pré-Refrão]<br>Você finge que acredita e eu pago pra ver<br>Não vou mudar tua vida, mas é bom de ter<br>Amores de uma noite ainda são amores, ê<br><br>[Refrão]<br>A gente se apaixona só na sexta-feira<br>Jura amor eterno, mas de brincadeira<br>E o nosso "pra sempre" dura a noite inteira<br>Ah, ah-ah<br>Gosto quando sua boca mente assim<br>Eu não sou pra você, você não é pra mim<br>E o nosso "pra sempre" dura a noite inteira<br>Ah, ah-ah<br><br>[Pós-Refrão]<br>(Um, dois, três)',
        artistId='1', userId='1')
    coringa = Song(name='CORINGA', albumArtUrl='1',
                   lyrics='1', artistId='1', userId='1')
    essa_eu_fiz_pro_nossa_amor = Song(
        name='Essa Eu Fiz Pro Nossa Amor', albumArtUrl='1', lyrics='1', artistId='1', userId='1')
    imaturo = Song(name='Imaturo', albumArtUrl='1',
                   lyrics='1', artistId='1', userId='1')
    vou_morrer_sozinho = Song(
        name='Vou Morrer Sozinho', albumArtUrl='1', lyrics='1', artistId='1', userId='1')
    triste_pra_sempre = Song(
        name='Triste Pra Sempre', albumArtUrl='1', lyrics='1', artistId='1', userId='1')

    db.session.add(me_beija_com_raiva)
    db.session.add(amor_pirata)
    db.session.add(coringa)
    db.session.add(essa_eu_fiz_pro_nossa_amor)
    db.session.add(imaturo)
    db.session.add(vou_morrer_sozinho)
    db.session.add(triste_pra_sempre)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_songs():
    db.session.execute('TRUNCATE songs RESTART IDENTITY CASCADE;')
    db.session.commit()
