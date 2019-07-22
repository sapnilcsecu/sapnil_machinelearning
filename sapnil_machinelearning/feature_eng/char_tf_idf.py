'''
Created on Apr 19, 2019

@author: Nasir uddin
'''
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn import model_selection

#NB, WordLevel TF-IDF:  81.0


def char_tf_idf(txt_text,txt_label):
    Train_X, Test_X, Train_Y, Test_Y  = model_selection.train_test_split(txt_text, txt_label)
    tfidf_vect_ngram_chars = TfidfVectorizer(analyzer='char', token_pattern=r'\w{1,}', ngram_range=(2,3), max_features=5000)
    tfidf_vect_ngram_chars.fit(txt_text)
    Train_X_ngram_chars =  tfidf_vect_ngram_chars.transform(Train_X) 
    Test_X_ngram_chars =  tfidf_vect_ngram_chars.transform(Test_X)
    
    return Train_X_ngram_chars, Test_X_ngram_chars,Train_Y, Test_Y,tfidf_vect_ngram_chars