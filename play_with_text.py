import re;
import string
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS

input_lower_and_upper_case_str = 'The 5 biggest countries by population in 2017 are China, India, United States, Indonesia, and Brazil.'
input_lower_case_str = input_lower_and_upper_case_str.lower();
print(input_lower_case_str);

input_str ='Box A contains 3 red and 5 white balls, while Box B contains 4 red and 2 blue balls.';
result = re.sub(r'\d+', '', input_str)
print(result)

input_str = 'This &is [an] example? {of} string. with.? punctuation!!!!'
translator = str.maketrans('', '', string.punctuation)
print(input_str.translate(translator))

input_with_whitespace = ' \t a string example\t '
input_withoutspace = input_with_whitespace.strip()
print(input_withoutspace)

# remove stop words
input_str = 'NLTK is a leading platform for building Python programs to work with human language data.'
stop_words = set(stopwords.words('english'))
tokens = word_tokenize(input_str)
print(tokens)
result = [i for i in tokens if not i in stop_words]
print (result)

result = [i for i in tokens if not i in ENGLISH_STOP_WORDS]
print(result)

