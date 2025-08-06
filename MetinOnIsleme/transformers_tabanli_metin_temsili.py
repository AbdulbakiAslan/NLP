#import libraries 

from transformers import AutoTokenizer, AutoModel
import torch


#model ve tokenizer yukle 

model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

#input text (metni) tanımlama

text = "Transformers can be used for naturel language procressing."

#metni tokenlara çevirmek
inputs = tokenizer(text, return_tensors="pt") # cıktı pytorch tensoru olarak return edilir

with torch.no_grad(): #gradyanların hesaplanması durdurulur, boylece belleği daha verimli kullanırız
    outputs = model(**inputs)
    
#modelin çıkısından son gizli durum alalim
    
last_hidden_state = outputs.last_hidden_state# tum toekn ciktılarını lamak icin

#ilk tokenin embedding inin alalim ve print edelim
first_token_embedding = last_hidden_state[0,0,:].numpy()

print(f"Metnin temsili: {first_token_embedding}")