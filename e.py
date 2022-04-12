class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
    def printCard(self):
        print(" ______")
        print("|" + self.suit + "     |")
        print("|      |")
        if self.number < 10: print("|  " + str(self.number) + "   |")
        else: print("|  " + str(self.number) + "  |")
        print("|      |")
        print("|     " + self.suit + "|")
        print(" ‾‾‾‾‾‾")

ticker = 0
deck = []

while ticker < 12:
   deck.append(Card(ticker, "♠"))
   ticker = ticker + 1

ticker = 0
while ticker < 12:
    deck[ticker].printCard()
    ticker = ticker + 1
    
