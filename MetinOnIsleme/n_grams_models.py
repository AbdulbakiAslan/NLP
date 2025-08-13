#import libraries 

import nltk
from nltk.util import ngrams #ngram modeli için
from nltk.tokenize import word_tokenize #tokenizasyon için
from collections import Counter


# ornek veri seti olustur 

corpus = [
    "I love apple",
    "I love him",
    "I love NLP",
    "You love me",
    "He lowes apple",
    "They love apple",
    "I love you and you love me"
    ]

#verileri tokenize hale getir 
tokens = [word_tokenize(sentence.lower()) for sentence in corpus]


# bigram

bigrams = []
for token_list in tokens: 
    bigrams.extend(list(ngrams(token_list, 2)))

bigrams_freq = Counter(bigrams)

#trigram
trigrams =[]
for token_list in tokens:
    trigrams.extend(list(ngrams(token_list, 3)))

trigram_freq = Counter(trigrams)


#model testing

#I love bigramından sonra "you" veya "apple" kellimelerinin gelme olasılıklarını hesaplayalım

bigram = ("i","love") # hedef bigram
#"i love you" olma olasılıgı
prob_you = trigram_freq[("i","love","you")]/bigrams_freq[bigram]

print(f"you kelimesinin gelme olasılığı: {prob_you}")

# i love apple olma olasılığı 
prob_apple = trigram_freq[("i","love","you")]/bigrams_freq[bigram]
print(f"apple kelimesinin gelme olasılığı: {prob_apple}")
