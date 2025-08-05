"""
word2Vec (google)
fasttext(meta- facebook)
"""


#import libraries
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA #principle component analysis: 
    #boyutu indirgiyoruz ve daha rahat şekilde görülebilir oluyor dimension reduaction
    
from gensim.models import word2Vec
from gensim.utils import simple_preprocess
#ornek veri seti oluştur
sentences = [
    
    "Köpek çok tatlı bir hayvandır.",
    "Köpekler evcil hayvanlardır.",
    "Kediler genellikle bağımsız haraket etmeyi severler",
    "Köpekler sadık ve dost canlısı hayvanlardır.",
    "Hayvanlar insnlar için iyi arkadaşlardır."
    
    
    ]

#word2vec


#fasttext



# gorselleştirme : PCA