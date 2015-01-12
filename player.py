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
