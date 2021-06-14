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
        lyrics='''[Intro: All]\nSTAYC girls, it's going down \n \n [Verse 1: J & amp; < i > Sumin < /i > ] \n Time is running, boy, 그건 누구에겐 돈 \n You know I'm so dope, 더는 못 기다려 줘\n<i>원래 나는 좀 참을성이 없는 몸\n솔직한 게 좋은 걸, but you gotta know, yeah-yeah</i>\n\n[Pre-Chorus: Seeun, <i>Isa</i> &amp; <b>Yoon</b>]\n달콤하기만 해도 싫어, so check it\n매너 좋은 거 착한 거는 나도 구분해, yeah\n<i>순간 반짝할 거면 시작도 않는 걸\nSometimes, 내가 생각해도</i> (<b>I think I'm really cool < /b > ) \n \n [Chorus: Sieun & amp; < i > Yoon < /i > ] \n ASAP, 내 반쪽, 아니, 완전 copy \n 나와 똑같아 내 맘 잘 알아줄 \n <i > ASAP, 꼭 닮은 내 décalcomanie \n 눈앞에 나타나 줘 < /i > \n \n [Post-Chorus: Isa, < i > Sumin < /i > &amp; < b > Seeun < /b > ] \n ASAP \n Hoo-ooh-ooh-ooh \n <i > ASAP \n Hoo-ooh-ooh-ooh < /i > \n <b > 눈앞에, 눈앞에, 나타나 줘"''',
        artistId='2', userId='1'
    )
    tiempo = Song(
        name='Tiempo', albumArtUrl='https://images.genius.com/0cf5244b2123b6b9234b6cd7cae570d5.1000x1000x1.png',
        lyrics="[Intro]\nWoh-oh-oh-oh-oh-oh, jajaja\nWoh-oh-oh-oh-oh-oh\nSky Rompiendo El Bajo\nDímelo, Gotay\n\n[Coro]\nMe puse a dedicarte tiempo (Tiempo)\nTiempo del que yo había perdido (Perdido)\nAmore' como el tuyo, no lo entiendo(No lo entiendo) \n Estoy solo y ahora eso e' un lío (Eh, eh)\nPorque salgo pa' la pista, pa'l party\nBabie' suelta', alcohol y mari (Mari)\nNo quiero que me llame', mami(Woh) < br > Ando suelto de party por Miami < br > \n [Verso 1] < br > Ma', tan chulita que te ve' (Que te ve')\nEse booty parece de TV (De TV, V)\nAndo con par dе trago' y par de .10 (Woh) < br > Yo te di banda pa' que tú mе la de' (Woh) < br > Mi cubanita quiere que prenda < br > Tú me conoce', por eso e' que no uso prenda'\nJangueando en Dubái, las babie' están flow Kendall < br > Yo soy la movie, cabrone', no me la vendan\nMi cubanita quiere que prenda\nTú me conoce', por eso e' que no uso prenda' < br > Jangueando en Dubái, las babie' están flow Kendall (¡Yah!)\nYo soy la movie, cabrone', no me la vendan, yeah-eh-eh",
        artistId='3', userId='1'
    )
    brindemos = Song(
        name='Brindemos', albumArtUrl='https://images.genius.com/794c2f77fec9455fb6758b5b1d7f683a.1000x1000x1.jpg',
        lyrics='''[Intro: Anuel AA & Ozuna, Ambos]\nReal Hasta La Muerte, \u00bfo\u00ed'te, cabr\u00f3n? (Eh)\nPerd\u00f3name Dios m\u00edo porque yo he pecado(Uah)\nTo' este dinero me tiene enamorado\nLa fama y el poder a m\u00ed me secuestraron\nPero yo no me vo'a morir\n\n[Pre-Coro: Anuel AA & Ozuna, Ozuna]\nY ahora estamo' aqu\u00ed, seguimo' aqu\u00ed\nYo soy intocable como Pablo en Medell\u00edn\nYo nunca vo'a matar a un hermano como Ca\u00edn (Woh-oh)\nYo tengo mis soldados como Osama y Hussein (Hussein, eh)\n\n[Coro: Anuel AA & Ozuna, Ozuna]\nBrindemo' por to' el dinero que hacemo' (Hacemo')\nBrindemo' por lo' carro' que tenemo' (Que tenemo')\nBrindemo' por lo' cuadrado' que vendemo' (Oh-oh-oh-oh)\nY a to'a las babies que les metemo'\nBrindemo' por to' el dinero que hacemo' (Hacemo')\nBrindemo' por lo' carro' que tenemo' (Que tenemo')\nBrindemo' por lo' cuadrado' que vendemo' (Oh-oh-oh-oh)\nY a to'a las babies que les metemo' (Eh)\n\n[Verso 1: Anuel AA]\nMis hermanos se mueren por m\u00ed\nYo me muero por ellos tambi\u00e9n (Tambi\u00e9n)\nLos kilo' en los faldo', los faldo' en los bote'\nY por faldo, los kilo' son cien(Cien)\nYo soy una estrella\nAlzo mis cadena' como si estuviera en Bel\u00e9n (Am\u00e9n)\nY yo tengo una cruz en el bicho\nY tengo a tu puta grit\u00e1ndome \"am\u00e9n\" (Jaja)\nEl diablo rojo, rorrueco, la FN rompe chaleco (Jeje)\nLa droga to'as pa' los teco' y t\u00fa te va' a morir como Cheko (Jeje)\n200 mil en el cuello (Cuello)\nLo' kilo 'e droga y lo' sello' (Lo' sello')\nTe mandamo' en el expreso\nY el talib\u00e1n se cae del camello(\u00a1Brr!; brr)\nEl Draco pinta'o Louis Vuitton (Louis Vuitton)\nLa 9 full con el Bot\u00f3n (Brr)\nDe enfriamiento el sistem\u00f3n\nY de peine' de 30 yo tengo un vag\u00f3n(Jaja)\nLa glope es de la cuarta generaci\u00f3n\nLe compr\u00e9 el de 50 al Tet\u00f3n(Al Tet\u00f3n)\nEn el casco te pongo un mill\u00f3n\nY los gato' to' van a cazar al rat\u00f3n(Brr), brr\nMe compr\u00e9 el Panamera(-namera)\nAcosta'o en mi celda, desde la nevera (Desde la nevera)\nY los cabrone' que a m\u00ed me arrestaron\nPensaron que me jodieron mi carrera(Real Hasta La Muerte)\nPero les hice un mill\u00f3n 'tando preso\nY yo soy intocable adentro y afuera (27, cabr\u00f3n)\nY mi puta est\u00e1 hecha completa\nY tiene el culo como Natalia Rivera (Jaja)\n\n[Coro: Ozuna, Ozuna & Anuel AA]\nBrindemo' por to' el dinero que hacemo' (Hacemo')\nBrindemo' por lo' carro' que tenemo' (Que tenemo')\nBrindemo' por lo' cuadrado' que vendemo' (Oh-oh-oh-oh)\nY a to'a las babies que les metemo'\nBrindemo' por to' el dinero que hacemo'\nBrindemo' por lo' carro' que tenemo'\nBrindemo' por lo' cuadrado' que vendemo'\nY a to'a las babies que les metemo'\n\n[Verso 2: Ozuna & Anuel AA]\nOzuna (Brr)\nBrindemo' por lo que tenemo' (Uoh-oh-oh-oh)\nEl ticket que hicimo', el ticket que hacemo' (Baby; am\u00e9n)\nDe la m\u00fasica, millone' recogemo' (Jaja)\nTe la traficamo' como si fuera el veneno, yo'-o'-o'\nRafagazo pa' sentir\nDonde estoy, no hay ning\u00fano pa' yo competir\nPablo y el Chapo de palo refill\nUna falla y te mandamo' con los difunto' a dormir\nA tu gata le metemo'\nLa cuenta no tiene freno(Baby)\nPor los enemigos brindemo'\nLa v\u00eda es directa, ya no nos caemo', yeh\nPatek, AP Tourbill\u00f3n\nCotiza esta combi, ya vale un mill\u00f3n(Prro)\nNo corremo' con la traici\u00f3n (Uoh-oh)\nYo vend\u00eda pel\u00edcula, ahora monto pelicul\u00f3n\nBrindemo', doble A, en el juego estamo'\nFlipiamo' la caleta y duplicamo', yeh\n\n[Coro: Anuel AA & Ozuna, Ambos]\nBrindemo' por to' el dinero que hacemo' (Uah)\nBrindemo' por lo' carro' que tenemo'\nBrindemo' por lo' cuadrado' que vendemo'\nPor las babies que les metemo'\n\n[Puente: Anuel AA & Ozuna, Ozuna]\nY ahora estamo' aqu\u00ed('Tamos aqu\u00ed)\nSeguimo' aqu\u00ed(Seguimo' aqu\u00ed)\nYo soy intocable como Pablo en Medell\u00edn (Uoh-oh-oh-oh)\nYo nunca vo'a matar a un hermano como Ca\u00edn(Como Ca\u00edn)\nYo tengo mis soldados como Osama y Hussein\n\n[Outro: Anuel AA]\n\u00a1Brr!''',
        artistId='4', userId='1'
    )
    yeezy = Song(
        name='Yeezy', albumArtUrl='https://images.genius.com/794c2f77fec9455fb6758b5b1d7f683a.1000x1000x1.jpg',
        lyrics='''[Intro: Anuel AA]\nBaby, ponte las Yeezy, las Yeezy, las Yeezy\nReal Hasta La Muerte, \u00bfo\u00ed'te, cabr\u00f3n?\nBrr, lo' intocable', lo' iluminati'\nAnuel\n\n[Verso 1: Anuel AA]\nLos demonio', los diablo' y los lobo' (Los lobo')\nEl AKA y el cabo 'e caobo (Brr)\nT\u00fa eres casada pero yo te robo (Te robo)\nT\u00fa te parece' a Carmen Villalobos (Villalobo)\nLa maldad se te nota en la cara (Uah)\nLas nalgas 'e Sophia Vergara\nLe di 7 mil pa' que se me operara\nY le di otros 3 mil pa' que se me tatuara, eh, eh\nEl diablo en mujer (Mujer)\nLe gusta fumar y beber (Beber)\nLo voy a enrolar pa' prender\nP\u00f3nteme en cuatro, beb\u00e9, que te lo vo'a meter (Jaja)\nYo bebo code\u00edna, mi puta e' fina (Fina)\nHija de puta como la felina (La felina)\nYo te lo meto en el Jet o en un bote en la playa (Skrt, skrt)\nComo Rafael Amaya (Jaja)\nFronte\u00e1ndome, ella se hizo las nalgas (Uah)\nY yo tengo el Draco en la falda (Uah)\nPero ella es una diabla\nElla sigue fronte\u00e1ndome\nYo no voy a perderla porque yo no vo'a amarla\nPero que rico es tenerla, uh, yeh-eh-eh (Uah)\n\n[Estribillo: Anuel AA]\nT\u00fa te trepas encima de m\u00ed y yo adentro de ti, te toqu\u00e9 el punto G\nBaby, ponte las Yeezy, las Yeezy\nY m\u00e1mame el bicho en el Panamera (Skrt)\nLos 47 solda'os y los R de posici\u00f3n, y 30 kilos en el Jet (Brr)\nBaby, ponte las Yeezy, las Yeezy\nLas Yeezy, las Yeezy, las Yeezy (Uah)\nT\u00fa te trepas encima de m\u00ed y yo adentro de ti, te toqu\u00e9 el punto G\nBaby, ponte las Yeezy, las Yeezy\nY m\u00e1mame el bicho en el Panamera (Skrt)\nLos 47 solda'os y los R de posici\u00f3n, y 30 kilos en el Jet (Brr)\nBaby, ponte las Yeezy, las Yeezy\nLas Yeezy, las Yeezy, las Yeezy (Uah)\n\n[Verso 2: Anuel AA]\nMe mont\u00e9 en el Porsche to' vest\u00ed'o 'e Versace\nY la baby vestida de Chanel (Anuel)\nSi yo fuera 'e Colombia yo fuera Pablo\nY si yo fuera de Cuba Fidel (Fidel)\nYo tengo 3 Draco' y yo soy intocable como Jes\u00fas en Israel (\u00a1Brr!)\nLos Draco' en las mano\nY te vamo' a hablar con las mano', cabr\u00f3n, como Eliel (Jaja)\nYo te pongo tu pierna en mi hombro\nY ese totito yo te lo vo'a joder (Joder)\nYo estaba preso pero ese totito por FaceTime lo puse a llover (Jeje)\nY yo no puedo fumar porque mi oficial de la proba- me va a revocar (Revocar)\nPero yo tengo una perla en el bicho y yo te vo'a poner tu totito a llorar (Jaja)\nChingando en la ducha\nTu totito me habla y mi bicho te escucha (Te escucha)\nLa Champa\u00f1a fucsia (Fucsia)\nYo estoy to' tatua'o como Los Salvatruchas (Brr)\nLos kilos de lenta, las tetas 'e 50 pa' to'a las 40 (\u00a1Brr!)\nMe compr\u00e9 la novena fulete\nY las tetas de 100 con los peine' de 30 (Brr)\nPint\u00e9 la glopeta de blanco\nBlanco coca\u00edna, blanca Lady Gaga (Lady Gaga)\nElla me escupe to' el bicho\nPero yo se la echo en la boca y siempre se la traga (Ah)\nGast\u00e9 mil 300 en las Bred\nY gaste mil 500 en las Balenciaga' (Balenciaga')\nY yo le meto este bicho a tu puta\nY siempre en la madre del diablo se caga (\u00a1Jajaja!; uah)\n\n[Estribillo: Anuel AA, \u00d1engo Flow ]\nT\u00fa te trepas encima de m\u00ed y yo adentro de ti te toqu\u00e9 el punto G (yeh)\nBaby, ponte las Yeezy, las Yeezy, y m\u00e1mame el bicho en el Panamera (yeh-eh-eh; skrt)\nLos 47 soldados y los R de posici\u00f3n y 30 kilos en el Jet (brr)\nBaby, ponte las Yeezy, las Yeezy, las Yeezy, las Yeezy, las Yeezy\nT\u00fa te trepas encima de m\u00ed y yo adentro de ti te toqu\u00e9 el punto G (uah-ah)\nBaby ponte las Yeezy, las Yeezy, y m\u00e1mame el bicho en el Panamera (skrt)\nLos 47 soldados y los R de posici\u00f3n y 30 kilos en el Jet (brr)\nBaby, ponte las Yeezy, las Yeezy, las Yeezy, las Yeezy, las Yeezy (uah)\n\n[Verso 3: \u00d1engo Flow]\nAntes de acostarme si llega la noche a los santos le rezo (baby)\nCon la Yeezy puesta la pongo a mamarme el bicho en el expreso (jajaja)\nSus ojos le dan vuelta, cuando ese toto le beso\nHoy yo te voy a joder to' la salud (yeh, yeh, yeh)\nDe abajo pa' arriba, estrujarte los huesos (mami; prr)\nEre' una bellaca igualita que yo\nLl\u00e9gale a mi cuarto pa' matarno' lo' do'\nPal'cabr\u00f3n de tu novio yo tengo una Glock\nCon 15 peinillas para d\u00e1rselos to'\nLa tormenta me lleva y me trae\nPa' todas estas putas tengo el bicho en high\nTropical como el flow de Hawai\nChingando en la arena por el desierto de Dubai\nYo soy tu baby, por siempre ser\u00e1s tu mi baby tambi\u00e9n\nFumando y chingando, el totito le huele a perfume 'e Cartier\nMe hice due\u00f1o de su piel, t\u00fa la enga\u00f1aste y yo la trate bien\nTrabaja los kilos conmigo\nEmpaca y bombea, tiene lo de ella tambi\u00e9n (uah)\n\n[Estribillo: Anuel AA, \u00d1engo Flow]\nT\u00fa te trepas encima de m\u00ed y yo adentro de ti te toqu\u00e9 el punto G\nBaby, ponte las Yeezy, las Yeezy, y m\u00e1mame el bicho en el Panamera (skrt)\nLos 47 soldados y los R de posici\u00f3n y 30 kilos en el Jet (brr)\nBaby, ponte las Yeezy, las Yeezy, las Yeezy, las Yeezy, las Yeezy (uah)\nT\u00fa te trepas encima de m\u00ed y yo adentro de ti te toqu\u00e9 el punto G\nBaby, ponte las Yeezy, las Yeezy, y m\u00e1mame el bicho en el Panamera (skrt)\nLos 47 soldados y los R de posici\u00f3n y 30 kilos en el Jet (brr)\nBaby, ponte las Yeezy, las Yeezy, las Yeezy, las Yeezy, las Yeezy (uah)''',
        artistId='4', userId='1'
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
    db.session.add(brindemos)
    db.session.add(yeezy)


    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_songs():
    db.session.execute('TRUNCATE songs RESTART IDENTITY CASCADE;')
    db.session.commit()
