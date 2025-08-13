"""

classification problem : duygy analizi -> olumlu veya olumsuz olarak sınıfladırma

"""

#import libraries
from nltk.classify import MaxentClassifier

#veri seti tanımlama
train_data = [
    ({"love":True, "amazing": True, "happy": True,"terrible": False}, "positive" ),
    ({"hate": True, "terrible": True},"negative"),
    ({"joy": True, "happy": True, "hate":True},"possitive"),
    ({"sad": True, "depressed": True,"love":False}, "negative" )    
    ]

#train maximum etropy classifier 

classifier = MaxentClassifier.train(train_data, max_iter = 10)

# yeni cumle ile test et
test_sentence = "I love this movie and it was amazing "  #"I hate this movie and it was terrible"

features = {word:(word in test_sentence.lower().split()) for word in ["love", "amazing", "terrible", "happy", "joy"]}

label = classifier.classify(features)
print(f"Result: {label}")