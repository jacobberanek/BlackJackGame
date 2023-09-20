from Card import *
import random
class BlackJackDeck():
    
            
    def __init__(self):
        self.card_list=[]
        self.discard_list=[]

        suitList=["SPADES", "HEARTS", "DIAMONDS", "CLUBS"]
        rankList=["ACE","TWO",'THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE','TEN','JACK','QUEEN','KING']
        pointList=[11,2,3,4,5,6,7,8,9,10,10,10,10]
        x = 0
        for r in rankList:
            for s in suitList:
                (self.card_list).append(Card(r,s,pointList[x]))
            x += 1
        self.card_list=self.shuffle()
        
        
    def __str__(self):
        for i in self.card_list:
            print(i)
        return ""

    def print_discard(self):
        for i in self.discard_list:
            print(i)
        return ""

    def __len__(self):
        return len(self.card_list)

    def addtoDiscard(self, card):
        self.discard_list.append(card)
        self.card_list.remove(card)
        


    def shuffle(self):
        tempList=self.card_list.copy()
        randomList=[]
        tempList2=[]
        while len(tempList)!=0:
            randomInt=random.randint(0,len(tempList)-1)
            randomList.append(tempList[randomInt])
            tempList.pop(randomInt)
        return randomList


    
    def drawCard(self):
        if len(self.card_list)!=0:
            #print(self.card_list[0])
            #self.discard_list.append(self.card_list[0])
            return self.card_list.pop(0)
        else:
            self.card_list=[]
            print()
            print("End of deck \nReshuffling...")
            
            print()
            self.card_list=self.discard_list.copy()
            self.discard_list.clear()
            self.card_list= self.shuffle()
                
                
                
                
            
            
                  
            
            
