import nltk

nltk.download("wordnet") # lemmaziation ,işlemi için gerekli veri tabanı 

from nltk.stem import PorterStemmer # stemming için foksiyon 

# porter stemmer nesnesini oluştur 

stemmer = PorterStemmer()

words = ["running","runner","ran", "runs", "better", "go", "went"]


#kelimelerin stem'lerini buluyoruz, bunu yaparken de porter stemmer in stem() fonksiyonunu kullanıyoruz
stems = [stemmer.stem(w) for w in words]

print(f"Stems: {stems}")

#%% lemmatization


from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

words = ["running","runner","ran", "runs", "better", "go", "went"]

lemmas = [lemmatizer.lemmatize(w, pos="v") for w in words]

print(f"Lemmas: {lemmas}")

