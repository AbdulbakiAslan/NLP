# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import re
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

from gensim.models import Word2Vec
from gensim.utils import simple_preprocess

# veri seti yükleme 

df = pd.read_csv("IMDB Dataset.csv")
documets = df["review"]

# metin temizleme 
def clean_text(text):
    text = text.lower() #kucuk harf yap
    text = re.sub(r"\d+","", text) #sayiları temizle
    text = re.sub(r"[^\w\s]","",text ) #özel karakterleri temizleme
    text = " ".join([word for word in text.split() if len(word)>2])
    
    
    return text

# clean_text("asdasdas ASDASD 15554 %&/ I SELaM")

cleaned_documents = [clean_text(doc) for doc in documets]

#metin tokenization

tokenized_documents = [simple_preprocess(doc) for doc in cleaned_documents]


# %%

#word2Vec modeli tanımla 
model = Word2Vec(sentences = tokenized_documents, vector_size=50, window=5,min_count=1,sg=0)
word_vectors = model.wv

words = list(word_vectors.index_to_key)[:500]
vectors = [word_vectors[word] for word in words]





# clustring KMeans K=2

kmeans = KMeans(n_clusters=2)
kmeans.fit(vectors)
clusters = kmeans.labels_



#PCA 50 -> 2 

pca = PCA(n_components=2)
reduced_vectors = pca.fit_transform(vectors)



# 2 boyutlu görselleştirme 
plt.scatter(reduced_vectors[:,0], reduced_vectors[:,1], c = clusters, cmap="viridis")

centers = pca.transform(kmeans.cluster_centers_)
plt.scatter(centers[:,0], centers[:,1], c = "red", marker = "x", s=130, label = "Center")
plt.legend()


#Ifigure üzerine kelimelerin eklenmesi

for i, word in enumerate(words):
    plt.text(reduced_vectors[i,0], reduced_vectors[i,1], word, fontsize=7)

plt.title("Word2Vec")    




