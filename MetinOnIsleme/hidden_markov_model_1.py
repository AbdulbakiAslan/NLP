"""

Part of Speech POS : kelimelerin uygun sozcuk turunu bulma calisması
HMM

I (zamir) a teacher(isim)
"""


#import libraries 
import nltk
from nltk.tag import hmm




#ornek training data tanımla

train_data =[
    [("I","PRP"),("am","VBP"),("a","DT"),("teacher","NN")],    
    [("You","PRP"),("are","VBP"),("a","DT"),("student","NN")]
    ]


#train HMM
trainer = hmm.HiddenMarkovModelTrainer()

hmm_tagger = trainer.train(train_data)


# yeni cumle olustur ve icindeki her bir sozcuğun turunu etiketle

test_sentence = "I am a student".split()

tags = hmm_tagger.tag(test_sentence)
print(f"Yeni cumle: {tags}")

"""

Yeni cumle: [('I', 'PRP'), ('am', 'VBP'), ('a', 'DT'), ('student', 'NN')]

"""


test_sentence = "He is a driver".split()

tags = hmm_tagger.tag(test_sentence)
print(f"Yeni cumle: {tags}")

"""

Yeni cumle: [('He', 'PRP'), ('is', 'PRP'), ('a', 'PRP'), ('driver', 'PRP')]
data büyük olmadığı için çokça yanlış yapıyor. 

"""