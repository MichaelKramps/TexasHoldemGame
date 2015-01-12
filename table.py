import deck
import handEvaluator
import player

class table:
    def __init__(self):
        self.deck = deck.deck()
        self.players = {}
        self.communityCards = []
        self.pot = 0
        self.handEvaluator = handEvaluator.handEvaluator()
    def newHand(self):
        for key in self.players:
            self.players[key].folded = False
            self.players[key].holeCards = []
        self.dealCards()     
##        self.displayCards()
        self.displayCommunity()
        self.displayMyHand()
    def dealCards(self, numPlayers = 4, numCards = 2):
        self.deck = deck.deck() #start with a new deck
        self.pot = 0 #new pot
        if bool(self.players) == False:
            for x in range(numPlayers):
                self.players.update({"Player" + str(x + 1): player.player()})
                currentPlayer = self.players["Player" + str(x + 1)]
                for y in range(numCards):
                    currentPlayer.holeCards.append(self.deck.chooseCard())
        else:
            for key in self.players:
                for card in range(numCards):
                    self.players[key].holeCards.append(self.deck.chooseCard())
    def displayMyHand(self):
        myHand = ""
        for card in self.players["Player1"].holeCards:
            myHand += ("(" + card[1] + " of " + card[2] + ")")
        print ("My Hand: " + myHand)
    def displayCards(self):
        for key in self.players:
            currentPlayer = self.players[key]
            currentCards = currentPlayer.holeCards
            cards = ""
            for card in currentCards:
                cards += ("(" + card[1] + " of " + card[2] + ")")
            print (key + ": " + cards)
    def dealFlop(self, numCards = 3):
        self.communityCards = [] #new Community cards
        for x in range(numCards):
            self.communityCards.append(self.deck.chooseCard())
        print ("After Flop - " + self.displayCommunity())
    def dealTurn(self, numCards = 1):
        for x in range(numCards):
            self.communityCards.append(self.deck.chooseCard())
        print ("After Turn - " + self.displayCommunity())
    def dealRiver(self, numCards = 1):
        for x in range(numCards):
            self.communityCards.append(self.deck.chooseCard())
        print ("After River - " + self.displayCommunity())
    def displayCommunity(self):
        cards = ""
        for card in self.communityCards:
            cards += ("(" + card[1] + " of " + card[2] + ")")
        return ("Community Cards: " + cards)
    def addToPot(self, numChips):
        self.pot += numChips
    def displayPot(self):
        print ("Pot Total: " + str(self.pot))
    def payoutPot(self, player, pot):
        self.players[player].chips += pot
    def evaluate(self):
        i = 1
        for player in self.players:
            hand = self.handEvaluator.evaluate(self.players[player].holeCards, self.communityCards)
            print (player + ": " + str(hand))
            i += 1
