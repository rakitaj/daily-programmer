from typing import Sequence, Dict, Callable
import common

def valid_passphrases(passphrases: Sequence[str], validate: Callable[[str], bool]) -> int:
    count = 0
    for passphrase in passphrases:
        if validate(passphrase):
            count += 1
    return count

def is_valid(passphrase: str) -> bool:
    passphrase_words: Dict[str, int] = {}
    for word in passphrase.split():
        if word in passphrase_words:
            return False
        else:
            passphrase_words[word] = 1
    return True

def is_valid_no_anagrams(passphrase: str) -> bool:
    passphrase_words: Dict[str, int] = {}
    words = passphrase.split()
    normalized_words = ["".join(sorted(word)) for word in words]
    for word in normalized_words:
        if word in passphrase_words:
            return False
        else:
            passphrase_words[word] = 1
    return True
 
if __name__ == "__main__":
    challenge_input = common.lines_from_text_file("day04_input.txt")
    print(f"Basic: {valid_passphrases(challenge_input, is_valid)}")
    print(f"No anagrams: {valid_passphrases(challenge_input, is_valid_no_anagrams)}")