"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""
from operator import itemgetter

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    word_count = {} # Dictionary to store words and their counts
    phrase = phrase.split() # Split string into list of words

    # Loop through each word and add to dictionary with a value of 1 if does
    # not exist, otherwise increment the value count associated with that key.
    for word in phrase:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count # Return word count dictionary


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon.

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If melon name does not exist, return 'No price found'.

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """
    # Dictionary to represent melon names and prices
    melon_prices = {'Watermelon': 2.95,
                    'Cantaloupe': 2.50,
                    'Musk': 3.25,
                    'Christmas': 14.25}

    # Return the price associate with a melon name or output that it was not found
    return melon_prices.get(melon_name, 'No price found')


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

        >>> word_length_sorted(["porcupine", "ok"])
        [(2, ['ok']), (9, ['porcupine'])]
    """
    word_lengths = {} # Dictionary for word lengths and words of that length

    for word in words:
        word_lengths.setdefault(len(word), [])
        word_lengths[len(word)].append(word)

    # Sorts words alphabetically in values of each key
    for key in word_lengths:
        word_lengths[key].sort()

    # Sort lengths of words in ascending order and created the tuples that
    # represent the dictionary.
    word_lengths = sorted(word_lengths.items())

    return word_lengths # Returns the tuples that represent the dictionary

def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    # Dictionary to translate English into Pirate-speak
    english_to_pirate = {'sir': 'matey',
                        'hotel': 'fleabag inn',
                        'student': 'swabbie',
                        'man': 'matey',
                        'professor': 'foul blaggart',
                        'restaurant': 'galley',
                        'your': 'yer',
                        'excuse': 'arr',
                        'students': 'swabbies',
                        'are': 'be',
                        'restroom': 'head',
                        'my': 'me',
                        'is': 'be'
                        }

    phrase = phrase.split() # Split string of phrase into list of words
    pirate_phrase = [] # List to store translated phrase

    # Loops 
    for word in phrase: 
        if english_to_pirate.get(word, None):
            pirate_phrase.append(english_to_pirate[word])
        else:
            pirate_phrase.append(word)

    return " ".join(pirate_phrase) # Join list of Pirate-speak to string


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    # Add the first word of the list as the first word in the result
    result_words = []
    result_words.append(names[0])

    # Remove first word from list of words
    names = names[1:]

    # Dictionary for starting letter and words that start with that letter
    names_dict = {}

    # Loop through the words and add the first letter of those words to the
    # dictionary as a key and the word as a value
    for name in names:
        names_dict.setdefault(name[0], [])
        names_dict[name[0]].append(name)

    # Last character of the first word
    last_char = result_words[0][-1:]

    # Loop through the list while there is a word that starts with the last
    # character of the next word
    while names_dict.get(last_char, None):

        # Checks to see if the key exists with an empty list.
        if names_dict[last_char] == []:
            break

        # Pops first word of the list of words (with correct starting
        # letter) to the result
        result_words.append(names_dict[last_char].pop(0))

        # Assign a new last character
        last_char = result_words[len(result_words) - 1][-1:] 

    return result_words

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
