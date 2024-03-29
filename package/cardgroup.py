# Developer  : khademul Bari
# Github: https://github.com/tawhidi
# Email: tawhidi.pro@gmail.com


from PyQt4 import QtGui
from .card import Card
from random import shuffle

class CardGroup(QtGui.QGridLayout):
    def __init__(self, cat, level="Easy", flip=False, disable = False):
        super(CardGroup, self).__init__()
        self.cat = cat
        self.level = level
        self.disable = disable

        self.cardList = []
        if self.level == "Easy":
            self.rows = 2
            self.cols = 4
        else:
            self.rows = 3
            self.cols = 4

        multiplication = self.rows*self.cols

        for i in range(1,((multiplication)//2)+1):
            self.cardList.append(Card(i,self.cat,True))
            self.cardList.append(Card(i,self.cat, True))
        shuffle(self.cardList)
        shuffle(self.cardList)
        shuffle(self.cardList)

        count = 0

        for i in range(1,self.rows+1):
            for j in range(1,self.cols+1):
                self.addWidget(self.cardList[count],i,j)
                count += 1
    def showAll(self):
        for card in self.cardList:
            card.setEnabled(True)