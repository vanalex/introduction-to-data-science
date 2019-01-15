#Loading the data set - training data.
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import numpy as np


twenty_train = fetch_20newsgroups(subset='train', shuffle=True)

# You can check the target names (categories) and some data files by following commands.
print(twenty_train.target_names) #prints all the categories

print("\n".join(twenty_train.data[0].split("\n")[:3])) #prints first line of the first data file


# Extracting features from text files
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
print(X_train_counts.shape)


tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print(X_train_tfidf.shape)

# Machine Learning
# Training Naive Bayes (NB) classifier on training data.
clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)
print(clf)


# Building a pipeline: We can write less code and do all of the above, by building a pipeline as follows:
# The names ‘vect’ , ‘tfidf’ and ‘clf’ are arbitrary but will be used later.
# We will be using the 'text_clf' going forward.
text_clf = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', MultinomialNB())])
text_clf = text_clf.fit(twenty_train.data, twenty_train.target)

#Performance of NB classifier
twenty_test = fetch_20newsgroups(subset='test', shuffle=True)
predicted = text_clf.predict(twenty_test.data)
print(np.mean(predicted == twenty_test.target))