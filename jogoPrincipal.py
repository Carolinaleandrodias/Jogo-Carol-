from random import random
import random
from colisão import *
from graphics import *


win = GraphWin(("Menina2.0"), 800, 600, autoflush=False) 

#sortear as bolhas, assim elas não vão cair em apenas uma sequência e sim sorteadas 
def bolas(win):
    
    sorteioX = [random.randint(50,750)]
    bolaX = random.choice(sorteioX)
    bolaY = -20

    bola = Image(Point(bolaX , bolaY),"bubble1.png")
    bola.draw(win)
    larguraBola = bola.getWidth()
    circulo_bola = Circle(Point(bola.getAnchor().getX(), bola.getAnchor().getY()), larguraBola/2 )
    #circulo_bola.draw(win)

    return bola , circulo_bola

#sortear as facas, elas vão cair com o objetivo de que o jogador perca suas vidas
def facas(win):
    
    sorteioX = [random.randint(50,750)]
    facaX = random.choice(sorteioX)
    facaY = -50

    faca = Image(Point(facaX , facaY), "faca.png")
    faca.draw(win)
    larguraFaca = faca.getWidth()
    circulo_faca = Circle(Point(faca.getAnchor().getX(), faca.getAnchor().getY()), larguraFaca/2 )
    #circulo_faca.draw(win)

    return faca , circulo_faca


#sortear as moedas 
def moedas(win):
    
    sorteioX = [random.randint(50,750)]
    moedaX = random.choice(sorteioX)
    moedaY = -10

    moeda = Image(Point(moedaX , moedaY),"moeda1.png")
    moeda.draw(win)
    larguramoeda = moeda.getWidth()
    circulo_moeda = Circle(Point(moeda.getAnchor().getX(), moeda.getAnchor().getY()), larguramoeda/2 )
    #circulo_moeda.draw(win)

    return moeda , circulo_moeda
  
key = 0
tela_inicio = Image(Point(400,300),"tela2.png")
tela_inicio.draw(win)


while key != "Return":
    key = win.checkKey()
    if key == "Return":
        tela_inicio.undraw()
    

#aqui são as imagens do meu personagem 
parado = ["Idle2 (1).png"]


correndoDir = ["Run1.png", "Run2.png", "Run3.png", "Run4.png", "Run5.png"]
tamCorrendoDir = len(correndoDir)

correndoEsq = ["Idle2Esq1.png", "RunEsq1.png", "RunEsq2.png", "RunEsq3.png", "RunEsq4.png", "RunEsq5.png"]
tamCorrendoEsq = len(correndoEsq)

morrendo = ["Dead1 (3).png", "Dead2.png","Dead3.png","Dead4.png","Dead5.png","Dead6.png"]

#desenha o fundo
imagem = Image(Point(400, 300),"ceu800.png")
imagem.draw(win)

#desenho do circulo da menina 
i = 0
menina = Image(Point(400,450), parado[i])
menina.draw(win)
larguraMenina = menina.getWidth()
circulo_menina= Circle(Point(menina.getAnchor().getX() - 5 , menina.getAnchor().getY()), larguraMenina/3 )
#circulo_menina.draw(win)

#imagem do coração de vida na tela
coração = Image(Point(760,560),"coração1.png")
coração.draw(win)
 

#aqui mostra a tabela de pontos no jogo
pontuacao = 1 
contador = "0"
contador_moedas = Text(Point(110,80), "Seus pontos: " + contador)
contador_moedas.setSize(20)
contador_moedas.setFace("times roman")
contador_moedas.draw(win)

#contador de vida, fonte, tam dos números 
contador_vida = 0
vidaMenina = 5
imagemVida = "5"
vida = Text(Point(760,560), imagemVida)
vida.setSize(20)
vida.setFace("times roman")
vida.draw(win)

#chamando a função - bolas 
bola , circulo_bola = bolas(win)  

#chamando a função - facas
faca , circulo_faca = facas(win)

#chamando a função - moedas
moeda , circulo_moeda = moedas(win)

velYBola = 0.5
z = 0
retornar = 0 
sair = 0

#opção para sair do jogo 
key = win.checkKey()
while sair != 1: 
    velX = 20

    
    if key == "Escape":
            sair = 1
    
#coordenadas da menina 
    raio_menina = circulo_menina.getRadius()
    circulo_meninaX = circulo_menina.getCenter().getX()
    circulo_meninaY = circulo_menina.getCenter().getY()
        
#coordenadas da bola
    raio_bola = circulo_bola.getRadius()
    circulo_bolaX = circulo_bola.getCenter().getX()
    circulo_bolaY = circulo_bola.getCenter().getY()

#coordenadas da faca
    raio_objeto = circulo_faca.getRadius()
    circulo_objetoX = circulo_faca.getCenter().getX()
    circulo_objetoY = circulo_faca.getCenter().getY()

#coordenadas da moeda
    raio_moeda = circulo_moeda.getRadius()
    circulo_moedaX = circulo_moeda.getCenter().getX()
    circulo_moedaY = circulo_moeda.getCenter().getY()


    bola.move(0,velYBola)
    circulo_bola.move(0,velYBola)
    bolaY = bola.getAnchor().getY()
    if bolaY >= 650:
        bola.move(0,velYBola)
        circulo_bola.move(0,velYBola)
        bola , circulo_bola = bolas(win)

#colisão 
    #(radius1, radius2, X1 , X2 , Y1, Y2):
    if colidiu (raio_bola, raio_menina, circulo_bolaX, circulo_meninaX, circulo_bolaY, circulo_meninaY):
        bola.move(1000, 1000)
        circulo_bola.move(1000, 1000)
        vida.undraw()
        vidaMenina -= 1
        imagemVida = "" + str(vidaMenina)
        vida = Text(Point(760,560), "" + imagemVida)
        vida.setSize(20)
        vida.setFace("times roman")
        vida.draw(win)
        contador_vida = contador_vida + 1


    if pontuacao >= 2:
        faca.move(0,velYBola)
        circulo_faca.move(0,velYBola)
        facaY = faca.getAnchor().getY()
        if facaY >= 650:
            faca.move(0,velYBola)
            circulo_faca.move(0,velYBola)
            faca , circulo_faca = facas(win)
        

    #(radius1, radius2, X1 , X2 , Y1, Y2):
    if colidiu (raio_objeto, raio_menina, circulo_objetoX, circulo_meninaX, circulo_objetoY, circulo_meninaY):
        faca.move(1000, 1000)
        circulo_faca.move(1000, 1000)
        vida.undraw()
        vidaMenina -= 1
        imagemVida = "" + str(vidaMenina)
        vida = Text(Point(760,560), "" + imagemVida)
        vida.setSize(20)
        vida.setFace("times roman")
        vida.draw(win)
        contador_vida = contador_vida + 1


        
 

    moeda.move(0,velYBola)
    circulo_moeda.move(0,velYBola)
    moedaY = moeda.getAnchor().getY()

    if moedaY > 650:
        moeda , circulo_moeda = moedas(win)

    
    if colidiu (raio_moeda, raio_menina, circulo_moedaX, circulo_meninaX, circulo_moedaY, circulo_meninaY):
        moeda.move(1000, 1000)
        circulo_moeda.move(1000, 1000)
        contador_moedas.undraw()
        contador = "" + str(pontuacao)
        contador_moedas = Text(Point(110,80), "Seus pontos: " + contador)
        contador_moedas.setSize(20)
        contador_moedas.setFace("times roman")
        contador_moedas.draw(win)
        pontuacao += 1
        
        

    if contador_vida >= 6:
        #menina morre
        menina.move(0,0)
        while z <= len(morrendo) - 1:
            centroMenina = menina.getAnchor()
            menina.undraw()
            menina = Image(centroMenina,morrendo[z])
            menina.draw(win)
            z += 1
        

#tempo em que os objetos aparecem na tela
    if pontuacao >= 1:
        velYBola = 0.2
      
    if pontuacao >= 7:
        velYBola = 0.3

    if pontuacao >= 9:
        velYBola = 0.3
    
    #condição para vencer   
    if pontuacao >= 11:
        menina.move(1000,1000)
        bola.move(1000,1000)
        moeda.move(1000,1000)
        venceu = Image(Point(400,300),"venceu.png")
        venceu.draw(win)
        mensagemSair = Text(Point(400,500), "")
        mensagemSair.setSize(20)
        mensagemSair.setFace("helvetica")
        mensagemSair.draw(win)



    #condição para perder
    if contador_vida >= 5:
        #menina.move(1000,1000)
        contador_moedas.undraw()
        bola.move(1000,1000)
        moeda.move(1000,1000)
        perdeu = Image(Point(400,300),"perdeu.png")
        perdeu.draw(win)
        mensagemSair = Text(Point(400,250), "")
        mensagemSair.setSize(20)
        mensagemSair.setFace("helvetica")
        mensagemSair.draw(win)

#direção para direita
    if key == "Right" and contador_vida <= 4:
        i = (i + 1) % tamCorrendoDir
        centroMenina = menina.getAnchor()
        menina.undraw()
        menina = Image(centroMenina,correndoDir[i])
        menina.draw(win)

        if circulo_meninaX + 50 >= 800:
            menina.move(0,0)
            circulo_menina.move(0,0)
        else:
            menina.move(velX , 0)
            circulo_menina.move(velX,0)

    elif key == "Left"  and contador_vida <= 4:
        i = (i + 1) % tamCorrendoEsq 
        centroMenina = menina.getAnchor()
        menina.undraw()
        menina = Image(centroMenina,correndoEsq[i])
        menina.draw(win)
        if circulo_meninaX - 50 <= 0:
            menina.move(0,0)
            circulo_menina.move(0,0)

        else:
            menina.move(-velX , 0) 
            circulo_menina.move(-velX , 0) 
    

    if contador_vida >= 5 or pontuacao >= 11 :
        #sair do jogo
        if key == "Escape":
            sair = 1

        

    key = win.checkKey()

