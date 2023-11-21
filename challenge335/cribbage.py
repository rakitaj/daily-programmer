from typing import List, Tuple
import json
import os
import logging, sys
import itertools
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

    def get_rank_number(self) -> int:
        if self.get_rank() == "A":
            return 1
        elif self.get_rank() in ("J", "Q", "K"):
            return 10
        else:
            return self.get_rank()

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
    
    def fifteen(self) -> int:
        points = 0
        all_combinations = self.get_all_combinations()
        for combo in all_combinations:
            total = 0
            for card in combo:
                total += card.get_rank_number()
            if total == 15:
                points += 2
        return points
        
    def get_all_combinations(self) -> List[Tuple[Card]]:
        all_combinations : List[Tuple[Card]] = list()
        all_cards = list()
        all_cards.extend(self.cards)
        all_cards.append(self.face_up_card)
        for i in range(0, len(all_cards)):
            combos = list(itertools.combinations(all_cards, 1))
            all_combinations.extend(combos)
        return all_combinations

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