import nltk #naturel language toolkit


nltk.download("punkt") # metni kelime ve cumle bazinda tokenlara ayırab,lmek icin 
#veya nltk.download("punkt_tab")


text = "Hello, World! How are you? Hello, hi ..."

# kelime tokenizasyonu  word_tokanize : metni kelimelre çevirir, 
# noktalama işaretleri ve boşluklar  ayri birer token olarak elde edilecektir.

word_tokens = nltk.wordpunct_tokenize(text)





#cümle tokenizasyonu : sent_tokenize: metni cümlelere ayırır. her bir cümle token olur

setence_tokens = nltk.sent_tokenize(text)