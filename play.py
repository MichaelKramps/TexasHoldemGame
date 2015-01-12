import deck
import handEvaluator
import player
import random
import table

##This texasHoldem class was just thrown together. It doesn't handle errors and it is sloppy. I will be overhauled soon.
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
