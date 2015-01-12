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
