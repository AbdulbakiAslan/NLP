#import libraries

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import re 
from collections import Counter

df = pd.read_csv("IMDB Dataset.csv")

# metin verilerini alalım
documents = df["review"]
labels = df["sentiment"] #positive veya negative



# metin temizleme

def clean_text(text):
    
    # buyuk kucuk harf cevrimi
    text = text.lower()
    #rakamları temizleme
    text = re.sub(r"\d+", "",text)
    # ozel karakterlerin kalkması
    text = re.sub(r"[^\w\s]", "",text)

    # kısa kelimelerin temizlenmesi
    text = " ".join([word for word in text.split() if len(word) > 2 ])
    return text #temizlenmiş text'i return et
    
#metinleri temizle 

clean_doc = [clean_text(row) for row in documents ]   
#%% bow
#cevtorizer tanımla
vectorizer = CountVectorizer()


# metin -> sayısal hale getir
X = vectorizer.fit_transform(clean_doc[:75])
# kelime kümesi göster
feature_names = vectorizer.get_feature_names_out()

# vektör temsili göster 
vektor_temsili2 = X.toarray()
print(f"vektor temsili: {vektor_temsili2}")

df_bow = pd.DataFrame(vektor_temsili2, columns = feature_names)

# kelime frekanslarını göster 

word_counts = X.sum(axis=0).A1
word_freq = dict(zip(feature_names,word_counts))

#ilk 5 kelimeyi yazdır

most_common_5_words = Counter(word_counts).most_common(5)