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
