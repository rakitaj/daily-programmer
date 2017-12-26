from typing import Sequence, Dict, Callable
import common

def valid_passphrases(passphrases: Sequence[str], validate: Callable[[str], bool]) -> int:
    count = 0
    for passphrase in passphrases:
        if validate(passphrase):
            count += 1
    return count

def basic_validation(passphrase: str) -> bool:
    return validate_transformed_words(passphrase.split())

def anagram_validation(passphrase: str) -> bool:
    words = passphrase.split()
    normalized_words = ["".join(sorted(word)) for word in words]
    return validate_transformed_words(normalized_words)

def validate_transformed_words(words: Sequence[str]) -> bool:
    passphrase_words: Dict[str, int] = {}
    for word in words:
        if word in passphrase_words:
            return False
        else:
            passphrase_words[word] = 1
    return True
 
if __name__ == "__main__":
    challenge_input = common.lines_from_text_file("day04_input.txt")
    print(f"Basic: {valid_passphrases(challenge_input, basic_validation)}")
    print(f"No anagrams: {valid_passphrases(challenge_input, anagram_validation)}")