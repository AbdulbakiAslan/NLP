# -------------------------------
# Kütüphaneleri içe aktar
# -------------------------------
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import os


# Eğer spam.csv bu dizinde değilse, tam yolu ver:
# df = pd.read_csv(r"C:\Users\fizibil\NLP\MetinOnIsleme\spam.csv", encoding="latin1")

# -------------------------------
# Veri setini oku
# Kaggle'dan gelen spam.csv genelde UTF-8 değildir, Latin1 veya cp1252 olur
# -------------------------------
df = pd.read_csv("spam.csv", encoding="latin1")

# -------------------------------
# DataFrame'i incele
# -------------------------------
print("İlk 5 satır:")
print(df.head())

print("Sütun isimleri:", df.columns.tolist())

# Kaggle spam.csv genelde 'v1' = label (ham/spam), 'v2' = mesaj metni
# Eğer df.text yoksa, v2 sütununu TF-IDF'e vereceğiz
text_column = 'text' if 'text' in df.columns else 'v2'

# -------------------------------
# TF-IDF Vektörizasyon
# -------------------------------
vectorizer = TfidfVectorizer()

# fit_transform: metinleri sayısal TF-IDF matrisine dönüştürür
X = vectorizer.fit_transform(df[text_column])

# -------------------------------
# Özellik isimlerini (kelime kümesi) al
# -------------------------------
feature_names = vectorizer.get_feature_names_out()
print("Kelime sayısı:", len(feature_names))

# -------------------------------
# TF-IDF Skorlarını DataFrame'e dönüştür
# -------------------------------
tfidf_df = pd.DataFrame(X.toarray(), columns=feature_names)

print("TF-IDF matris boyutu:", tfidf_df.shape)
print("İlk 5 satır TF-IDF skoru:")
print(tfidf_df.head())
