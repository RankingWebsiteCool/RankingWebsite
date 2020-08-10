from jellyfish import porter_stem, match_rating_codex, levenshtein_distance
from nltk.corpus import stopwords
from unicodedata import normalize, category
import re
import numpy as np

stop_words = set(stopwords.words('english'))
punctuation = [':', ',', '-']

def stripAccents(s):
   return ''.join(c for c in normalize('NFD', s) if category(c) != 'Mn')

def representString(input_string : str):
    if type(input_string) != str: return
    input_string = stripAccents(input_string) # remove accents
    word_array = re.findall('[a-zA-Z]+', input_string) # only get letters
    word_array = [word.lower() for word in word_array] # make lower case
    word_array = [word for word in word_array if not word in stop_words] # remove stop words
    word_array = [porter_stem(word) for word in word_array] # get stems of words
    word_array = [match_rating_codex(word) for word in word_array] # shorten words
    return word_array

def queryStringDistance(query_string : str, database_string : str):
    top_three_matches = np.ndarray(3, dtype = np.float32)
    top_three_matches.fill(np.inf)
    for word in query_string:
        best_match = np.inf
        for match_word in database_string:
            match = levenshtein_distance(word, match_word)
            if match < best_match : best_match = match
        max_match_ind = top_three_matches.argmax()
        if best_match < top_three_matches[max_match_ind]:
            top_three_matches[max_match_ind] = best_match
    return np.mean([match for match in top_three_matches if not np.isinf(match)])

if __name__ == '__main__':
    # Represent strings
    input_string = 'The good, the bad and the ugly'
    input_words = representString(input_string)
    print(input_words)
    different_string = 'Bodger and Badger'
    different_words = representString(different_string)
    print(representString(different_string))
    similiar_string = 'God Baad En OOGLI'
    similiar_words = representString(similiar_string)
    print(similiar_words)
    # Make comparisons
    print(queryStringDistance(input_words, different_words))
    print(queryStringDistance(input_words, similiar_words))