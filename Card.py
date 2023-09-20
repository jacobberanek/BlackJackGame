import pygame,sys,os
from pygame.locals import *

class Card():

    def __init__(self, rank, suit, point_value):
        self.rank = rank
        self.suit = suit
        self.point_value = point_value
        self.up=True
        self.back_image=pygame.image.load(os.path.join("Cards", "back.png"))
        
        if self.suit=="HEARTS":
            if self.rank=="ACE":
                self.front_image = pygame.image.load(os.path.join("Cards", "heartA.png"))
            if self.rank == "TWO":
                self.front_image = pygame.image.load(os.path.join("Cards", "heart2.png"))
            if self.rank == "THREE":
                self.front_image = pygame.image.load(os.path.join("Cards", "heart3.png"))
            if self.rank == "FOUR":
                self.front_image = pygame.image.load(os.path.join("Cards", "heart4.png"))
            if self.rank == "FIVE":
                self.front_image = pygame.image.load(os.path.join("Cards", "heart5.png"))
            if self.rank == "SIX":
                self.front_image = pygame.image.load(os.path.join("Cards", "heart6.png"))
            if self.rank == "SEVEN":
                self.front_image = pygame.image.load(os.path.join("Cards", "heart7.png"))
            if self.rank == "EIGHT":
                self.front_image = pygame.image.load(os.path.join("Cards", "heart8.png"))
            if self.rank == "NINE":
                self.front_image = pygame.image.load(os.path.join("Cards", "heart9.png"))
            if self.rank == "TEN":
                self.front_image = pygame.image.load(os.path.join("Cards", "heart10.png"))
            if self.rank == "JACK":
                self.front_image = pygame.image.load(os.path.join("Cards", "heartJ.png"))
            if self.rank == "KING":
                self.front_image = pygame.image.load(os.path.join("Cards", "heartK.png"))
            if self.rank == "QUEEN":
                self.front_image = pygame.image.load(os.path.join("Cards", "heartQ.png"))
        if self.suit=="SPADES":
            if self.rank=="ACE":
                self.front_image = pygame.image.load(os.path.join("Cards", "spadeA.png"))
            if self.rank == "TWO":
                self.front_image = pygame.image.load(os.path.join("Cards", "spade2.png"))
            if self.rank == "THREE":
                self.front_image = pygame.image.load(os.path.join("Cards", "spade3.png"))
            if self.rank == "FOUR":
                self.front_image = pygame.image.load(os.path.join("Cards", "spade4.png"))
            if self.rank == "FIVE":
                self.front_image = pygame.image.load(os.path.join("Cards", "spade5.png"))
            if self.rank == "SIX":
                self.front_image = pygame.image.load(os.path.join("Cards", "spade6.png"))
            if self.rank == "SEVEN":
                self.front_image = pygame.image.load(os.path.join("Cards", "spade7.png"))
            if self.rank == "EIGHT":
                self.front_image = pygame.image.load(os.path.join("Cards", "spade8.png"))
            if self.rank == "NINE":
                self.front_image = pygame.image.load(os.path.join("Cards", "spade9.png"))
            if self.rank == "TEN":
                self.front_image = pygame.image.load(os.path.join("Cards", "spade10.png"))
            if self.rank == "JACK":
                self.front_image = pygame.image.load(os.path.join("Cards", "spadeJ.png"))
            if self.rank == "KING":
                self.front_image = pygame.image.load(os.path.join("Cards", "spadeK.png"))
            if self.rank == "QUEEN":
                self.front_image = pygame.image.load(os.path.join("Cards", "spadeQ.png"))
        if self.suit=="DIAMONDS":
            if self.rank=="ACE":
                self.front_image = pygame.image.load(os.path.join("Cards", "diamondA.png"))
            if self.rank == "TWO":
                self.front_image = pygame.image.load(os.path.join("Cards", "diamond2.png"))
            if self.rank == "THREE":
                self.front_image = pygame.image.load(os.path.join("Cards", "diamond3.png"))
            if self.rank == "FOUR":
                self.front_image = pygame.image.load(os.path.join("Cards", "diamond4.png"))
            if self.rank == "FIVE":
                self.front_image = pygame.image.load(os.path.join("Cards", "diamond5.png"))
            if self.rank == "SIX":
                self.front_image = pygame.image.load(os.path.join("Cards", "diamond6.png"))
            if self.rank == "SEVEN":
                self.front_image = pygame.image.load(os.path.join("Cards", "diamond7.png"))
            if self.rank == "EIGHT":
                self.front_image = pygame.image.load(os.path.join("Cards", "diamond8.png"))
            if self.rank == "NINE":
                self.front_image = pygame.image.load(os.path.join("Cards", "diamond9.png"))
            if self.rank == "TEN":
                self.front_image = pygame.image.load(os.path.join("Cards", "diamond10.png"))
            if self.rank == "JACK":
                self.front_image = pygame.image.load(os.path.join("Cards", "diamondJ.png"))
            if self.rank == "KING":
                self.front_image = pygame.image.load(os.path.join("Cards", "diamondK.png"))
            if self.rank == "QUEEN":
                self.front_image = pygame.image.load(os.path.join("Cards", "diamondQ.png"))
        if self.suit=="CLUBS":
            if self.rank=="ACE":
                self.front_image = pygame.image.load(os.path.join("Cards", "clubA.png"))
            if self.rank == "TWO":
                self.front_image = pygame.image.load(os.path.join("Cards", "club2.png"))
            if self.rank == "THREE":
                self.front_image = pygame.image.load(os.path.join("Cards", "club3.png"))
            if self.rank == "FOUR":
                self.front_image = pygame.image.load(os.path.join("Cards", "club4.png"))
            if self.rank == "FIVE":
                self.front_image = pygame.image.load(os.path.join("Cards", "club5.png"))
            if self.rank == "SIX":
                self.front_image = pygame.image.load(os.path.join("Cards", "club6.png"))
            if self.rank == "SEVEN":
                self.front_image = pygame.image.load(os.path.join("Cards", "club7.png"))
            if self.rank == "EIGHT":
                self.front_image = pygame.image.load(os.path.join("Cards", "club8.png"))
            if self.rank == "NINE":
                self.front_image = pygame.image.load(os.path.join("Cards", "club9.png"))
            if self.rank == "TEN":
                self.front_image = pygame.image.load(os.path.join("Cards", "club10.png"))
            if self.rank == "JACK":
                self.front_image = pygame.image.load(os.path.join("Cards", "clubJ.png"))
            if self.rank == "KING":
                self.front_image = pygame.image.load(os.path.join("Cards", "clubK.png"))
            if self.rank == "QUEEN":
                self.front_image = pygame.image.load(os.path.join("Cards", "clubQ.png"))
             
    def __str__(self):
        return '{} of {} (Value = {})'.format(self.rank, self.suit, self.point_value)

    def change_ace(self):
        if self.rank == 'ACE':
            self.point_value = 11

    def equalTo(self, other):
        if self.rank == other.rank and self.suit == other.suit:
            return True
        return False

    def compareTo(self, other):
        if self.equalTo(other):
            return 0
        elif self.rank > other.rank:
            return 1
        elif self.rank < other.rank:
            return -1
        else:
            suits = ['SPADES', 'CLUBS', 'DIAMONDS', 'HEART']
            suit1 = suits.index(self.suit)
            suit2 = suits.index(other.suit)
            if suit1 > suit2:
                return 1
            else:
                return -1

    def draw(self,win,x,y):
        if self.up:
            win.blit(self.front_image,(x,y))
        else:
            win.blit(self.back_image,(x,y))
    def flip(self):
        if self.up==True:
            self.up=False
        elif self.up==False:
            self.up=True


class button():
    def __init__(self,color,x,y,width,height,text=''):
        self.color=color
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.text=text
    def draw(self,win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height),0)
        if self.text!='':
            font=pygame.font.SysFont('comicsans',32)
            text=font.render(self.text,1,(0,0,0))
            win.blit(text,(self.x +(self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
    def isOver(self,pos):
        if pos[0]>self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1]<self.y+self.height:
                return True
        return False
    
            
