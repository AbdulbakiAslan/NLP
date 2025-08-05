# count vectorizer iceriye aktar 
from sklearn.feature_extraction.text import CountVectorizer

#veri seti oluştur 
doc = [
       "kedi bahçede",
       "kedi evde"]
# vectorizer tanımla 
vectorizer = CountVectorizer()
#metni sayısal vektorlere çevir 
X = vectorizer.fit_transform(doc)
#kelime kümesi oluşturma [bahcede, evde ,kedi]
feature_names = vectorizer.get_feature_names_out()
print(f"kelime kümesi : {feature_names}")

#vektor temsili

vector_temsili = X.toarray()

print(f"vector_temsili : {vector_temsili}")

"""

kelime kümesi : ['bahçede' 'evde' 'kedi']
vector_temsili : [[1 0 1]
 [0 1 1]]
"""