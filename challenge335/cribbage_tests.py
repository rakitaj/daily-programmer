import unittest
from cribbage import Hand, Card, Suit, Rank
from typing import List

class CribbageTests(unittest.TestCase):

    def hand_1_nobs(self) -> Hand:
        return self.create_hand(["AS", "JS", "JD", "3C", "2D"])

    def hand_0_nobs(self) -> Hand:
        return self.create_hand(["AS", "JS", "JD", "3C", "2K"])

    def hand_no_flush(self) -> Hand:
        return self.create_hand(["2K", "3K", "8K", "9D", "AK"])

    def hand_flush_4_cards(self) -> Hand:
        return self.create_hand(["2K", "3K", "8K", "9K", "AD"])

    def hand_flush_5_cards(self) -> Hand:
        return self.create_hand(["2K", "3K", "8K", "9K", "AK"])

    def create_hand(self, input_hand):
        cards: List[Card] = list()
        for chars in input_hand:
            cards.append(Card.create_card_from_chars(chars))
        return Hand(cards)

    def test_nobs(self):
        self.assertEqual(1, self.hand_1_nobs().nobs())
        self.assertEqual(0, self.hand_0_nobs().nobs())
        
    
    def test_flush(self):
        self.assertEqual(0, self.hand_no_flush().flush())
        self.assertEqual(4, self.hand_flush_4_cards().flush())
        self.assertEqual(5, self.hand_flush_5_cards().flush())

if __name__ == "__main__":
    unittest.main()