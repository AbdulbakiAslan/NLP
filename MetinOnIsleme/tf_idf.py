# import libraries
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

#ornek belge olustur 
documents =[
    "Köpek çok tatlı bir  hayvandır",
    "Köpekler ve kuşlar çok tatlı hayvanlardır.",
    "Inekler süt üretirler"
    ]
# vectorizer tanımla 
tfidf_vectorizer = TfidfVectorizer()
# metinleri sayısal hale çevir 
X = tfidf_vectorizer.fit_transform(documents)


# kelime kümesini incele 
featured_names = tfidf_vectorizer.get_feature_names_out()

#vektör temsilini incele 
vektor_temsili = X.toarray()
print(f"tf-idf: {vektor_temsili}")

df_tfidf = pd.DataFrame(vektor_temsili, columns=featured_names)
#ortalama tf idf değerlerine bakalım
tf_idf  = df_tfidf.mean(axis=0)