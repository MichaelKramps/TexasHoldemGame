##Simple poker game
##Created by Michael Kramps

import random

class deck:
    def __init__(self):
        self.availableCards = [(14, "Ace", "Hearts"), (13, "King", "Hearts"), (12, "Queen", "Hearts"),
                               (11, "Jack", "Hearts"), (10, "10", "Hearts"), (9, "9", "Hearts"),
                               (8, "8", "Hearts"), (7, "7", "Hearts"), (6, "6", "Hearts"),
                               (5, "5", "Hearts"), (4, "4", "Hearts"), (3, "3", "Hearts"),
                               (2, "2", "Hearts"), (14, "Ace", "Diamonds"), (13, "King", "Diamonds"), (12, "Queen", "Diamonds"),
                               (11, "Jack", "Diamonds"), (10, "10", "Diamonds"), (9, "9", "Diamonds"),
                               (8, "8", "Diamonds"), (7, "7", "Diamonds"), (6, "6", "Diamonds"),
                               (5, "5", "Diamonds"), (4, "4", "Diamonds"), (3, "3", "Diamonds"),
                               (2, "2", "Diamonds"), (14, "Ace", "Spades"), (13, "King", "Spades"), (12, "Queen", "Spades"),
                               (11, "Jack", "Spades"), (10, "10", "Spades"), (9, "9", "Spades"),
                               (8, "8", "Spades"), (7, "7", "Spades"), (6, "6", "Spades"),
                               (5, "5", "Spades"), (4, "4", "Spades"), (3, "3", "Spades"),
                               (2, "2", "Spades"), (14, "Ace", "Clubs"), (13, "King", "Clubs"), (12, "Queen", "Clubs"),
                               (11, "Jack", "Clubs"), (10, "10", "Clubs"), (9, "9", "Clubs"),
                               (8, "8", "Clubs"), (7, "7", "Clubs"), (6, "6", "Clubs"),
                               (5, "5", "Clubs"), (4, "4", "Clubs"), (3, "3", "Clubs"),
                               (2, "2", "Clubs"), ]
    def chooseCard(self):
        newCard = random.choice(self.availableCards)
        self.availableCards.remove(newCard)
        return newCard


class player:
    def __init__(self):
        self.holeCards = []
        self.chips = 500
        self.finalHand = []
        self.folded = False
    def bet(self, numChips):
        if numChips <= self.chips:
            self.chips -= numChips
            return numChips
        else:
            print ("You don't have enough chips")

######Simulator that can calculate percentage of certain types of hands for the given a number of simulations 
##class simulator1:
##    def __init__(self):
##        self.table = table()
##        self.straightFlushes = 0
##        self.fourKinds = 0
##        self.fullHouses = 0
##        self.flushes = 0
##        self.straights = 0
##        self.threeKinds = 0
##        self.twoPairs = 0
##        self.pairs = 0
##        self.highCards = 0
##        self.misses = 0
##    def display(self, sims):
##        print ("Straight Flushes: " + str(self.straightFlushes) + " / " + str(float(self.straightFlushes)/float(sims)) + "%")
##        print ("Four of a Kinds: " + str(self.fourKinds) + " / " + str(float(self.fourKinds)/float(sims)) + "%")
##        print ("Full Houses: " + str(self.fullHouses) + " / " + str(float(self.fullHouses)/float(sims)) + "%")
##        print ("Flushes: " + str(self.flushes) + " / " + str(float(self.flushes)/float(sims)) + "%")
##        print ("Straights: " + str(self.straights) + " / " + str(float(self.straights)/float(sims)) + "%")
##        print ("Three of a Kinds: " + str(self.threeKinds) + " / " + str(float(self.threeKinds)/float(sims)) + "%")
##        print ("Two Pairs: " + str(self.twoPairs) + " / " + str(float(self.twoPairs)/float(sims)) + "%")
##        print ("Pairs: " + str(self.pairs) + " / " + str(float(self.pairs)/float(sims)) + "%")
##        print ("High Cards: " + str(self.highCards) + " / " + str(float(self.highCards)/float(sims)) + "%")
##        print ("Misses: " + str(self.misses))
##    def simulate(self, sims):
##        for x in range(sims):
##            self.table = table()
##            hand = self.table.newHand()
##            result = (self.table.handEvaluator.evaluate(self.table.players["Player1"].holeCards, self.table.communityCards))
##            if result[0] == "straight flush":
##                self.straightFlushes += 1
##            elif result[0] == "four of a kind":
##                self.fourKinds += 1
##            elif result[0] == "full house":
##                self.fullHouses += 1
##            elif result[0] == "flush":
##                self.flushes += 1
##            elif result[0] == "straight":
##                self.straights += 1
##            elif result[0] == "three of a kind":
##                self.threeKinds += 1
##            elif result[0] == "two pair":
##                self.twoPairs += 1
##            elif result[0] == "pair":
##                self.pairs += 1
##            elif result[0] == "high card":
##                self.highCards += 1
##            else:
##                self.misses += 1
##        self.display(sims)
            
class table:
    def __init__(self):
        self.deck = deck()
        self.players = {}
        self.communityCards = []
        self.pot = 0
        self.handEvaluator = handEvaluator()
    def newHand(self):
        for key in self.players:
            self.players[key].folded = False
            self.players[key].holeCards = []
        self.dealCards()     
##        self.displayCards()
        self.displayCommunity()
        self.displayMyHand()
    def dealCards(self, numPlayers = 4, numCards = 2):
        self.deck = deck() #start with a new deck
        self.pot = 0 #new pot
        if bool(self.players) == False:
            for x in range(numPlayers):
                self.players.update({"Player" + str(x + 1): player()})
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

class handEvaluator: ##returns hand value in a list
    def checkStraightFlush(self, hand):
        flush = self.checkFlush(hand, True)
        if flush != False:
            straight = self.checkStraight(flush)
            if straight != False:
                return ["straight flush", straight[1]]
            else:
                return False
        else:
            return False
    def checkFourKind(self, hand):
        i = 0
        fourKind = False
        fourValue = 0
        for card in hand:
            nextCard1 = hand[i + 1]
            nextCard2 = hand[i + 2]
            nextCard3 = hand[i + 3]
            if card[0] == nextCard1[0] == nextCard2[0] == nextCard3[0]:
                fourKind = True
                fourValue = card[0]
                hand.remove(card)
                hand.remove(nextCard1)
                hand.remove(nextCard2)
                hand.remove(nextCard3)
            if fourKind == True or i == (len(hand) - 4):
                break
            i += 1
        if fourKind == True:
            return ["four of a kind", fourValue, hand[0][0]]
        else:
            return False
    def checkFullHouse(self, hand):
        threeKind = self.checkThreeKind(hand, False, True)
        if threeKind != False:
            remainingCards = threeKind[4]
            anotherThreeKind = self.checkThreeKind(remainingCards, True)
            if anotherThreeKind != False:
                return ["full house", threeKind[1], anotherThreeKind[1]]
            else:
                pair = self.checkPair(remainingCards, 2)
                if pair != False:
                    return ["full house", threeKind[1], pair[1]]
                else:
                    return False
        else:
            return False
    def checkFlush(self, hand, straightFlushCheck = False):
        i = 0
        flush = False
        suit = ""
        flushHand = []
        for card in hand:
            suit = card[2]
            flushHand.append(card)
            restOfHand = hand[i + 1:]
            for nextCard in restOfHand:
                if nextCard[2] == suit:
                    flushHand.append(nextCard)
            if len(flushHand) > 4:
                flush = True
                break
            elif i == (len(hand) - 5):
                break
            else:
                flushHand = [] ##resets hand for a failed flush attempt
                i += 1
        if flush == True and straightFlushCheck == False:
            return ["flush", flushHand[0][0], flushHand[1][0], flushHand[2][0], flushHand[3][0], flushHand[4][0]]
        elif flush == True and straightFlushCheck == True:
            return flushHand
        else:
            return False               
    def checkStraight(self, hand):
        i = 0
        straight = False
        aceInHand = False
        topStraightCard = ()
        numStraightCards = 1
        for card in hand:
            restOfHand = hand[i + 1:]
            if card[0] == 14:
                aceInHand = True
            if numStraightCards == 5:
                straight = True
                topStraightCard = card[0] + 4
                break
            if numStraightCards == 4:
                if card[0] == 2:
                    if aceInHand == True:
                        straight = True
                        topStraightCard = 5
                        break
                    else:
                        break
            for nextCard in restOfHand:
                if card[0] - nextCard[0] == 1:
                    numStraightCards += 1
                    break
                elif card[0] - nextCard[0] > 1:
                    numStraightCards = 1
                    break
                else:
                    break
            i += 1
        if straight == True:
            return ["straight", topStraightCard]
        else:
            return False            
    def checkThreeKind(self, hand, secondTest = False, fullHouse = False): ##Checks for three of a kind
        i = 0
        threeKind = False
        threeValue = 0
        for card in hand:
            nextCard1 = hand[i + 1]
            nextCard2 = hand[i + 2]
            if card[0] == nextCard1[0] == nextCard2[0]:
                threeKind = True
                threeValue = card[0]
                hand.remove(card)
                hand.remove(nextCard1)
                hand.remove(nextCard2)
            if threeKind == True or i == (len(hand) - 3):
                break
            i += 1
        if threeKind == True and secondTest == False and fullHouse == False:
            return ["three of a kind", threeValue, hand[0][0], hand[1][0]] ##, hand]
        elif threeKind == True and secondTest == False and fullHouse == True:
            return ["three of a kind", threeValue, hand[0][0], hand[1][0], hand] 
        elif threeKind == True and secondTest == True and fullHouse == False:
            return ["three of a kind", threeValue]
        else:
            return False
    def checkPair(self, hand, times = 0): ##Checks for one pair, then checks for another pair
        i = 0
        pair = False
        pairValue = 0
        for card in hand:
            nextCard = hand[i + 1]
            if card[0] == nextCard[0]:
                pair = True
                pairValue = card[0]
                hand.remove(card)
                hand.remove(nextCard)
            if pair == True or i == (len(hand) - 2):
                break
            i += 1
        if pair == True:
            firstTest = ["pair", pairValue, hand]
            if times == 0: ##check for two pair
                secondTest = self.checkPair(hand, 1)
                if secondTest[0] == "pair":
                    return ["two pair", firstTest[1], secondTest[1], hand[0][0]]
                else:
                    return ["pair", firstTest[1], hand[0][0], hand[1][0], hand[2][0]]
            else: ##only used for the full house pair check
                return ["pair", firstTest[1]]
        else:
            if times == 2:
                return False ##only used for the full house pair check
            else:
                return ["high card", hand[0][0], hand[1][0], hand[2][0], hand[3][0], hand[4][0]]
    def evaluate(self, hand, community = []): #evaluate the strength of a hand
        fullHand = hand + community
        orderedHand = tuple(self.orderCards(fullHand))
        straightFlush = self.checkStraightFlush(list(orderedHand))
        if straightFlush == False:
            fourKind = self.checkFourKind(list(orderedHand))
            if fourKind == False:
                fullHouse = self.checkFullHouse(list(orderedHand))
                if fullHouse == False:
                    flush = self.checkFlush(list(orderedHand))
                    if flush == False:
                        straight = self.checkStraight(list(orderedHand))
                        if straight == False:
                            threeKind = self.checkThreeKind(list(orderedHand))
                            if threeKind == False:
                                pair = self.checkPair(list(orderedHand))
                                return (pair)
                            else:
                                return (threeKind)
                        else:
                            return (straight)
                    else:
                        return (flush)
                else:
                    return (fullHouse)
            else:
                return (fourKind)
        else:
            return(straightFlush)
    def orderCards(self, cards): ##order cards from highest to lowest
        fullHand = cards
        i = 0
        for card in fullHand:
            card1 = card
            j = i + 1
            restOfHand = fullHand[j:]
            for nextCard in restOfHand:
                if nextCard[0] > card1[0]:
                    fullHand[i] = nextCard
                    fullHand[j] = card1
                    card1 = nextCard
                    j += 1
                else:
                    j += 1
            i += 1
        return fullHand
    def convertHandStrengthString(self, hand):
            if hand[0] == "straight flush":
                return 8
            elif hand[0] == "four of a kind":
                return 7
            elif hand[0] == "full house":
                return 6
            elif hand[0] == "flush":
                return 5
            elif hand[0] == "straight":
                return 4
            elif hand[0] == "three of a kind":
                return 3
            elif hand[0] == "two pair":
                return 2
            elif hand[0] == "pair":
                return 1
            else:
                return 0

##This texasHoldem class was just thrown together. It doesn't handle errors and it is sloppy. Please don't judge my abilities based on this class, but on the code above.
class texasHoldem:
    def __init__(self):
        self.table = table()
        self.evaluator = handEvaluator()
        self.winningHand = -1
        self.winners = []
    def play(self):
        input("Welcome to Texas Holdem! You are 1 of 4 players who have 500 chips. When prompted to bet, you may wager any value between 0 and the number of chips you currently have. Press 'enter' to start the game")
        self.table.newHand()
        p1 = self.table.players["Player1"]
        while (p1.chips > -1 and p1.chips < 2001):
            for key in self.table.players: ##Unfold all players
                self.table.players[key].folded = False
            if p1.holeCards == []:
                self.table.newHand()
            self.winningHand = -1 ##Reset Winning Hand, these resets should probably be moved to the table class when I rewrite this
            self.winners = [] #Reset winners
            preFlopWager = input("How many chips would you like to bet this round? (You have " + str(p1.chips) + " chips) ")
            self.wager(p1, int(preFlopWager))
            if int(preFlopWager) > 0:
                for key in self.table.players:
                    if random.random() < 0.9 and key != "Player1":
                        self.wager(self.table.players[key], int(preFlopWager))
                    elif key == "Player1":
                        phantom = 0 ##got to be a better way to do this
                    else:
                        self.table.players[key].folded = True
                        print (key + " folds")
            self.table.dealFlop()
            self.table.displayPot()
            self.table.displayMyHand()
            flopWager = input("How many chips would you like to bet this round? (You have " + str(p1.chips) + " chips) ")
            self.wager(p1, int(flopWager))
            if int(flopWager) > 0:
                for key in self.table.players:
                    if random.random() < 0.98 and key != "Player1":
                        self.wager(self.table.players[key], int(flopWager))
                    elif key == "Player1":
                        phantom = 0
                    else:
                        self.table.players[key].folded = True
                        print (key + " folds")
            self.table.dealTurn()
            self.table.displayPot()
            self.table.displayMyHand()
            turnWager = input("How many chips would you like to bet this round? (You have " + str(p1.chips) + " chips) ")
            self.wager(p1, int(turnWager))
            if int(turnWager) > 0:
                for key in self.table.players:
                    if random.random() < 0.9 and key != "Player1":
                        self.wager(self.table.players[key], int(turnWager))
                    elif key == "Player1":
                        phantom = 0
                    else:
                        self.table.players[key].folded = True
                        print (key + " folds")
            self.table.dealRiver()
            self.table.displayPot()
            self.table.displayMyHand()
            riverWager = input("How many chips would you like to bet this round? (You have " + str(p1.chips) + " chips) ")
            self.wager(p1, int(riverWager))
            if int(riverWager) > 0:
                for key in self.table.players:
                    if random.random() < 0.9 and key != "Player1":
                        self.wager(self.table.players[key], int(riverWager))
                    elif key == "Player1":
                        phantom = 0
                    else:
                        self.table.players[key].folded = True
                        print (key + " folds")
            for key in self.table.players:
                if self.table.players[key].folded == False:
                    self.table.players[key].finalHand = self.evaluator.evaluate(self.table.players[key].holeCards, self.table.communityCards)
                    self.winners.append(key)
                    print (key + str(self.table.players[key].finalHand))
            for key in self.table.players:
                if self.table.players[key].folded == False:
                    if self.evaluator.convertHandStrengthString(self.table.players[key].finalHand) > self.winningHand:
                        self.winningHand = self.evaluator.convertHandStrengthString(self.table.players[key].finalHand)
                        self.winners = []
                        self.winners.append(key)
                        del (self.table.players[key].finalHand[0])
                    elif self.evaluator.convertHandStrengthString(self.table.players[key].finalHand) == self.winningHand:
                        self.winners.append(key)
                        del (self.table.players[key].finalHand[0])
            if len(self.winners) == 1:
                self.table.payoutPot(self.winners[0], self.table.pot)
                print (self.winners[0] + "wins the pot!")##we have a winner!
            else:
                winningPlayer = self.findWinner(self.winners)
                if winningPlayer == "Split pot":
                    print ("It's a split pot.")
                else:
                    print (winningPlayer + " wins the pot!")
            for key in self.table.players: ##empty players' hands
                self.table.players[key].holeCards = []
            if p1.chips < 1:
                print ("You ran out of chips!")
                break
            elif p1.chips > 1999:
                print ("You win!")
                break
                                        
                    
    def wager(self, player, wager):
        player.bet(wager)
        self.table.addToPot(wager)

    def findWinner(self, wins):
        self.winningHand = 0
        firstWinner = wins[0]
        if len(wins) == 1:
            self.table.payoutPot(firstWinner, self.table.pot)
            return firstWinner
        elif self.table.players[firstWinner].finalHand == []:
            payout = self.table.pot/len(wins)
            for player in wins:
                self.table.payoutPot(player, payout)
            return ("Split pot") ##something
        else:
            for player in wins:
                if self.table.players[player].finalHand[0] > self.winningHand:
                    self.winningHand = self.table.players[player].finalHand[0]
                    self.winners = []
                    self.winners.append(player)
                    del (self.table.players[player].finalHand[0])
                elif self.table.players[player].finalHand[0] == self.winningHand:
                    self.winners.append(player)
                    del (self.table.players[player].finalHand[0])
            return self.findWinner(self.winners)
            

game = texasHoldem()
game.play()
