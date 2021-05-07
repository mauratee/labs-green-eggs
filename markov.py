"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    opened_file = open(file_path).read()
    
    return opened_file

# working_file = open_and_read_file('green-eggs.txt')
# print(working_file)


example_dict = {('a', 'fox?'): ['Would'], # from assignment notes, will be used to check dictionary contents below
 ('Sam', 'I'): ['am?'],
 ('could', 'you'): ['in', 'with', 'in', 'with'],
 ('you', 'with'): ['a', 'a'],
 ('box?', 'Would'): ['you'],
 ('ham?', 'Would'): ['you'],
 ('you', 'in'): ['a', 'a'],
 ('a', 'house?'): ['Would'],
 ('like', 'green'): ['eggs'],
 ('like', 'them,'): ['Sam'],
 ('and', 'ham?'): ['Would'],
 ('Would', 'you'): ['could', 'could', 'could', 'could', 'like', 'like'],
 ('you', 'could'): ['you', 'you', 'you', 'you'],
 ('a', 'mouse?'): ['Would'],
 ('them,', 'Sam'): ['I'],
 ('in', 'a'): ['house?', 'box?'],
 ('with', 'a'): ['mouse?', 'fox?'],
 ('house?', 'Would'): ['you'],
 ('a', 'box?'): ['Would'],
 ('green', 'eggs'): ['and'],
 ('you', 'like'): ['green', 'them,'],
 ('mouse?', 'Would'): ['you'],
 ('fox?', 'Would'): ['you'],
 ('eggs', 'and'): ['ham?']
}


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.
    For example:
        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:
        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:
        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {} # create empty dictionary to hold keys and values
    word = text_string.split() # take 'test-string' parameter and apply .split method. 
                               #  Assign output to variable "word"
    
    for i in range(len(word) - 2): # Iterate through "word" list and stop two words from end

        key = (word[i], word[i + 1]) # Assign "key" to tuple with "i-th" word and "i+1-th" word
        value = [] #appending new words value list (see below)
        

        if chains.get(key) is not None: # Check if current key already exists in dictionary "chains"
            chains[key].append(word[i + 2])  # If key exists, append next word after tuple to value in dict
        else: # If key not in dictionary "chains"
            value.append(word[i + 2]) # Append next word after tuple to list "value"
            chains[key] = value # Assign tuple to dictionary "chains" as key and assign value list to 
                                # dictionary as value

    return(chains) # Return dictionary "chains"
        

# test_function = make_chains(working_file) # Pass "working file" through function "make_chains"
# print(f'dictionary of word chains = {test_function}') # Print resulting dictionary

# Test below is to see if dictionary returned from make_chains function matches example dictionary
# if test_function == example_dict:
#     print('it matches')

import random # import random module

def make_text(chains): # define new function to create Markov chain
    """Take input as dictionary, return text of newly generated Markov chain."""

    link_words = [] # Create empty list to hold Markov chain words
    length = len(chains) # Assign variable to number of keys in dictionary "chains"

    rand_key = (random.choice(list(chains))) # Assign variable to randomly chosen key from
                                             # dictionary "chains"
    # print(f'rand key = {rand_key}') # Print random key
    link_words.extend(rand_key) # Add contents of tuple, "rand_key" to list "link_words"
    
    random_value = random.choice(chains[rand_key]) # Assign variable to randomly chosen value
                                                   # from list of value at location of 'rand_key'
    # print(f'rand value = {random_value}') # Print random value
    link_words.append(random_value) # Append random value to Markov chain list

    # print(f'link = {link_words}') # Print list of Markov chain words

    # Create function to continuously generate new keys and check if ket exists in dictionary
    def create_new_key(Markov_chain_list):
        """ Take input as Markov chain word list, return list or None.
        
            Create new key from Markov chain list, check if new key in dictionary,
            if so, append random value from new key value list of dictionary to Markov
            chain list.
            
            If key not in dictionary, return None"""

        new_key = (Markov_chain_list[-2], Markov_chain_list[-1])
        # print(f'new_key = {new_key}')
        if new_key in chains:
            new_word = random.choice(chains[new_key])
            link_words.append(new_word)
            #print(f'link words = {link_words}')
            return link_words
        else:
            return None
    
    # link_plus = create_new_key(link_words) 
    # print(f'link plus = {link_plus}')

    while create_new_key(link_words) is not None: # While create_new_key is not returning None,
        create_new_key(link_words) # Re-run function to create new key and append to link_words
    

    return ' '.join(link_words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
