# from werkzeug.security import generate_password_hash
from app.models import db, Song

def seed_songs():

    me_beija_com_raiva = Song(
        name='Me Beija Com Raiva', albumArtUrl='https://images.genius.com/744fef9d5c19f101b2c505bb569a6d35.640x640x1.jpg',
        lyrics='''[Verso 1]\nDe sonhadores a inimigos\nVocê tá indo, vai me deixar aqui perdido\nCê já contou pros seus amigos de nós?\n\n
        [Verso 2]
        No chão do quarto, com nossos vícios
        É coisa pura de tanto amar virou loucura
        De tantas brigas, amargura entre nós
        
        [Pré-refrão]
        Errei, larguei, não nego não
        Mas lembra do que eu disse, então
        Amar é muito melhor que ter razão
        Luta por mim, desiste não
        E lembra do que eu disse, então
        Amar é muito melhor que ter razão
        
        [Refrão]
        Joga tua verdade toda na minha cara
        Mas antes de ir embora eu te impeço, para
        E me beija com raiva, me beija com raiva
        Como fodemos o maior amor do mundo?
        Sei lá se esse é o nosso ultimo segundo
        Então me beija com raiva, me beija com raiva''',
        artistId='1', userId='1')
    amor_pirata = Song(
        name='AMOR PIRATA', albumArtUrl='https://images.genius.com/904b7c7ca19a7943d8bd38d9e26dc8b6.1000x1000x1.jpg',
        lyrics='''[Verso 1]\nEu n\u00e3o t\u00f4 fazendo nada\nAlta noite, madrugada\nDiz a\u00ed voc\u00ea(Diz a\u00ed voc\u00ea)\nEu posso passar na tua casa\nCom essa minha cara-lavada\nDe quem sabe o que dizer? (Eu sei o que dizer)\n\n[Pr\u00e9-Refr\u00e3o]\nVoc\u00ea finge que acredita e eu pago pra ver\nN\u00e3o vou mudar tua vida, mas \u00e9 bom de ter\nAmores de uma noite ainda s\u00e3o amores, \u00ea\n\n[Refr\u00e3o]\nA gente se apaixona s\u00f3 na sexta-feira\nJura amor eterno, mas de brincadeira\nE o nosso \"pra sempre\" dura a noite inteira\nAh, ah-ah\nGosto quando sua boca mente assim\nEu n\u00e3o sou pra voc\u00ea, voc\u00ea n\u00e3o \u00e9 pra mim\nE o nosso \"pra sempre\" dura a noite inteira\nAh, ah-ah\n\n[P\u00f3s-Refr\u00e3o]\n(Um, dois, tr\u00eas)\n\n[Verso 2]\nPraia do Futuro \u00e0 noit\u0435\nMal consigo ouvir seu nome\nMe av\u0435nturo em voc\u00ea (\u00d4h)\nO som alto, luzes fortes\nEsse nosso amor pirata\nA gente sabe o que fazer, \u00ea-\u00ea, \u00ea\n\n[Pr\u00e9-Refr\u00e3o]\nVoc\u00ea finge que acredita e eu pago pra ver\nN\u00e3o vou mudar tua vida, mas \u00e9 bom de ter\nAmores de uma noite ainda s\u00e3o amores, \u00ea-i\u00ea (\u00ca-i\u00ea)\n\n[Refr\u00e3o]\nA gente se apaixona s\u00f3 na sexta-feira\nJura amor eterno, mas de brincadeira\nE o nosso \"pra sempre\" dura a noite inteira\nAh, ah-ah (\u00f4-\u00f4-\u00f4)\nGosto quando sua boca mente assim\nEu n\u00e3o sou pra voc\u00ea, voc\u00ea n\u00e3o \u00e9 pra mim\nE o nosso \"pra sempre\" dura a noite inteira\nAh, ah-ah\n\n[Sa\u00edda]\nNosso amor \u00e9 s\u00f3 de brincadeira\nDura a noite inteira, ah\nNosso amor \u00e9 s\u00f3 de brincadeira (\u00d4-\u00f4h)\n(\u00d4-\u00f4h) Dura a noite inteira, ah\nNosso amor \u00e9 s\u00f3 de brincadeira\nDura a noite inteira, ah''',
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
    asap = Song(
        name='ASAP', albumArtUrl='https://images.genius.com/3fad5b29419dc447ed7d68e8739019b1.1000x1000x1.png',
        lyrics="[Intro: All]<br>STAYC girls, it's going down < br > <br > [Verse 1: J & amp; < i > Sumin < /i > ] < br > Time is running, boy, 그건 누구에겐 돈 < br > You know I'm so dope, 더는 못 기다려 줘<br><i>원래 나는 좀 참을성이 없는 몸<br>솔직한 게 좋은 걸, but you gotta know, yeah-yeah</i><br><br>[Pre-Chorus: Seeun, <i>Isa</i> &amp; <b>Yoon</b>]<br>달콤하기만 해도 싫어, so check it<br>매너 좋은 거 착한 거는 나도 구분해, yeah<br><i>순간 반짝할 거면 시작도 않는 걸<br>Sometimes, 내가 생각해도</i> (<b>I think I'm really cool < /b > ) < br > <br > [Chorus: Sieun & amp; < i > Yoon < /i > ] < br > ASAP, 내 반쪽, 아니, 완전 copy < br > 나와 똑같아 내 맘 잘 알아줄 < br > <i > ASAP, 꼭 닮은 내 décalcomanie < br > 눈앞에 나타나 줘 < /i > <br > <br > [Post-Chorus: Isa, < i > Sumin < /i > &amp; < b > Seeun < /b > ] < br > ASAP < br > Hoo-ooh-ooh-ooh < br > <i > ASAP < br > Hoo-ooh-ooh-ooh < /i > <br > <b > 눈앞에, 눈앞에, 나타나 줘",
        artistId='2', userId='1'
    )
    tiempo = Song(
        name='Tiempo', albumArtUrl='https://images.genius.com/0cf5244b2123b6b9234b6cd7cae570d5.1000x1000x1.png',
        lyrics="[Intro]<br>Woh-oh-oh-oh-oh-oh, jajaja<br>Woh-oh-oh-oh-oh-oh<br>Sky Rompiendo El Bajo<br>Dímelo, Gotay<br><br>[Coro]<br>Me puse a dedicarte tiempo (Tiempo)<br>Tiempo del que yo había perdido (Perdido)<br>Amore' como el tuyo, no lo entiendo(No lo entiendo) < br > Estoy solo y ahora eso e' un lío (Eh, eh)<br>Porque salgo pa' la pista, pa'l party<br>Babie' suelta', alcohol y mari (Mari)<br>No quiero que me llame', mami(Woh) < br > Ando suelto de party por Miami < br > <br > [Verso 1] < br > Ma', tan chulita que te ve' (Que te ve')<br>Ese booty parece de TV (De TV, V)<br>Ando con par dе trago' y par de .10 (Woh) < br > Yo te di banda pa' que tú mе la de' (Woh) < br > Mi cubanita quiere que prenda < br > Tú me conoce', por eso e' que no uso prenda'<br>Jangueando en Dubái, las babie' están flow Kendall < br > Yo soy la movie, cabrone', no me la vendan<br>Mi cubanita quiere que prenda<br>Tú me conoce', por eso e' que no uso prenda' < br > Jangueando en Dubái, las babie' están flow Kendall (¡Yah!)<br>Yo soy la movie, cabrone', no me la vendan, yeah-eh-eh",
        artistId='3', userId='1'
    )

    db.session.add(me_beija_com_raiva)
    db.session.add(amor_pirata)
    db.session.add(coringa)
    db.session.add(essa_eu_fiz_pro_nossa_amor)
    db.session.add(imaturo)
    db.session.add(vou_morrer_sozinho)
    db.session.add(triste_pra_sempre)
    db.session.add(asap)
    db.session.add(tiempo)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_songs():
    db.session.execute('TRUNCATE songs RESTART IDENTITY CASCADE;')
    db.session.commit()
