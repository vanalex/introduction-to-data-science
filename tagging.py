import nltk
from nltk.corpus import brown


nltk.download('brown')
nltk.help.upenn_tagset('RB')
nltk.help.upenn_tagset('NN')

text = nltk.word_tokenize("And now for something completely different")
print(nltk.pos_tag(text))

text = nltk.word_tokenize("They refuse to permit us to obtain the refuse permit")
print(nltk.pos_tag(text))
print(nltk.corpus.brown.words())
print('===========================================================')
text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
text.similar('woman')
print('============================================================')

tagged_token = nltk.tag.str2tuple('fly/NN')
print(tagged_token)
print(tagged_token[0], tagged_token[1])

sent = '''
... The/AT grand/JJ jury/NN commented/VBD on/IN a/AT number/NN of/IN
... other/AP topics/NNS ,/, AMONG/IN them/PPO the/AT Atlanta/NP and/CC
... Fulton/NP-tl County/NN-tl purchasing/VBG departments/NNS which/WDT it/PPS
... said/VBD ``/`` ARE/BER well/QL operated/VBN and/CC follow/VB generally/RB
... accepted/VBN practices/NNS which/WDT inure/VB to/IN the/AT best/JJT
... interest/NN of/IN both/ABX governments/NNS ''/'' ./.
... '''

tagged_tokens = nltk.tag.str2tuple(sent)
print(tagged_tokens)


def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text
                                  if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].most_common(5)) for tag in cfd.conditions())


tagdict = findtags('NN', nltk.corpus.brown.tagged_words(categories='news'))
print('=================tagging the news corpora========================')
for tag in sorted(tagdict):
    print(tag, tagdict[tag])


def process(sentence):
    for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
        if (t1.startswith('V') and t2 == 'TO' and t3.startswith('V')):
            print(w1, w2, w3)


for tagged_sent in brown.tagged_sents():
     process(tagged_sent)
