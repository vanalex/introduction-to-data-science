from nltk.probability import ConditionalFreqDist
from nltk.tokenize import word_tokenize


sent = "the the the dog dog some other words that we do not care about"
cfdist = ConditionalFreqDist()

for word in word_tokenize(sent):
    condition = len(word)
    cfdist[condition][word] += 1

print(cfdist[3])
print(cfdist[3].freq('the'))
print(cfdist[3]['dog'])
print(cfdist.tabulate())