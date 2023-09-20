import pygame,sys
from pygame.locals import *
from Card import *
from BlackJackDeck import *
from Bet import *

pygame.init()
screen=pygame.display.set_mode((800,600))

font=pygame.font.Font('freesansbold.ttf',32)
tryAgain=button((150,170,255),500,400,150,50,"Play again")

dealerPool=Bet(750,250)
playerPool=Bet(750,250)

def start(pBet, dBet):
    deck=BlackJackDeck()
    deck.shuffle()
    deck.shuffle()
    deck.shuffle()
    deck.shuffle()
    count=3
    end=True
    #win condition booleans
    bustD=False
    bustP=False
    pWins=False
    dWins=False

    bet=False
    pMoneyGone=False
    dMoneyGone=False
    #starting card numbers
    dealerFirst=28
    playerFirst=2

    #hands
    player=[]
    dealer=[]

    num=1

    #card positions
    dealerPos=200
    playerPos=200

    #player cards
    player.append(deck.card_list[0])
    player.append(deck.card_list[1])

    dealer.append(deck.card_list[26])
    deck.card_list[26].flip()
    dealer.append(deck.card_list[27])

    #score
    playerScore=player[0].point_value+player[1].point_value
    dealerScore=dealer[0].point_value+dealer[1].point_value




    while end:
        if bustP==True:
            for i in range(len(player)):
                if player[i].point_value==11:
                    player[i].point_value=1
                    bustP=False
        mousePos=pygame.mouse.get_pos()
        screen.fill((53,130,77))

        #buttons
        standButton=button((150,170,255),400,50,150,50,"Stand")
        hitButton=button((255,150,150),600,50,150,50,"Hit")

        betButton=button((0,255,0), 600,300,150,50,"Bet")

        #changes color if hovering over
        if standButton.isOver(mousePos):
            standButton.color=(0,0,255)
        else:
            standButton.color=(150,170,255)
            
        if hitButton.isOver(mousePos):
            hitButton.color=(255,0,0)
        else:
            hitButton.color=(255,150,150)

        if betButton.isOver(mousePos) and len(player)==2:
            betButton.color=(0,255,0)
        else:
            betButton.color=(150,255,150)

        if bet==True:
            betButton.color=(255,0,0)

        standButton.draw(screen)
        hitButton.draw(screen)
        if pWins==False and dWins==False and bustD==False and bustP==False:
            betButton.draw(screen)
        

        #text
        text=font.render("Player Cards: "+str(playerScore),True,(255,255,255))
        text2=font.render("Dealer Cards ",True,(255,255,255))

        pWin=font.render("Player Wins with a score of: "+str(playerScore),True,(0,0,0),(137,207,240))
        dWin=font.render("Dealer Wins with a score of: "+str(dealerScore),True,(0,0,0),(137,207,240))
        dScore=font.render("Dealer Score: " + str(dealerScore),True,(0,0,0),(137,207,240))
        pScore=font.render("Player Score: " + str(dealerScore),True,(0,0,0),(137,207,240))
        if pBet.pool!=0:
            pMoney=font.render("Money: " + str(len(pBet)), True, (0,0,0))
        elif pBet.pool==0:
            pMoney=font.render("Money: " + str(len(pBet)), True, (255,0,0))

        
        pPoor=font.render("Player loses. Out of money", True, (255,0,0))
        dPoor=font.render("Dealer loses. Out of money", True, (255,0,0))
            
        if bustD==True:
            screen.blit(endD,(200,200))
            screen.blit(pWin,(200,250))
            text2=font.render("Dealer Cards: "+str(dealerScore),True,(255,255,255))
            tryAgain.draw(screen)
        if (bustD==True or pWins==True) and bet==True:
            pBet.winBet(dBet)
            dBet.loseBet(pBet)
            bet=False
        if bustP==True:
            screen.blit(endP,(200,200))
            screen.blit(dWin,(00,250))
            text2=font.render("Dealer Cards: "+str(dealerScore),True,(255,255,255))
            tryAgain.draw(screen)
        if (bustP==True or dWins==True) and bet==True:
            dBet.winBet(pBet)
            pBet.loseBet(dBet)
            bet=False


        #keeping cards displayed

        for i in range(len(player)):
            player[i].draw(screen, 50+i*50, 100)

        for i in range(len(dealer)):
            dealer[i].draw(screen, 50+i*50, 400)
            
        #drawing player and dealer score                  
        screen.blit(text,(5,50))
        screen.blit(text2,(5,350))

        screen.blit(pMoney, (500,5))

        
        if playerScore>21:
            endP=font.render("Player Busts",True,(0,0,0),(137,207,240))
            pWin=font.render("Player Wins, Dealer Busts",True,(0,0,0),(137,207,240))
            bustP=True
            text2=font.render("Dealer Cards: "+str(dealerScore),True,(255,255,255))
            tryAgain.draw(screen)
            if num==1:
                dealer[0].flip()
                num+=1
            
        if dealerScore>21:
            endD=font.render("Dealer Busts",True,(0,0,0),(137,207,240))
            dWin=font.render("Dealer Wins, Player Busts",True,(0,0,0),(137,207,240))
            bustD=True
            text2=font.render("Dealer Cards: "+str(dealerScore),True,(255,255,255))
            tryAgain.draw(screen)
            if num==1:
                dealer[0].flip()
                num+=1

        if dWins==True:
            screen.blit(dWin,(200,200))
            text2=font.render("Dealer Cards: "+str(dealerScore),True,(255,255,255))
            tryAgain.draw(screen)


        if pWins==True:
            screen.blit(pWin,(200,200))
            text2=font.render("Dealer Cards: "+str(dealerScore),True,(255,255,255))
            tryAgain.draw(screen)

        if pMoneyGone==True:
            screen.blit(pPoor, (350,125))

        if dMoneyGone==True:
            screen.blit(dPoor, (350,125))
        if pBet.pool==0:
            pMoneyGone=True
        elif dBet.pool==0:
            dMoneyGone=True



        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key==K_ESCAPE):
                end=False
                pygame.quit()
                
            #flips cards in order
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if betButton.isOver(mousePos):
                    if len(player)==2:
                        bet=True
                if tryAgain.isOver(mousePos) and (bustP==True or bustD==True or pWins==True or dWins==True):
                    if pBet.pool!=0:
                        start(dealerPool, playerPool)
                    elif dBet.pool!=0:
                        start(dealerPool, playerPool)
                if hitButton.isOver(mousePos) and pWins==False and dWins==False:
                    if playerScore<21 and bustD==False:
                        player.append(deck.card_list[playerFirst])

                        pygame.display.update()
                        
                        playerFirst+=1
                        playerPos+=50

                        playerScore+=player[-1].point_value
            
                if standButton.isOver(mousePos) and pWins==False and dWins==False:
                    while(dealerScore<17 and bustD==False and bustP==False):
                        dealer.append(deck.card_list[dealerFirst])
                        dealerFirst+=1
                        dealerPos+=50

                        dealerScore+=dealer[-1].point_value
                        if dealerScore>playerScore:
                            screen.blit(dWin,(200,200))
                            text2=font.render("Dealer Cards: "+str(dealerScore),True,(255,255,255))
                            if num==1:
                                dealer[0].flip()
                                num+=1
                        elif playerScore>dealerScore:
                            screen.blit(pWin,(200,200))
                            text2=font.render("Dealer Cards: "+str(dealerScore),True,(255,255,255))
                            if num==1:
                                dealer[0].flip()
                                num+=1



                    if dealerScore>playerScore and dealerScore<22 and playerScore<22:
                        dWins=True
                        text2=font.render("Dealer Cards: "+str(dealerScore),True,(255,255,255))
                        if num==1:
                                dealer[0].flip()
                                num+=1

                    if dealerScore<21 and playerScore<21:
                        if dealerScore>playerScore:
                            dWins=True
                            text2=font.render("Dealer Cards: "+str(dealerScore),True,(255,255,255))
                            if num==1:
                                dealer[0].flip()
                                num+=1
                        elif playerScore>dealerScore:
                            pWins=True
                            text2=font.render("Dealer Cards: "+str(dealerScore),True,(255,255,255))
                            if num==1:
                                dealer[0].flip()
                                num+=1
                        elif playerScore==dealerScore:
                            dWins=True
                            text2=font.render("Dealer Cards: "+str(dealerScore),True,(255,255,255))
                            if num==1:
                                dealer[0].flip()
                                num+=1
                    if dealerScore==playerScore:
                        dWins=True
                        text2=font.render("Dealer Cards: "+str(dealerScore),True,(255,255,255))
                        if num==1:
                            dealer[0].flip()
                            num+=1


                    if dealerScore>21:
                        dBust=True
                    if playerScore>21:
                        pBust=True

                    if playerScore==21 and dealerScore!=21:
                        pWins=True
                    if playerScore!=21 and dealerScore==21:
                        dWins=True
start(dealerPool, playerPool)
                    

                

                    



                    
        
                
