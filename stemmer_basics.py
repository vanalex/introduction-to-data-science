from nltk.stem import PorterStemmer, WordNetLemmatizer, LancasterStemmer
from nltk import pos_tag
from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()
lemmatiser = WordNetLemmatizer()
lancaster = LancasterStemmer()

print("Porter Stemmer")
print(stemmer.stem("cats"))
print(stemmer.stem("trouble"))
print(stemmer.stem("troubling"))
print(stemmer.stem("troubled"))
print("Lancaster Stemmer")
print(lancaster.stem("cats"))
print(lancaster.stem("trouble"))
print(lancaster.stem("troubling"))
print(lancaster.stem("troubled"))

print("Stem %s: %s" % ("studying", stemmer.stem("studying")))
print("Lemmatise %s: %s" % ("studying", lemmatiser.lemmatize("studying")))
print("Lemmatise %s: %s" % ("studying", lemmatiser.lemmatize("studying", pos="a")))

s = "It is too cold outside"
tokens = word_tokenize(s)  # Generate list of tokens
tokens_pos = pos_tag(tokens)

print(tokens_pos)

#A list of words to be stemmed
word_list = ["friend", "friendship", "friends", "friendships","stabil","destabilize","misunderstanding","railroad","moonlight","football"]
print("{0:20}{1:20}{2:20}".format("Word","Porter Stemmer","lancaster Stemmer"))
for word in word_list:
    print("{0:20}{1:20}{2:20}".format(word,stemmer.stem(word),lancaster.stem(word)))

sentence="Pythoners are very intelligent and work very pythonly and now they are pythoning their way to success."


def stemSentence(sentence):
    token_words=word_tokenize(sentence)
    token_words
    stem_sentence=[]
    for word in token_words:
        stem_sentence.append(stemmer.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)


x = stemSentence(sentence)
print(x)

file=open("text")
my_lines_list=file.readlines()
print('text ===> ', my_lines_list)

print(my_lines_list[0])
print('stemmed sentence')
stemmedsentence = stemSentence(my_lines_list[0])
print(stemmedsentence)