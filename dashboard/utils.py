import numpy as np
import re
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pickle
from sklearn.feature_extraction.text import CountVectorizer

def total_trained_data():
    corpus = pickle.load(open('corpus.plk','rb'))
    return len(corpus)

def get_clean_text(text):
    review = re.sub('[^a-zA-Z]', ' ', str(text))
    review = review.lower()
    review = review.split()

    # Custom Stopwords
    stopWords = stopwords.words('english')
    stopWords.append('read more')

    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopWords)]

    review = ' '.join(review)

    return review

def train_data(reviews):
    estimator = pickle.load(open('classifier.plk','rb'))
    corpus = pickle.load(open('corpus.plk','rb'))

    start = len(corpus)
    corpus = corpus + reviews

    cv = CountVectorizer(max_features = 12000)
    X = cv.fit_transform(corpus)
    X = X.toarray()

    y_train = X[(start-1):-1, :]


    result = estimator.predict(y_train)

    return result
