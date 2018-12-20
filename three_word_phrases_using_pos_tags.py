import nltk
from nltk.corpus import brown
nltk.download('universal_tagset')


def process(sentence):
    for (w1, t1), (w2, t2), (w3, t3) in nltk.trigrams(sentence):
        if t1.startswith('V') and t2 == 'TO' and t3.startswith('V'):
            print(w1, w2, w3)


for tagged_sent in brown.tagged_sents():
    process(tagged_sent)


brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
data = nltk.ConditionalFreqDist((word.lower(), tag)
    for (word, tag) in brown_news_tagged)

for word in sorted(data.conditions()):
     if len(data[word]) > 3:
         tags = [tag for (tag, _) in data[word].most_common()]
         print(word, ' '.join(tags))
