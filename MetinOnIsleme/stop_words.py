import nltk

from nltk.corpus import stopwords

nltk.download("stopwords") # farklı dillerde en çok kullanılan stop words içeren veri seti



# ingilizce stop words analizi   (nltk)
stop_words_eng = set (stopwords.words("english"))

# ornek ingilizce metin

text = "There are some examples of handling stop words from some texts."
text_list = text.split()
#eğer word ingilizce stop word listesinde (stop_words_eng) yoksa, bu kelimeyi filtrelenmiş listeye ekliyoruz. 
filtred_words = [word for word in text_list if word.lower() not in stop_words_eng]
print(f"filtred_words: {filtred_words}")


#%% türkçe stop words analizi (nltk)
stop_words_tr = set(stopwords.words("turkish"))
metin = " merhaba arkadaslar çok güzel bir ders işliyoruz. Bu ders faydalı mı ?"
# veri temizleme muhakkak yapılmalı diğer türlü net olarak çalışmaz mı ile ? birleşik olsa algılıyamazdı. 
metin_list = metin.split()

filtred_words_tr = [word for word in metin_list if word.lower() not in stop_words_tr]




#%%  kütüphanesiz stop words cikarimi

#stopword listesi oluştur
tr_stopwords = ["için","bu","ile","mu","mi","özel"]

#örnek türkçe metin
metin = "Bu bir denemedir. Amacimiz bu metinde bulunan özel karakterleri elemek mi acaba?"

filtered_words = [word for word in metin.split() if word.lower() not in tr_stopwords]
filtered_stop_words = set([word.lower() for word in metin.split() if word.lower() in tr_stopwords])

print(f"filtered_words: {filtered_words}")