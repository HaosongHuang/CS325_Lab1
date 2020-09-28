import codecs
from nltk.corpus import stopwords

f=codecs.open('text.txt',encoding='utf8')
lines = f.readlines()
for line in lines:
    print(line)
all_text=' '.join(lines).lower()
tokens = nltk.word_tokenize(all_text)
print(len(tokens))

fd = FreqDist(tokens)
fd.most_common(10)

tokenizer= RegexpTokenizer('\w+')
tokens = tokenizer.tokenize(all_text)
english_stopwords = stopwords.words('english')
stopwords_set = set(english_stopwords)
filtered_tokens = [w for w in tokens if w not in english_stopwords]


