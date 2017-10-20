from enum import Enum, auto
from typing import List
import json
import os
import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

class Suit(object):

    def __init__(self, suit):
        self.value = suit

class Rank(object):

    def __init__(self, rank):
        self.value = rank

class Card(object):
    
    def __init__(self, rank: Rank, suit: Suit) -> None:
        self.rank = rank
        self.suit = suit

    def get_rank(self):
        return self.rank.value

    def get_suit(self):
        return self.suit.value

    def __str__(self):
        return f"{self.get_rank} of {self.get_suit()}"

    @classmethod
    def create_card_from_chars(cls, chars: str) -> "Card":
        rank = Rank(chars[0])
        suit = Suit(chars[1])
        return Card(rank, suit)

    @classmethod
    def create_cards_from_json(cls, path: str, input_name: str) -> List["Card"]:
        cards: List[Card] = list()
        with open(path, "r") as json_data:
            data = json.load(json_data)
            raw_json_cards = data[input_name].split(",")
        for raw_card in raw_json_cards:
            card = Card.create_card_from_chars(raw_card)
            cards.append(card)
        return cards

class Hand(object):

    def __init__(self, cards: List[Card]) -> None:
        self.cards = cards[:4]
        self.face_up_card = cards[4]

    def nobs(self) -> int:
        points = 0
        for card in self.cards:
            if card.get_rank() == "J" and card.get_suit() == self.face_up_card.get_suit():
                points += 1
        return points

    def flush(self) -> int:
        all_the_same = True
        suit = self.cards[0].get_suit()
        for card in self.cards[:4]:
            if card.get_suit() == suit:
                pass
            else:
                all_the_same = False
        if all_the_same == False:
            return 0
        else:
            if suit == self.face_up_card.get_suit():
                return 5
            else:
                return 4

    def get_score(self):
        pass

    def __str__(self) -> str:
        result = f"The hand is{os.linesep}"
        for card in self.cards:
            result += f"{str(card)}{os.linesep}"
        result += str(self.face_up_card)
        return result

if __name__ == "__main__":
    cards = Card.create_cards_from_json("cribbage_sample_input.json", "first")
    hand = Hand(cards)
    print(hand)