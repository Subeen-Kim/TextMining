import wikipedia
import math

def text_to_word(text):
    text = text.replace('-',' ')
    text = text.replace('(','')
    text = text.replace(')','')
    text = text.replace("'",'')
    text = text.replace(".",'')
    text = text.replace(",",'')
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

def matching_summary(search_1,search_2):
    print ('Common words in the summary of', search_1,'&', search_2)

    text_1 = text_to_word(wikipedia.summary(search_1))
    text_2 = text_to_word(wikipedia.summary(search_2))
    histogram_1 = histogram(text_1)
    histogram_2 = histogram(text_2)

    preposition = ['as','by','in','at','on','with','of','for','to','through','after','from','over','until','during','under','all']
    pronoun = ['i','me','my','he','his','him','she','her','hers','we','our','ours','it','its','they','them','their']
    number = ['one','two','three','four','five','first','second','third']
    article = ['also','an','a','the','non','most']
    commonverb = ['is','are','was','were','be','been','have','has','had','get','got','gotten','can','could','make','made']
    alphabet = ['a','b','c','d','e','g','f','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','–','&']
    conjunction = ['and','but','or','yet','that','which','where','what','when','why','how']

    common_count = dict()
    for word in text_1:
        geometric_mean = math.sqrt(histogram_1.get(word, 0)*histogram_2.get(word, 0))
        if geometric_mean != 0:
            if word not in preposition and word not in pronoun and word not in article and word not in commonverb and word not in alphabet and word not in conjunction and word not in number:
                common_count[word] = geometric_mean

    return common_count

import matplotlib.pyplot as plt

word1 = input('1st word: ')
word2 = input('2nd word: ')
forxlabel = 'Common Words in Wikipedia Summary: ' + word1 + ' & ' + word2
forylabel = 'Geometric Mean of Frequencey'

dictionary = matching_summary(word1,word2)
fig = plt.figure()
plt.bar(range(len(dictionary)), dictionary.values(), align='center')
plt.xticks(range(len(dictionary)), dictionary.keys(), rotation=80)
plt.xlabel(forxlabel)
plt.ylabel(forylabel)
plt.show()

fig.savefig('image',dpi=600,bbox_inches='tight')
