# metinlerde bulunan fazla boşlukları ortadan kaldır

text = " Hello,    World!       2235"


cleaned_text1 = " ".join(text.split())
print(f"text: {text} \n cleaned_text1: {cleaned_text1}")
#%% Büyük --> küçük harf çevirimi
text = "Hello, World! 2235"
text.lower()    #kucuk harfe cevir
cleaned_text2 = text.lower()
print(f"text: {text} \n cleaned_text2: {cleaned_text2}")


# %% noktalama işaretlerini kaldır
import string
text = "Hello, World! 2035"

cleaned_text3= text.translate(str.maketrans("","" , string.punctuation))
print(f"text: {text} \n cleaned_text3: {cleaned_text3}")



#%%özel karakterleri kaldır
import re

text =  "Hello, World! 2035% "

cleaned_text4 = re.sub(r"[^A-Za-z0-9\s]","",text)
print(f"text: {text} \n cleaned_text4: {cleaned_text4}")



#%%yazim hatalarini düzeltl

from textblob import TextBlob # metin analizindeki kütüphane

text = "Hellko, Wurld! 2035"
cleaned_text5 = TextBlob(text).correct()#hataları düzeltir

print(f"text: {text} \n cleaned_text5: {cleaned_text5}")



#%% html ya da url etiketlerini kalir


from bs4 import BeautifulSoup
html_text = "<div>Hello, World! 2035</div>"

# beatiful soup ile html yapısını pars et, get text ile text kısmını çek 

cleaned_text6 = BeautifulSoup(html_text,"html.parser").getText()

print(f"text: {html_text} \n cleaned_text6: {cleaned_text6}")



# %% ÖDEV -- deneme

import string
import re
from textblob import TextBlob
from bs4 import BeautifulSoup
text2 = "Abi nden BuNUn Nedeni neir ki 1111??!! "
cleaned_text= " ".join(text2.split())
text2.lower()

cleaned_text6 = text2.lower()

cleaned_text6 = text2.translate(str.maketrans("","", string.punctuation))

cleaned_text6 = re.sub(r"[^A-Za-z0-9\s]","",text2)

cleaned_text6 = TextBlob(text2).correct()


print(cleaned_text6)