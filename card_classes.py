import random


class Card:

    def __init__(self, csv_dict):
        # csv_dict is a single entry of dict with 7 stats:
        self.id_c = csv_dict['id']
        self.name = csv_dict['name']
        self.cost = csv_dict['cost']
        self.counter = csv_dict['counter']
        self.type_c = csv_dict['type']
        self.effect = csv_dict['effect']
        self.ki_cost = csv_dict['ki_cost']

    def __str__(self):
        return f'{self.name}\n{self.cost}{self.counter} - {self.type_c}\n«{self.effect}»\n'


class Deck:

    def __init__(self, name, deck):
        # deck is the full list(csv_dict)
        self.name = name
        self.deck = []
        for card in deck:
            self.deck.append(Card(card))
        self.shuffle()

    def __len__(self):
        return len(self.deck)

    def __str__(self):
        if len(self) == 0:
            return '<Empty deck>'

        str_ret = []
        for c in self.deck:
            str_ret.append(c.name)
        return ", ".join(str_ret)

    def draw_card(self):
        """Extracts one card from the top deck"""
        return self.deck.pop()

    def empty(self):
        """If the cards go to another deck, empty this one"""
        self.deck = []

    def refill(self, another_deck):
        """From the discard deck to the playing deck"""
        self.deck = another_deck.deck
        another_deck.empty()
        self.shuffle()

    def shuffle(self):
        """Shuffles the deck when init and refill"""
        random.shuffle(self.deck)
