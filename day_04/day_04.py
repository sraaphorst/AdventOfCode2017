#!/usr/bin/env python3

# Automatic submission does not appear to be working.
import aocd


def is_valid_passphrase(passphrase):
    """
    Determine if a supplied passphrase, as a string, is valid, i.e. does not contain repeated words.
    :param passphrase: the string representing the passphrase
    :return: True if valid, and False otherwise

    >>> is_valid_passphrase('aa bb cc dd ee')
    True
    >>> is_valid_passphrase('aa bb cc dd aa')
    False
    >>> is_valid_passphrase('aa bb cc dd aaa')
    True
    """
    words = passphrase.split()
    return len(set(words)) == len(words)


def is_valid_anagramfree_passphrase(passphrase):
    """
    Determine if a supplied passphrase, as a string, is valid, i.e. does not contain repeated words or anagrams.
    :param passphrase: the string representing the passphrase
    :return: True if valid, and False otherwise

    >>> is_valid_anagramfree_passphrase('abcde fghij')
    True
    >>> is_valid_anagramfree_passphrase('abcde xyz ecdab')
    False
    >>> is_valid_anagramfree_passphrase('a ab abc abd abf abj')
    True
    >>> is_valid_anagramfree_passphrase('iiii oiii ooii oooi oooo')
    True
    >>> is_valid_anagramfree_passphrase('oiii ioii iioi iiio')
    False
    """
    # Keep track of how many entries we expect to see in the set.
    words = passphrase.split()
    s = {''.join(sorted(word)) for word in words}
    return len(s) == len(words)


def count_valid_passphrases(passphrases, filterer):
    """
    Determine how many, out of a block of line-separated passphrases, are valid.
    :param passphrases: the block of line-separated passphrases
    :param filterer: the filterer to use to determine valid passphrases
    :return: the number of valid passphrases

    >>> count_valid_passphrases('aa bb cc dd ee\\naa bb cc dd aa\\naa bb cc dd aaa', is_valid_passphrase)
    2
    """
    return len(list(filter(filterer, passphrases.split('\n'))))


if __name__ == '__main__':
    session = aocd.get_cookie()
    data = aocd.get_data(day=4, year=2017, session=session)

    a1 = count_valid_passphrases(data, is_valid_passphrase)
    print("a1 = %r" % a1)
    aocd.submit1(a1, day=1, year=2017, session=session, reopen=False)

    a2 = count_valid_passphrases(data, is_valid_anagramfree_passphrase)
    print("a2 = %r" % a2)
    aocd.submit2(a1, day=1, year=2017, session=session, reopen=False)
