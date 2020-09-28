import nltk
import codecs
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def printBTgram(filtered_tokens):
    bigrm = nltk.bigrams(filtered_tokens)
    trigrm = nltk.trigrams(filtered_tokens)
    bigrmFreqDist = nltk.FreqDist(bigrm)
    trigrmFreqDist = nltk.FreqDist(trigrm)

    print("Below is the most frequent 10 bigrams")
    for i in bigrmFreqDist.most_common(10):
        print(i)
    print("\nBelow is the most frequent 10 trigrams")
    for i in trigrmFreqDist.most_common(10):
        print(i)

f=codecs.open('text.txt',encoding='utf8')
lines = f.readlines()
all_text=' '.join(lines).lower()
tokens = nltk.word_tokenize(all_text)
print("Before removal, there are ", len(tokens)," number of tokens\n")

tokenizer= nltk.RegexpTokenizer('\w+')
tokens = tokenizer.tokenize(all_text)
english_stopwords = stopwords.words('english')
stopwords_set = set(english_stopwords)
filtered_tokens = [w for w in tokens if w not in english_stopwords]

print("After removal, There are ",len(filtered_tokens), " number of tokens")
print("There are ",len(set(filtered_tokens))," number of word types\n")
printBTgram(filtered_tokens)

print("\n Now the lemmatizer begins\n")
lemmatizer = WordNetLemmatizer()
for token in filtered_tokens:
    token = lemmatizer.lemmatize(token)
printBTgram(filtered_tokens)





