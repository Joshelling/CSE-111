from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import pytest


def test_get_determiner():
    # Test the singular determiners.
    singular_determiners = ["the", "one"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the singular_determiners list.
        assert word in singular_determiners

    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.

    # Test the plural determiners.
    plural_determiners = ["some", "many"]
    for _ in range(4):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners
    
def test_get_noun():
    singular_noun = ['adult', 'bird', 'boy', 'car', 'cat', 'child',
        'dog', 'girl', 'man', 'woman']
    for _ in range(4):
        word = get_noun(1)
        assert word in singular_noun
    
    plural_noun = ['adults', 'birds', 'boys', 'cars', 'cats',
        'children', 'dogs', 'girls', 'men', 'women']
    for _ in range(4):
        word = get_noun(2)
        assert word in plural_noun

def test_get_verb():
    past_verb = [ 'drank', 'ate', 'grew', 'laughed', 'thought',
        'ran', 'slept', 'talked', 'walked', 'wrote']
    for _ in range(4):
        word = get_verb(0, 'past')
        assert word in past_verb
    
    present_plural_verb = ['drinks', 'eats', 'grows', 'laughs', 'thinks',
        'runs', 'sleeps', 'talks', 'walks', 'writes']
    for _ in range(4):
        word = get_verb(1, 'present')
        assert word in present_plural_verb
    
    present_single_verb = ['drink', 'eat', 'grow', 'laugh', 'think',
        'run', 'sleep', 'talk', 'walk', 'write']
    for _ in range(4):
        word = get_verb(0, 'present')
        assert word in present_single_verb
    future_verb = ['will drink', 'will eat', 'will grow', 'will laugh',
        'will think', 'will run', 'will sleep', 'will talk',
        'will walk', 'will write']
    for _ in range(4):
        word = get_verb(0, 'future')
        assert word in future_verb
def test_get_preposition():
    prep_phrases = ['about', 'above', 'across', 'after', 'along',
        'around', 'at', 'before', 'behind', 'below',
        'beyond', 'by', 'despite', 'except', 'for',
        'from', 'in', 'into', 'near', 'of',
        'off', 'on', 'onto', 'out', 'over',
        'past', 'to', 'under', 'with', 'without']
    for _ in range(4):
        word = get_preposition()
        assert word in prep_phrases

def test_get_prepositional_phrase():
    prep_phrases = ['about', 'above', 'across', 'after', 'along',
        'around', 'at', 'before', 'behind', 'below',
        'beyond', 'by', 'despite', 'except', 'for',
        'from', 'in', 'into', 'near', 'of',
        'off', 'on', 'onto', 'out', 'over',
        'past', 'to', 'under', 'with', 'without']
    singular_determiners = ["the", "one"]
    plural_determiners = ["some", "many"]
    singular_noun = ['adult', 'bird', 'boy', 'car', 'cat', 'child',
        'dog', 'girl', 'man', 'woman']
    plural_noun = ['adults', 'birds', 'boys', 'cars', 'cats',
        'children', 'dogs', 'girls', 'men', 'women']
    past_verb = [ 'drank', 'ate', 'grew', 'laughed', 'thought',
        'ran', 'slept', 'talked', 'walked', 'wrote']
    present_plural_verb = ['drinks', 'eats', 'grows', 'laughs', 'thinks',
        'runs', 'sleeps', 'talks', 'walks', 'writes']
    future_verb = ['will drink', 'will eat', 'will grow', 'will laugh',
        'will think', 'will run', 'will sleep', 'will talk',
        'will walk', 'will write']
    present_single_verb = ['drink', 'eat', 'grow', 'laugh', 'think',
        'run', 'sleep', 'talk', 'walk', 'write']
    for _ in range(4):

        sentence = get_prepositional_phrase(1, "past")
        final_sentence = sentence.split(' ')
    
        
        if final_sentence [0] in singular_determiners:
            assert final_sentence [0] in singular_determiners
        elif final_sentence [0] in plural_determiners:
            assert final_sentence [0] in plural_determiners
        if final_sentence [1] in singular_noun:
            assert final_sentence [1] in singular_noun
        elif final_sentence [1] in plural_noun:
            assert final_sentence [1] in plural_noun
        if final_sentence [2] in past_verb:
            assert final_sentence [2] in past_verb
        elif final_sentence [2] in present_single_verb:
            assert final_sentence [2] in present_single_verb
        elif final_sentence [2] in present_plural_verb:
            assert final_sentence in present_plural_verb
        elif final_sentence [2] in future_verb:
            assert final_sentence [2] in future_verb
        assert final_sentence [3] in prep_phrases
        if final_sentence [4] in singular_determiners:
            assert final_sentence [4] in singular_determiners
        elif final_sentence [4] in plural_determiners:
            assert final_sentence [4] in plural_determiners
        if final_sentence [5] in singular_noun:
            assert final_sentence [5] in singular_noun 
        elif final_sentence [5] in plural_noun:
            assert final_sentence [5] in plural_noun
    
    for _ in range(4):

        sentence = get_prepositional_phrase(0, "past")
        final_sentence = sentence.split(' ')
    
        
        if final_sentence [0] in singular_determiners:
            assert final_sentence [0] in singular_determiners
        elif final_sentence [0] in plural_determiners:
            assert final_sentence [0] in plural_determiners
        if final_sentence [1] in singular_noun:
            assert final_sentence [1] in singular_noun
        elif final_sentence [1] in plural_noun:
            assert final_sentence [1] in plural_noun
        if final_sentence [2] in past_verb:
            assert final_sentence [2] in past_verb
        elif final_sentence [2] in present_single_verb:
            assert final_sentence [2] in present_single_verb
        elif final_sentence [2] in present_plural_verb:
            assert final_sentence in present_plural_verb
        elif final_sentence [2] in future_verb:
            assert final_sentence [2] in future_verb
        assert final_sentence [3] in prep_phrases
        if final_sentence [4] in singular_determiners:
            assert final_sentence [4] in singular_determiners
        elif final_sentence [4] in plural_determiners:
            assert final_sentence [4] in plural_determiners
        if final_sentence [5] in singular_noun:
            assert final_sentence [5] in singular_noun 
        elif final_sentence [5] in plural_noun:
            assert final_sentence [5] in plural_noun
    
    for _ in range(4):

        sentence = get_prepositional_phrase(1, "present")
        final_sentence = sentence.split(' ')
    
        
        if final_sentence [0] in singular_determiners:
            assert final_sentence [0] in singular_determiners
        elif final_sentence [0] in plural_determiners:
            assert final_sentence [0] in plural_determiners
        if final_sentence [1] in singular_noun:
            assert final_sentence [1] in singular_noun
        elif final_sentence [1] in plural_noun:
            assert final_sentence [1] in plural_noun
        if final_sentence [2] in past_verb:
            assert final_sentence [2] in past_verb
        elif final_sentence [2] in present_single_verb:
            assert final_sentence [2] in present_single_verb
        elif final_sentence [2] in present_plural_verb:
            assert final_sentence [2] in present_plural_verb
        elif final_sentence [2] in future_verb:
            assert final_sentence [2] in future_verb
        assert final_sentence [3] in prep_phrases
        if final_sentence [4] in singular_determiners:
            assert final_sentence [4] in singular_determiners
        elif final_sentence [4] in plural_determiners:
            assert final_sentence [4] in plural_determiners
        if final_sentence [5] in singular_noun:
            assert final_sentence [5] in singular_noun 
        elif final_sentence [5] in plural_noun:
            assert final_sentence [5] in plural_noun
        
    for _ in range(4):

        sentence = get_prepositional_phrase(0, "present")
        final_sentence = sentence.split(' ')
    
        
        if final_sentence [0] in singular_determiners:
            assert final_sentence [0] in singular_determiners
        elif final_sentence [0] in plural_determiners:
            assert final_sentence [0] in plural_determiners
        if final_sentence [1] in singular_noun:
            assert final_sentence [1] in singular_noun
        elif final_sentence [1] in plural_noun:
            assert final_sentence [1] in plural_noun
        if final_sentence [2] in past_verb:
            assert final_sentence [2] in past_verb
        elif final_sentence [2] in present_single_verb:
            assert final_sentence [2] in present_single_verb
        elif final_sentence [2] in present_plural_verb:
            assert final_sentence in present_plural_verb
        elif final_sentence [2] in future_verb:
            assert final_sentence [2] in future_verb
        assert final_sentence [3] in prep_phrases
        if final_sentence [4] in singular_determiners:
            assert final_sentence [4] in singular_determiners
        elif final_sentence [4] in plural_determiners:
            assert final_sentence [4] in plural_determiners
        if final_sentence [5] in singular_noun:
            assert final_sentence [5] in singular_noun 
        elif final_sentence [5] in plural_noun:
            assert final_sentence [5] in plural_noun
    
    for _ in range(4):

        sentence = get_prepositional_phrase(1, "future")
        final_sentence = sentence.split(' ')
    
        # assert final_sentence [3] in prep_phrases
        if final_sentence [0] in singular_determiners:
            assert final_sentence [0] in singular_determiners
        elif final_sentence [0] in plural_determiners:
            assert final_sentence [0] in plural_determiners
        if final_sentence [1] in singular_noun:
            assert final_sentence [1] in singular_noun
        elif final_sentence [1] in plural_noun:
            assert final_sentence [1] in plural_noun
        if final_sentence [2] in past_verb:
            assert final_sentence [2] in past_verb
        elif final_sentence [2] in present_single_verb:
            assert final_sentence [2] in present_single_verb
        elif final_sentence [2] in present_plural_verb:
            assert final_sentence in present_plural_verb
        elif final_sentence [2] in future_verb:
            assert final_sentence [2] in future_verb
        elif final_sentence [3] in prep_phrases:
            assert final_sentence [3] in prep_phrases
        if final_sentence [4] in singular_determiners:
            assert final_sentence [4] in singular_determiners
        elif final_sentence [4] in plural_determiners:
            assert final_sentence [4] in plural_determiners
        if final_sentence [5] in singular_noun:
            assert final_sentence [5] in singular_noun 
        elif final_sentence [5] in plural_noun:
            assert final_sentence [5] in plural_noun
    
    for _ in range(4):

        sentence = get_prepositional_phrase(0, "future")
        final_sentence = sentence.split(' ')
        if final_sentence[3] in prep_phrases:
            assert final_sentence [3] in prep_phrases
        if final_sentence [0] in singular_determiners:
            assert final_sentence [0] in singular_determiners
        elif final_sentence [0] in plural_determiners:
            assert final_sentence [0] in plural_determiners
        if final_sentence [1] in singular_noun:
            assert final_sentence [1] in singular_noun
        elif final_sentence [1] in plural_noun:
            assert final_sentence [1] in plural_noun
        if final_sentence [2] in past_verb:
            assert final_sentence [2] in past_verb
        elif final_sentence [2] in present_single_verb:
            assert final_sentence [2] in present_single_verb
        elif final_sentence [2] in present_plural_verb:
            assert final_sentence in present_plural_verb
        elif final_sentence [2] in future_verb:
            assert final_sentence [2] in future_verb
        if final_sentence [4] in singular_determiners:
            assert final_sentence [4] in singular_determiners
        elif final_sentence [4] in plural_determiners:
            assert final_sentence [4] in plural_determiners
        if final_sentence [5] in singular_noun:
            assert final_sentence [5] in singular_noun 
        elif final_sentence [5] in plural_noun:
            assert final_sentence [5] in plural_noun
        
   

   
   

    # sentence = get_prepositional_phrase(1, "present").split(' ')
    # assert sentence in get_prepositional_phrase(1, "present")

    # sentence = get_prepositional_phrase(0, "present").split(' ')
    # assert sentence in get_prepositional_phrase(0, "present")

    # sentence = get_prepositional_phrase(0, "future").split(' ')
    # assert sentence in get_prepositional_phrase(0, "future")

    # sentence = get_prepositional_phrase(1, "future").split(' ')
    # assert sentence in get_prepositional_phrase(1, "future")

    

    
pytest.main(["-v", "--tb=line", "-rN", "test_sentences.py"])