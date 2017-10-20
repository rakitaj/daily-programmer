import unittest
from cribbage import Hand, Card, Suit, Rank
from typing import List

class CribbageTests(unittest.TestCase):

    def hand_1(self) -> Hand:
        return self.create_hand(["AS", "JS", "JD", "3C", "2D"])

    def hand_2(self) -> Hand:
        return self.create_hand(["AS", "JS", "JD", "3C", "2K"])

    def hand_3(self) -> Hand:
        return self.create_hand(["2K", "3K", "8K", "9D", "AK"])

    def hand_4(self) -> Hand:
        return self.create_hand(["2K", "3K", "8K", "9K", "AD"])

    def hand_5(self) -> Hand:
        return self.create_hand(["2K", "3K", "8K", "9K", "AK"])

    def create_hand(self, input_hand):
        cards: List[Card] = list()
        for chars in input_hand:
            cards.append(Card.create_card_from_chars(chars))
        return Hand(cards)

    def test_nobs_1(self):
        hand_1 = self.hand_1()
        self.assertEqual(1, hand_1.nobs())

    def test_nobs_2(self):
        hand_2 = self.hand_2()
        self.assertEqual(0, hand_2.nobs())
    
    def test_flush(self):
        hand_3 = self.hand_3()
        self.assertEqual(0, hand_3.flush())
        hand_4 = self.hand_4()
        self.assertEqual(4, hand_4.flush())
        hand_5 = self.hand_5()
        self.assertEqual(5, hand_5.flush())

if __name__ == "__main__":
    unittest.main()