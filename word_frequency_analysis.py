import string
# print(string.punctuation)
# print(string.whitespace)

# mydict = {}

# for char in string.punctuation:
#     mydict[char] = None

# print(mydict)

def word_list_from_file(filepath):
    file = open(filepath)
    wordlist = []
    headerinfo = True
    for line in file:
        line = line.strip()
        if line == "CHAPTER I.":
            headerinfo = False
        if headerinfo == True:
            continue
        line = line.replace('-', ' ')
        line = line.translate(line.maketrans('', '', string.punctuation))
        line = line.replace('“', '')
        line = line.replace('”', '')
        line = line.replace('”', '')
        line = line.replace('’', '')
        line = line.replace('‘', '')
        line = line.replace('—', ' ')
        line = line.replace('  ', ' ')
        line = line.lower()
        line = line.split(" ")
        wordlist = wordlist + line
        wordlist = list(filter(None, wordlist))
        if line == ['the', 'end']:
            return wordlist
        
storywordlist = word_list_from_file('alice-in-wonderland.txt')


def word_frequency_histogram(wordlist):
    allwords = open('words.txt')
    wordhist = {}
    for word in allwords:
        wordhist[word.strip()] = 0
    for word in wordlist:
        if word in wordhist:
            wordhist[word] += 1
    bookwordhist = {'Total Words': len(wordlist)}
    for word in wordhist:
        if wordhist[word] > 0:
            bookwordhist[word] = wordhist[word]

    return(bookwordhist)

wordfreqhist = word_frequency_histogram(storywordlist)

def highest_values_dict(dictionary):
    dictionarycopy = dictionary.copy()
    high_value_dict = {}
    for x in range(20):
        dictionarycopy[max(dictionarycopy, key=dictionarycopy.get)] = 0
        high_value_dict[max(dictionarycopy, key=dictionarycopy.get)] = dictionarycopy[max(dictionarycopy, key=dictionarycopy.get)]
    return high_value_dict


most_common_words_dict = highest_values_dict(wordfreqhist)
# print(most_common_words_dict)

def checkForTypos(file):
    wordlist = word_list_from_file(file)
    allwords = open('words.txt')
    typoshist = {}
    wordhist = {}
    for word in allwords:
        wordhist[word.strip()] = 0
    for word in wordlist:
        if word not in wordhist:
            if word not in typoshist:
                typoshist[word] = 1
            else: typoshist[word] +=1
    print(typoshist)

checkForTypos('alice-in-wonderland.txt')