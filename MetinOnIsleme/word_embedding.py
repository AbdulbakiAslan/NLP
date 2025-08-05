"""
word2Vec (google)
fasttext(meta- facebook)
"""


#import libraries
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA #principle component analysis: 
    #boyutu indirgiyoruz ve daha rahat şekilde görülebilir oluyor dimension reduaction
    
from gensim.models import Word2Vec, FastText
from gensim.utils import simple_preprocess
#ornek veri seti oluştur
sentences = [
    
    "Köpek çok tatlı bir hayvandır.",
    "Köpekler evcil hayvanlardır.",
    "Kediler genellikle bağımsız haraket etmeyi severler",
    "Köpekler sadık ve dost canlısı hayvanlardır.",
    "Hayvanlar insnlar için iyi arkadaşlardır."
    ]

tokanized_sentences = [simple_preprocess(sentence) for sentence in sentences]

#word2vec


word2_vec_model = Word2Vec(sentences = tokanized_sentences, vector_size=50, window=5, min_count=1, sg=0)



#fasttext

fasttext_model = FastText(sentences=tokanized_sentences,vector_size=50,window=5,min_count=1,sg=0)


# gorselleştirme : PCA

def plot_word_embedding(model,title):
    word_vectors = model.wv
    
    words = list(word_vectors.index_to_key)
    vectors = [word_vectors[word] for word in words]
    
    #pca
    pca = PCA(n_components=3)
    reduced_vectors = pca.fit_transform(vectors)
    
    #3d gorselleştirme
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111,projection = "3d")
    
    #vektörleriz çiz
    ax.scatter(reduced_vectors[:,0],reduced_vectors[:,1], reduced_vectors[:,2])
    
    #kelimeleri etiketle
    for i, word in enumerate(words):
        ax.text(reduced_vectors[i,0],reduced_vectors[i,1],reduced_vectors[i,2],word, fontsize = 12)
    
    ax.set_title(title)
    ax.set_xlabel("Component 1")
    ax.set_ylabel("Component 2")
    ax.set_zlabel("Component 3")
    plt.show()
        
plot_word_embedding(word2_vec_model, "Word2Vec")   
plot_word_embedding(fasttext_model, "FastText")         