def text_lowercase(text):
    return text.lower()
input_str = "Hey, did you know that the summer break is coming? Amazing right !!"
print(text_lowercase(input_str))

import re
def remove_numbers(text):
    result = re.sub(r'\d+', '', text)
    return result
input_str = "There are 3 balls in this bag, and 12 in the other one."
print(remove_numbers(input_str))

import string
def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)
input_str = "Hey, did you know that the summer break is coming? Amazing right"
print(remove_punctuation(input_str))


def remove_whitespace(text):
    return ' '.join(text.split())
input_str = " we don't need the given questions"
print(remove_whitespace(input_str))

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
def remove_stopwords(text):
    stop_words = set(stopwords.words("english"))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    return filtered_text
example_text = "This is a sample sentence and we are going to remove the stopword"
print(remove_stopwords(example_text))

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
lemmatizer = WordNetLemmatizer()
def lemmatize_word(text):
    word_tokens = word_tokenize(text)
    lemmas = [lemmatizer.lemmatize(word, pos='v') for word in word_tokens]
    return lemmas
text = "data science uses scientific methods algorithms and many types of processing"
print(lemmatize_word(text))


import inflect
p = inflect.engine()
def convert_number(text):
    temp_str = text.split()
    new_string = []
    for word in temp_str:
        if word.isdigit():
            temp = p.number_to_words(word)
            temp = temp.replace(" ", "")   # 🔹 remove spaces in number words
            new_string.append(temp)
        else:
            new_string.append(word)

    return ' '.join(new_string)
input_str = "There are 3 balls in this bag, and 12 in the other one."
print(convert_number(input_str))

from nltk.tokenize import word_tokenize
from nltk import pos_tag
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
def pos_tagging(text):
    word_tokens = word_tokenize(text)
    return pos_tag(word_tokens)
print(pos_tagging("You just gave me a scare"))
