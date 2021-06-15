import random
def get_determiner(quantity):

    """Return a randomly chosen determiner. A determiner is a word
    like "the", "a", "one", "two", "some", "many". If quantity == 1,
    this function will return either "the" or "one". Otherwise
    this function will return either "some" or "many".

    Parameter
        quantity: an integer. If quantity == 1, this function will
            return a determiner for a singular noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["the", "one"]
    else:
        words = ["some", "many"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun. If quantity == 1, this
    function will return one of these ten singular nouns:
        "adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"
    Otherwise, this function will return one of these ten
    plural nouns:
        "adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"

    Parameter
        quantity: an integer that determines if the
            returned noun is singular or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = ['adult', 'bird', 'boy', 'car', 'cat', 'child',
        'dog', 'girl', 'man', 'woman']
    else:
        words = ['adults', 'birds', 'boys', 'cars', 'cats',
        'children', 'dogs', 'girls', 'men', 'women']
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past", this
    function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this function will
    return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1, this function
    will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of these
    ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameter
        quantity: an integer that determines if the returned
            verb is singular or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == 'past':
        words = [ 'drank', 'ate', 'grew', 'laughed', 'thought',
        'ran', 'slept', 'talked', 'walked', 'wrote']
    elif tense == 'present' and quantity == 1:
        words = ['drinks', 'eats', 'grows', 'laughs', 'thinks',
        'runs', 'sleeps', 'talks', 'walks', 'writes']
    elif tense == 'present' and quantity != 1:
        words = ['drink', 'eat', 'grow', 'laugh', 'think',
        'run', 'sleep', 'talk', 'walk', 'write']
    elif tense == 'future':
        words = ['will drink', 'will eat', 'will grow', 'will laugh',
        'will think', 'will run', 'will sleep', 'will talk',
        'will walk', 'will write']
    word = random.choice(words)
    return word

def get_preposition():
    words = ['about', 'above', 'across', 'after', 'along',
        'around', 'at', 'before', 'behind', 'below',
        'beyond', 'by', 'despite', 'except', 'for',
        'from', 'in', 'into', 'near', 'of',
        'off', 'on', 'onto', 'out', 'over',
        'past', 'to', 'under', 'with', 'without']
    word = random.choice(words)
    return word
def get_prepositional_phrase(quantity, tense):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and nouns are singular or plural.
    Return: a prepositional phrase.
    """
    phrase = f'{get_determiner(quantity)} {get_noun(quantity)} {get_verb(quantity, tense)} {get_preposition()} {get_determiner(quantity)} {get_noun(quantity)}'
    # phrase = f'{get_preposition()} {get_determiner(quantity)} {get_noun(quantity)}'
    return phrase
def main():
    print(f'{get_determiner(1)} {get_noun(1)} {get_verb(0,"past")}')
    print(f'{get_determiner(0)} {get_noun(0)} {get_verb(0, "past")}')
    print(f'{get_determiner(1)} {get_noun(1)} {get_verb(0, "present")}')
    print(f'{get_determiner(0)} {get_noun(0)} {get_verb(1,"present")}')
    print(f'{get_determiner(1)} {get_noun(1)} {get_verb(0, "future")}')
    print(f'{get_determiner(0)} {get_noun(0)} {get_verb(0, "future")}')
    print(f'{get_prepositional_phrase(1, "past")}')
    print(f'{get_prepositional_phrase(0, "past")}')
    print(f'{get_prepositional_phrase(1, "present")}')
    print(f'{get_prepositional_phrase(0, "present")}')
    print(f'{get_prepositional_phrase(1, "future")}')
    print(f'{get_prepositional_phrase(0, "future")}')
main()
