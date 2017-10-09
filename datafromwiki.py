import wikipedia
import math

def text_to_word(text):
    text = text.replace('-',' ')
    text = text.replace('(','')
    text = text.replace(')','')
    text = text.replace("'",'')
    text = text.lower()
    list_of_unsorted = text.split()
    return list_of_unsorted

def histogram(unsorted_words):
    count = dict()
    for word in unsorted_words:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
    return count

#histogram(text_to_word('Subeen-is-(an)-idiot'))

def matching_summary():
    print ('Relationship between the given words will be presented')
    search_1 = input('1st word: ')
    search_2 = input('2nd word: ')
    text_1 = text_to_word(wikipedia.summary(search_1))
    text_2 = text_to_word(wikipedia.summary(search_2))
    histogram_1 = histogram(text_1)
    histogram_2 = histogram(text_2)

    common_count = dict()
    for word in text_1:
        geometric_mean = math.sqrt(histogram_1.get(word, 0)*histogram_2.get(word, 0))
        if geometric_mean != 0:
            common_count[word] = geometric_mean
        else:

    return common_count

matching_summary()
