
# 1. Write a program that reads a word list from a file (see Section 9.1) and prints all the sets of words that are anagrams.


def neglength(e):
    return -len(e)

def letters_to_words_dict(wordlistfile):
    wordlist = open(wordlistfile)
    dicta = {}
    
    for word in wordlist:
        wordtuple = tuple(sorted(word)[1:])
        if wordtuple not in dicta:
            dicta[wordtuple] = [word[:-1]]
        else:
            dicta[wordtuple].append(word[:-1])
    return dicta

letters_dict = letters_to_words_dict('words.txt')

def dict_only_values_length_over_1(dictionary):
    newdict = {}
    for key, value in dictionary.items():
        if len(value) > 1:
            newdict[key] = value
    return newdict

anagrams_dict = dict_only_values_length_over_1(letters_dict)



def anagram_sets():
    letters_dict = letters_to_words_dict('words.txt')
    anagrams_dict = dict_only_values_length_over_1(letters_dict)
    anagrams_list = list(anagrams_dict.values())
    for listy in anagrams_list:
        print(listy)

# anagram_sets()

# 2. Modify the previous program so that it prints the largest set of anagrams first,followed by the second largest set, and so on.
def sorted_values(dictionary):
    values = list(dictionary.values())
    values.sort(key=len)
    return values

def sorted_anagram_sets():
    letters_dict = letters_to_words_dict('words.txt')
    anagrams_dict = dict_only_values_length_over_1(letters_dict)
    anagrams_list = sorted_values(anagrams_dict)
    for listy in anagrams_list:
        print(listy)

sorted_anagram_sets()

# 3. In Scrabble a “bingo” is when you play all seven tiles in your rack, along with a letter on the board, to form an eight-letter word. What set of 8 letters forms the most possible bingos? Hint: there are seven.

# Here I assumed there may be more than one set of 8 letters


def only_keys_with_set_length(dictionary, length):
    new_dict = {}
    for key, value in dictionary.items():
        if len(key) == length:
            new_dict[key] = value
    return new_dict

def only_longest_list(listy):
    listy.sort(key = neglength)
    newlist = []
    length = 0
    for sublist in listy:
        if len(sublist) >= length:
            length = len(sublist)
            newlist.append(sublist)
    return newlist

def find_keys_from_valueslist(dictionary, valueslist):
    keyslist = []
    for value in valueslist:
        for key, val in dictionary.items():
            if val == value:
                keyslist.append(key) 
    return keyslist

def scrabble_bingo_letters():
    eightletterwordsdict = only_keys_with_set_length(anagrams_dict, 8)
    eightletteranagrams = sorted_values(eightletterwordsdict)
    mosteightletteranagrams = only_longest_list(eightletteranagrams)
    bingo_letters = find_keys_from_valueslist(anagrams_dict, mosteightletteranagrams)
    print(bingo_letters)

scrabble_bingo_letters()