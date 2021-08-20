import string

from typing import List

STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves',
             'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself',
             'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers',
             'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs',
             'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll",
             'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been',
             'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against',
             'between', 'into', 'through', 'during', 'before', 'after', 'above',
             'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over',
             'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when',
             'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',
             'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own',
             'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just',
             'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o',
             're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't",
             'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn',
             "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't",
             'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't",
             'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't",
             'won', "won't", 'wouldn', "wouldn't"]

with open('the_great_gatsby.txt', encoding='utf-8') as f:
    contents = f.read()

translator = str.maketrans('', '', string.punctuation)
no_punctuation = contents.translate(translator)
no_punctuation = no_punctuation.lower()
words = no_punctuation.split(' ')

words_dict = {}
user_word = input("Enter a word to look for: ")


for word in words:
    if word in STOPWORDS:
        continue
    elif word in words_dict:
        words_dict[word] += 1
    elif word not in words_dict:
        words_dict[word] = 1

words = list(words_dict.items())  # .items() returns a list of tuples
# sort largest to smallest, based on count
words.sort(key=lambda tup: tup[1], reverse=True)
# print the top 10 words, or all of them, whichever is smaller
for i in range(min(10, len(words))):
    print(words[i])
