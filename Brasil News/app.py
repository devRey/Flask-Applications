from flask import Flask, render_template
from classes import Jornalistas
from classes import Noticias



#                        determinando Jornalistas
Jornalista1 = Jornalistas(1, "Beyoncé Giselle Knowles-Carter", "img/jornal1.png", "She Knows dos Famosos")
Jornalista2 = Jornalistas(2, "Chuu do Brasil News", "img/jornal2.png", "Colunista de Entretenimento")

jornalistasList = [Jornalista1, Jornalista2]

#                        determinando Categorias
# categoriaCultura = Categorias("Cultura")
# categoriaPolitica = Categorias("Política")


#                        determinando Notícias
Noticias1 = Noticias(1, "Michael Jackson cria perfil em rede social e vive vida tranquila no interior do Mato Grosso", "Vivinho da Silva", "Há 14 horas.", """Michael Jackson surpreende a todos ao ressurgir no interior do Mato Grosso, onde vive em segredo como um agricultor anônimo! Criando um perfil em uma rede social, ele compartilha sua vida tranquila, cultivando melancias e ensinando os moradores a dançar o "Moonwalk". “Aqui, sou só mais um cara comum!”, diz ele, enquanto postava selfies com chapéu de palha e bota, longe dos holofotes e das polêmicas. O Rei do Pop está de volta, e ninguém sabia!""", "famosos", "Beyoncé Giselle Knowles-Carter", """ Após anos de especulação e teorias da conspiração, uma das notícias mais chocantes do século acaba de ser divulgada: Michael Jackson, o Rei do Pop, foi encontrado vivo no interior do Mato Grosso! A descoberta surpreendeu fãs e admiradores ao redor do mundo, que nunca deixaram de acreditar que ele poderia ainda estar entre nós.

A notícia começou a circular quando um grupo de turistas visitou uma pequena fazenda na zona rural e encontrou um homem que se parecia exatamente com o ícone da música. Vestindo um chapéu de palha, botas de couro e rodeado por melancias, o “misterioso agricultor” se apresentou como Michael. Os turistas não acreditaram no que viam e logo começaram a filmar e compartilhar nas redes sociais, causando uma onda de incredulidade.

“Eu só queria viver em paz, longe das câmeras e da pressão da fama”, disse Michael em uma entrevista exclusiva. “Aqui, posso cultivar minhas melancias e ensinar os moradores a dançar o ‘Moonwalk’ sem ninguém me incomodar.” Os fãs em todo o mundo foram à loucura ao ouvir a notícia, enquanto alguns expressaram seu ceticismo.

Pessoas de todas as idades e de todos os cantos do mundo começaram a chegar à fazenda para tentar ver o Rei do Pop ao vivo. “É um milagre! Eu sempre soube que ele não tinha partido”, comentou uma fã emocionada. “Agora eu posso finalmente dançar ao som de ‘Billie Jean’ com o verdadeiro Michael!”

Fontes próximas ao cantor afirmaram que a decisão de se afastar da vida pública foi feita após a pressão intensa da fama e a incessante atenção da mídia. “Ele queria um recomeço e encontrou isso aqui, longe de toda a agitação de Hollywood”, revelou um amigo próximo.

As redes sociais foram inundadas com hashtags como #MichaelEstáVivo e #ReiDoPopNoMato, enquanto teóricos da conspiração discutem a possibilidade de que ele tenha planejado tudo isso como uma forma de escapar do estrelato. O mistério e a mágica de Michael Jackson continuam a fascinar e intrigar seus fãs, que agora têm uma nova razão para celebrar.

A descoberta não apenas traz de volta o Rei do Pop, mas também levanta perguntas sobre o que realmente aconteceu nos anos anteriores. Uma coisa é certa: a música de Michael Jackson nunca deixará de viver, e agora, com ele de volta, o mundo pode aguardar novas surpresas!  """, "img/noticia1.png", 1)
Noticias2 = Noticias(2, """ Irritado com o momento do país, Ed Motta dispara: "Biri jum tchi pa birilum".   """, "Sem papas na língua!", "Há 1  hora.", "Entre risos e confusões, fãs se perguntam: seria um grito de protesto ou apenas uma nova dança? Ed sempre surpreende!", "entretenimento", "Chuu do Brasil News", """Em um raro momento de manifestação pública, o cantor e compositor Ed Motta usou suas redes sociais para expressar sua frustração com a situação atual do Brasil. Mas, como sempre, ele fez isso à sua maneira única e incompreensível, soltando uma frase que deixou os seguidores intrigados: "Biri jum tchi pa birilum".

Enquanto alguns se apressaram em buscar explicações, especulando que se tratava de uma mensagem cifrada ou um código cósmico, outros garantem que foi apenas um desabafo emocional em seu idioma próprio — algo entre o scat jazz e uma sessão de descompressão zen.

Nas respostas, fãs seguiram a vibe, com comentários como:

“Bro, feeling it! Total birilum mood hoje.”
“Esse governo é só tchi tchi e nada de jum...”
“Biri jum tchi pa, meu presidente seria melhor que qualquer um aí.”
Fontes próximas ao artista afirmam que Ed estava degustando uma safra especial de vinho francês quando a frase foi publicada, o que pode ter contribuído para a fluidez criativa. Boatos indicam também que ele teria recusado pedidos para explicar a frase, alegando: "Se você não entendeu, é porque nunca ouviu jazz de verdade".

Especialistas em semiótica tentaram decodificar o desabafo, mas até agora ninguém chegou a um consenso. Um professor da USP, após horas analisando, concluiu: "A resposta pode estar no groove. Ou talvez em Paris".

No entanto, o próprio Ed voltou horas depois para acalmar seus fãs e declarou em outra postagem:
“Não é para entender com a mente, é para sentir com a alma. Às vezes, a vida é só um grande biri jum tchi pa birilum."

E, assim, com uma mistura de filosofia e nonsense, Ed Motta segue sendo incompreensível, inigualável e, principalmente, sempre no ritmo certo — seja lá qual ele for.""", "img/noticia2.png", 2)
Noticias3 = Noticias(3, """ UA comenta sensação de voltar a se chamar 'Xuxa' após desbloqueio do 'X' no Brasil: "Um alívio!". """, "Xuxa voltou!", "Há 2 horas.", """ UA comemora em grande estilo! Com o desbloqueio do 'X' no Brasil, a eterna Rainha dos Baixinhos volta a ser 'Xuxa' e não consegue conter a alegria: "Finalmente! não aguentava mais"- Diz, agora, Xuxa """, "famosos", "Beyoncé Giselle Knowles-Carter", """ Após semanas de expectativa, o tão aguardado desbloqueio da rede social X (antigo Twitter) no Brasil finalmente aconteceu, e ninguém está mais animado do que UA, a famosa apresentadora que, como muitos brasileiros, estava ansiosa para voltar a se chamar 'Xuxa'. Em uma coletiva de imprensa improvisada, UA não hesitou em compartilhar sua alegria: “É um alívio! Finalmente posso voltar a ser a Xuxa que todos conhecem!”.

Em meio a risadas, a artista não só comemorou o retorno do seu nome icônico, mas também fez questão de incluir a letra “X” em seu discurso, de forma quase poética. “A letra X é como um amigo que voltou de uma longa viagem — e agora, está aqui, brilhando mais do que nunca!”, exclamou, enquanto fazia uma pose dramaticamente exagerada.

UA também aproveitou a oportunidade para criticar a situação anterior, onde o ‘X’ estava bloqueado no Brasil. “Era como viver em um mundo sem cores! Sem a letra 'X', eu me sentia apenas UA, como se fosse uma versão inacabada de mim mesma. Agora posso brilhar de novo!”, disse, piscando para a câmera.

Com um toque de nostalgia, UA ainda brincou sobre como os fãs sentiam falta do nome e o impacto que isso teve em suas lives. “Se a rede social fosse um show, seria como tocar sem os meus instrumentos! Ninguém estava conseguindo entender o que eu estava dizendo: ‘UÁ, não é isso que você está pensando!’. Agora, tudo faz sentido!”

E como se a vida não estivesse cheia de surpresas, UA até anunciou uma nova fase na carreira: um novo álbum, “De Volta ao X”, onde ela promete trazer de volta os clássicos de sua carreira com letras que fazem referência a essa nova liberdade. “Quem diria que o ‘X’ ia ser tão importante na minha vida? A letra é como um bom vinho: só melhora com o tempo!”, afirmou ela, enquanto se preparava para gravar um novo clipe com uma coreografia que envolvia muitos 'Xs'.

Enquanto o Brasil celebra o desbloqueio da rede social X e o retorno triunfante de UA como 'Xuxa', os fãs se preparam para um revival épico e repleto de boas risadas. Afinal, no mundo das redes sociais, um “X” pode fazer toda a diferença! E quem melhor para representar essa volta por cima do que a eterna Rainha dos Baixinhos? Que comece a festa! """, "img/noticia3.png", 1)
Noticias4 = Noticias(4, "BOMBA! Raça, da banda Raça Negra se pronuncia sobre o caso Diddy:", "Diddy ie, Di-Diddy ie ie, Diddy Diddy ie", "3 dias atrás.", "Diddy ie, Di-Diddy ie, e Agora?", "entretenimento", "Chuu do Brasil News", """ Em um reviravolta surpreendente no mundo da música, a banda Raça Negra se viu no centro de uma polêmica envolvendo o rapper P. Diddy, que está enfrentando graves acusações de comportamentos inadequados. Informações recentes sugerem que a banda pode ter uma conexão com o caso, levando à indignação entre os fãs e à necessidade de esclarecimentos urgentes.

O vocalista da banda, conhecido por sua postura ética e compromisso com causas sociais, fez uma declaração oficial para desmentir as alegações. "Estamos profundamente chocados com o que está acontecendo. A Raça Negra nunca esteve envolvida em nenhuma atividade que pudesse ser considerada inapropriada ou antiética. A música sempre foi nossa forma de unir as pessoas e promover a positividade", disse ele em uma coletiva de imprensa.

Durante a declaração, o cantor enfatizou a importância de separar a música do comportamento pessoal de artistas. "Não podemos permitir que uma controvérsia envolvendo uma pessoa obscureça o trabalho de todos os artistas que lutam por um mundo melhor. A Raça Negra sempre defendeu a inclusão e a alegria, e estamos comprometidos em continuar fazendo isso, independentemente das circunstâncias."

A banda também anunciou que tomará medidas legais para proteger seu nome e reputação. "Não aceitamos ser arrastados para essa situação. Vamos lutar para que nossa imagem seja restaurada e continuaremos a fazer música que inspira e eleva as pessoas", afirmou o vocalista.

A comunidade musical e os fãs estão em alvoroço, debatendo sobre as implicações dessas acusações e o impacto que isso pode ter na carreira da banda. Enquanto isso, Raça Negra se prepara para lançar um novo álbum, com a esperança de que a música fale mais alto do que qualquer controvérsia.

A situação continua a se desenrolar, e todos os olhos estão voltados para a Raça Negra, que prometeu esclarecer qualquer mal-entendido e reafirmar seu compromisso com a música e a integridade. """, "img/noticia4.png", 2)

noticiasList = [Noticias1, Noticias2, Noticias3, Noticias4]


app = Flask(__name__)

@app.route("/")
def home():
        noticiasRecentes = noticiasList[1:3]
        return render_template("index.html", noticias = noticiasRecentes, jornalistasList = jornalistasList, noticiasList = noticiasList)


@app.route("/noticias/<int:id>")
def noticia(id):
        for noticia in noticiasList:
                if noticia.get_id() == id:
                        return render_template("noticias.html", noticia = noticia)
        return '<h1>Ops! Nenhuma notícia encontrada!</h1>'

@app.route("/jornalistas/<int:id>")
def jornalista(id):
       for jornalista in jornalistasList:
              if jornalista.get_id() == id:
                noticiasDoJornalista = [
                        noticia for noticia in noticiasList if noticia.get_jornalista() == jornalista.nome
                     ]
                return render_template("jornalistas.html", jornalista = jornalista, noticias = noticiasDoJornalista)



if __name__ == '__main__':
    app.run(debug=True)

