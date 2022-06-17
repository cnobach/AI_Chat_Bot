import nltk
from nltk.stem.porter import PorterStemmer
import numpy as np

# Uncomment below if first time running program, comment back after
# nltk.download('punkt')


# Tokenizes the sentence and returns the list
def tokenize(sentence):
    return nltk.word_tokenize(sentence)

# Stems a word and returns it (lowercase)
def stem(word):
    stemmer = PorterStemmer()
    return stemmer.stem(word.lower())

def bag_of_words(tokenized, all_words):
    # Stem all wokenized words
    tokenized = [stem(word) for word in tokenized]
    # Create the bag with zeroes
    bag = np.zeros(len(all_words), dtype=np.float32)
    # Loop all words
    for i, word in enumerate(all_words):
        # If the word exists in the tokenized sentence, put a 1 in the index of the bag
        if word in tokenized:
            bag[i] = 1.0
    
    return bag