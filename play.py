import deck
import handEvaluator
import player
import random
import table

##This texasHoldem class is unfinished. It needs to be revised for error handling and readability.
class texasHoldem:
    def __init__(self):
        self.table = table.table()
        self.evaluator = handEvaluator.handEvaluator()
        self.winningHand = -1
        self.winners = []
    def play(self):
        input("Welcome to Texas Holdem! You are 1 of 4 players who have 500 chips. When prompted to bet, you may wager any value between 0 and the number of chips you currently have. Press 'enter' to start the game")
        self.table.newHand()
        p1 = self.table.players["Player1"]
        while (p1.chips > -1 and p1.chips < 2001):
            self.winningHand = -1 ##Reset Winning Hand
            self.winners = [] #Reset winners
            self.table.newHand() ##Deal new hole cards
            self.preFlopBet()
            self.table.dealFlop()
            self.table.displayPot()
            self.table.displayMyHand()
            self.flopBet()
            self.table.dealTurn()
            self.table.displayPot()
            self.table.displayMyHand()
            self.turnBet()
            self.table.dealRiver()
            self.table.displayPot()
            self.table.displayMyHand()
            self.riverBet()
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
    def preFlopBet(self):
        p1 = self.table.players["Player1"]
        preFlopWager = input("How many chips would you like to bet this round? (You have " + str(p1.chips) + " chips) ")
        try:
            preFlopWager = int(preFlopWager)
        except:
            try:
                preFlopWager = int(float(preFlopWager))
            except:
                preFlopWager = 0
        self.wager(p1, preFlopWager)
        if preFlopWager > 0:
            for key in self.table.players:
                if random.random() < 0.9 and key != "Player1":
                    self.wager(self.table.players[key], preFlopWager)
                elif key == "Player1":
                    phantom = 0 ##got to be a better way to do this
                else:
                    self.table.players[key].folded = True
                    print (key + " folds")
    def flopBet(self):
        p1 = self.table.players["Player1"]
        flopWager = input("How many chips would you like to bet this round? (You have " + str(p1.chips) + " chips) ")
        try:
            flopWager = int(flopWager)
        except:
            try:
                flopWager = int(float(flopWager))
            except:
                flopWager = 0
        self.wager(p1, flopWager)
        if flopWager > 0:
            for key in self.table.players:
                if random.random() < 0.98 and key != "Player1":
                    self.wager(self.table.players[key], flopWager)
                elif key == "Player1":
                    phantom = 0
                else:
                    self.table.players[key].folded = True
                    print (key + " folds")
    def turnBet(self):
        p1 = self.table.players["Player1"]
        turnWager = input("How many chips would you like to bet this round? (You have " + str(p1.chips) + " chips) ")
        try:
            turnWager = int(turnWager)
        except:
            try:
                turnWager = int(float(turnWager))
            except:
                turnWager = 0
        self.wager(p1, turnWager)
        if turnWager > 0:
            for key in self.table.players:
                if random.random() < 0.9 and key != "Player1":
                    self.wager(self.table.players[key], turnWager)
                elif key == "Player1":
                    phantom = 0
                else:
                    self.table.players[key].folded = True
                    print (key + " folds")
    def riverBet(self):
        p1 = self.table.players["Player1"]
        riverWager = input("How many chips would you like to bet this round? (You have " + str(p1.chips) + " chips) ")
        try:
            riverWager = int(riverWager)
        except:
            try:
                riverWager = int(float(riverWager))
            except:
                riverWager = 0
            self.wager(p1, riverWager)
            if riverWager > 0:
                for key in self.table.players:
                    if random.random() < 0.9 and key != "Player1":
                        self.wager(self.table.players[key], riverWager)
                    elif key == "Player1":
                        phantom = 0
                    else:
                        self.table.players[key].folded = True
                        print (key + " folds")
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
