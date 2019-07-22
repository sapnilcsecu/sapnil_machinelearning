'''
Created on Apr 19, 2019

@author: Nasir uddin
'''
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection


# NB, ngram_tf_idf is:  76.08%


def ngram_tf_idf(txt_text, txt_label):
    Train_X, Test_X, Train_Y, Test_Y = model_selection.train_test_split(txt_text, txt_label)
    
    # tfidf_vect_ngram = TfidfVectorizer(analyzer='word', token_pattern=r'\w{1,}', ngram_range=(2,3), max_features=5000)
    
    tfidf_vect_ngram = TfidfVectorizer(analyzer='word', ngram_range=(2, 3), max_features=5000)
    tfidf_vect_ngram.fit(txt_text)
    Train_X_ngram = tfidf_vect_ngram.transform(Train_X)
    Test_X_ngram = tfidf_vect_ngram.transform(Test_X)
    
    return Train_X_ngram , Test_X_ngram, Train_Y, Test_Y, tfidf_vect_ngram
    
