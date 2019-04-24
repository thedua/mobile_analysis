from django.shortcuts import render
import pickle
import numpy as np
import pandas as pd
from rest_framework import views
from rest_framework.response import Response
from .serializers import PredictionSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from analysis.settings import BASE_DIR
import os
import re
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

class Prediction(views.APIView):
    data_param = openapi.Parameter('data', in_=openapi.IN_QUERY, description='data', type=openapi.TYPE_STRING)

    @staticmethod
    def read_dataset(file_url):
        df = pd.read_csv(file_url)
        categorical_columns = ['Age', 'EstimatedSalary']
        df_new  = pd.get_dummies(df,columns=categorical_columns)
        return df_new

    @swagger_auto_schema(manual_parameters=[data_param])
    def get(self, request):

        data = request.query_params.get('data',None)
        estimator = pickle.load(open('classifier.plk','rb'))
        features = [x.strip() for x in data.split(',')]

        X = [features[0]]

        review = re.sub('[^a-zA-Z]', ' ', str(X[0]))
        review = review.lower()
        review = review.split()

        # Custom Stopwords
        stopWords = stopwords.words('english')
        stopWords.append('read more')

        ps = PorterStemmer()
        review = [ps.stem(word) for word in review if not word in set(stopWords)]

        review = ' '.join(review)

        corpus = pickle.load(open('corpus.plk','rb'))
        corpus.append(review)

        print(corpus[-1])
        from sklearn.feature_extraction.text import CountVectorizer
        cv = CountVectorizer(max_features = 12000)
        X = cv.fit_transform(corpus).toarray()
        X_test = [X[-1]]

        if hasattr(estimator,'predict'):
            result = estimator.predict(X_test)
        else:
            result = [[0.0,0.0]]
            result[0][int(estimator.predict(df))] = 1.0

        return Response(result)
