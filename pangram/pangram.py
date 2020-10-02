from string import ascii_lowercase

alphabet = set(ascii_lowercase)


def is_pangram(sentence=""):
    """
    Determine if a sentence is a pangram
    - A pangram is a sentence using every letter of the alphabet at least once.
    - ex: The quick brown fox jumps over the lazy dog.
    """

    if not isinstance(sentence, str):
        raise Exception("sentence must be a string")

    missingLetters = alphabet.difference(sentence.lower())
    return len(missingLetters) == 0
