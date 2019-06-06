import pygame

pygame.init()
pygame.font.init()        

def main():
    vivo = True
    chave = False
    audio_vit = True
    som_bomb = True
    def colisao(matriz,sup,x,y,tela,cv):
        if matriz[x][y] == 'b' :
            sup.blit(bomba_img, (y*25,x*25,25,25))
            font_padrao = pygame.font.get_default_font()
            fonte_bomba = pygame.font.SysFont(font_padrao, 45)
            text = fonte_bomba.render('Você Morreu', 1, (0,0,0))
            tela.blit(text,(0,0))
            return False,cv
        elif matriz[x][y] == 'f':
            matriz[x][y] = 's'
            return True,cv
        elif matriz[x][y] == 't':
            matriz[x][y] = 's'
            return True,True
        elif matriz[x][y] == 'c':
            if cv == True :
                font_padrao = pygame.font.get_default_font()
                fonte_ganhou = pygame.font.SysFont(font_padrao, 45)
                text = fonte_ganhou.render('Você Ganhou', 1, (0,0,0))
                tela.blit(text,(0,0))
                return False,True
            else :
                font_padrao = pygame.font.get_default_font()
                fonte_perdeu = pygame.font.SysFont(font_padrao, 45)
                text = fonte_perdeu.render('Chave errada! TROLEI!!!!', 1, (0,0,0))
                tela.blit(text,(0,0))
        
        return True,cv

    #pygame.init()
    tela = pygame.display.set_mode([1001,651])
    pygame.display.set_caption("Hell's Escape")
    relogio = pygame.time.Clock()
    cor_preto = (0,0,0)
    cor_branco = (255,255,255)
    cor_azul = (110,190,230)
    cor_verde = (140,0,0)
    cor_vermelho = (136,0,0)
    cor_amarelo = (218,226,65)

    sup = pygame.Surface((875,525))
    sup.fill(cor_verde)

    reiniciar = pygame.Rect(450,609,116,36)

    portao_img = pygame.image.load("portao.png").convert_alpha()
    bomba_img = pygame.image.load("bomba.png").convert_alpha()
    chave_img = pygame.image.load("chave.png").convert_alpha()

    personagem_img = pygame.image.load("personagem.png").convert_alpha()
    pix_x, pix_y = 0, 25
    sup.blit(personagem_img, (pix_y, pix_x))

    

    #personagem = pygame.Rect(88,78,25,25)
    matriz =    [#1  2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35
                [10,'s', 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,'c', 10],#1-
                [10,'s', 10,'s','s','s','s','s', 10,'s','s','s','s','s','s','s','s','s', 10,'t', 10,'s','s','s','s','s','s','s','s','s','s','s', 10,'s', 10],#2-
                [10,'s', 10,'s', 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,'s', 10,'s', 10,'s', 10, 10, 10,'s', 10,'s', 10, 10, 10, 10, 10,'s', 10,'s', 10],#3-
                [10,'s','s','s', 10,'s','s','s','s','s','s','s','s','s', 10,'s', 10,'s', 10,'s', 10,'s', 10,'s', 10,'s','s','s', 10,'s','b','s','s','s', 10],#4-
                [10,'s', 10, 10, 10, 10, 10, 10, 10,'s', 10,'s', 10,'s', 10,'s', 10,'s', 10,'s', 10,'s', 10,'s', 10, 10, 10,'s', 10,'s', 10, 10, 10,'s', 10],#5-
                [10,'s','s','s', 10,'s','s','s','s','s', 10,'s', 10,'s','s','s', 10,'s','s','s', 10,'s','s','s','s','s', 10,'s', 10,'s', 10,'s', 10,'s', 10],#6-
                [10, 10, 10,'s', 10,'s', 10, 10, 10, 10, 10,'s', 10,'s', 10, 10, 10,'b', 10, 10, 10, 10, 10,'s', 10,'s', 10,'s', 10,'s', 10,'s', 10, 10, 10],#7-
                [10,'s','s','s', 10,'s','s','s','s','s', 10,'s', 10,'s','s','s','s','s','s','s','s','s', 10,'s', 10,'s', 10,'s','s','s','s','s', 10,'s', 10],#8-
                [10,'s', 10, 10, 10, 10, 10, 10, 10,'s', 10,'s', 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,'s', 10,'s', 10, 10, 10, 10, 10,'s', 10,'s', 10],#9-
                [10,'s','s','s', 10,'s','s','s','s','s', 10,'f','s','s','s','s','s','s', 10,'s','s','s','s','s', 10,'s', 10,'s','s','s', 10,'s','s','s', 10],#10-
                [10,'s', 10,'s', 10,'s', 10, 10, 10, 10, 10,'s', 10, 10, 10, 10, 10,'s', 10,'s', 10, 10, 10, 10, 10,'s', 10,'s', 10, 10, 10, 10, 10,'s', 10],#11-
                [10,'s', 10,'s', 10,'s', 10,'s','s','f', 10,'s','s','s','s','s', 10,'s', 10,'s','s','s','s','s','s','s', 10,'s','s','s','s','s','s','s', 10],#12-
                [10,'s', 10,'s', 10,'s', 10,'s', 10, 10, 10, 10, 10, 10, 10, 10, 10,'s', 10, 10, 10, 10, 10, 10, 10, 10, 10,'s', 10, 10, 10, 10, 10, 10, 10],#13-
                [10,'s', 10,'s','s','s', 10,'s', 10,'s','s','s','s','s','s','s', 10,'s', 10,'s','s','s','s','s','s','s','s','s','s','s','s','s', 10,'s', 10],#14-
                [10,'s', 10, 10, 10, 10, 10,'s', 10,'s', 10, 10, 10,'s', 10,'s', 10,'s', 10, 10, 10, 10, 10,'s', 10, 10, 10, 10, 10,'s', 10, 10, 10,'s', 10],#15-
                [10,'s','s','s', 10,'s', 10,'s', 10,'s', 10,'s','s','s', 10,'s', 10,'s','s','s','s','s', 10,'s', 10,'s','s','s','s','s', 10,'s','s','s', 10],#16-
                [10,'s', 10, 10, 10,'s', 10,'s', 10,'b', 10,'s', 10,'s', 10,'s', 10,'s', 10, 10, 10, 10, 10,'s', 10,'s', 10, 10, 10,'s', 10,'s', 10, 10, 10],#17-
                [10,'s', 10,'s','s','b', 10,'s','s','s', 10,'b', 10,'s', 10,'s', 10,'s', 10,'s','s','s','s','b', 10,'s', 10,'s', 10,'s', 10,'s','s','s', 10],#18-
                [10,'s', 10, 10, 10,'s', 10, 10, 10,'s', 10, 10, 10,'s', 10,'s', 10,'s', 10,'s', 10, 10, 10, 10, 10,'s', 10,'s', 10,'s', 10, 10, 10,'s', 10],#19-
                [10,'s','s','s','s','s','s','s', 10,'s','s','s','s','s', 10,'s','s','s','s','s','s','s','s','s','s','s', 10,'s','s','s','s','s','s','s', 10],#20
                [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],#21
                ]

    pos_personagem_x = 0
    pos_personagem_y = 1
    #setando o labirinto

    

    pygame.mixer.music.load('Toxic Waste Music.ogg')
    pygame.mixer.music.play(-1)
    audio_btpar = pygame.mixer.Sound('thaan.ogg')
    audio_vt = pygame.mixer.Sound('Yeahh.ogg')
    audio_bomba = pygame.mixer.Sound('SOM DE EXPLOSAO.ogg')

    font_bot = pygame.font.get_default_font()
    fonte_rei = pygame.font.SysFont(font_bot, 35)
    text_rei = fonte_rei.render('Reiniciar', 1, (255,255,255))
    

    sair = False

    while sair == False :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()
                if 450 <= pos_mouse[0] <= 566 :
                    if 609 <= pos_mouse[1] <= 645 :
                        vivo = True
                        chave = False
                        audio_vit = True
                        som_bomb = True
                        pos_personagem_x = 0
                        pos_personagem_y = 1
                        pix_x, pix_y = 0, 25
                        matriz[1][19] = 't'
                        matriz[9][11] = 'f'
                        matriz[11][9] = 'f'

            if event.type == pygame.KEYDOWN and vivo == True:
                if event.key == pygame.K_LEFT:
                    if matriz[pos_personagem_x][pos_personagem_y - 1] != 10:
                        pix_y -= 25
                        #personagem.move_ip(-25,0)
                        pos_personagem_y -= 1
                    else :
                        audio_btpar.play()
                if event.key == pygame.K_RIGHT:
                    if matriz[pos_personagem_x][pos_personagem_y + 1] != 10:
                        pix_y += 25
                        #personagem.move_ip(25,0)
                        pos_personagem_y += 1
                    else :
                        audio_btpar.play()
                if event.key == pygame.K_UP:
                    if matriz[pos_personagem_x -1][pos_personagem_y] != 10:
                        pix_x -= 25
                        #personagem.move_ip(0,-25)
                        pos_personagem_x -= 1
                    else :
                        audio_btpar.play()
                if event.key == pygame.K_DOWN:
                    if matriz[pos_personagem_x + 1][pos_personagem_y] != 10:
                        pix_x += 25
                        #personagem.move_ip(0,25)
                        pos_personagem_x += 1
                    else :
                        audio_btpar.play()
                


             
        
        tela.fill(cor_branco)
        tela.blit(sup,[63,78])
        
        
        #pygame.draw.rect(tela, cor_azul, personagem)

        for x in range(0,len(matriz)):
            for y in range(0,len(matriz[x])):
                if matriz[x][y] == 10 :
                    pygame.draw.rect(sup,cor_preto,(y*25,x*25,25,25))
                else:
                    if matriz[x][y] == 's':
                        pygame.draw.rect(sup,cor_verde,(y*25,x*25,25,25))
                    elif matriz[x][y] == 'c':
                        pygame.draw.rect(sup,cor_verde,(y*25,x*25,25,25))
                        sup.blit(portao_img, (y*25,x*25,25,25))
                    elif matriz[x][y] == 'b':
                        pygame.draw.rect(sup,cor_verde,(y*25,x*25,25,25))
                        #sup.blit(bomba_img, (y*25,x*25,25,25))
                    elif matriz[x][y] == 'f' or matriz[x][y] == 't':
                        pygame.draw.rect(sup,cor_verde,(y*25,x*25,25,25))
                        sup.blit(chave_img, (y*25,x*25,25,25))

        
        sup.blit(personagem_img, (pix_y, pix_x))
        pygame.draw.rect(tela,cor_vermelho,reiniciar)
        tela.blit(text_rei,(455,615))
        vivo,chave = colisao(matriz,sup,pos_personagem_x,pos_personagem_y,tela,chave)
        if pos_personagem_x == 0 and pos_personagem_y == 33 :
            if chave == True and audio_vit == True:
                audio_vt.play()
                audio_vit = False
        if matriz[pos_personagem_x][pos_personagem_y] == 'b' :
            if som_bomb == True:
                audio_bomba.play()
                som_bomb = False
                
                
        
        pygame.display.update()
        relogio.tick(30)


    pygame.quit()

    
main()
