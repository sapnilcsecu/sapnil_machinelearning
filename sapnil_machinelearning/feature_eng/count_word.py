'''
Created on Aug 19, 2019

@author: Nasir uddin
'''
from stop_words import get_stop_words

def count_word_fit(doc_list,class_labels):
    vocabularyCount = 0
    vocabulary = []
    vocabularySet = set()
    
    word_dict = {}
    
     #Using Python's stop-words package to get the stop words in English
    stop_words = get_stop_words('english')
    for doc in doc_list:
       words = doc.split(" ")
       for word in words:                        
        if word not in vocabularySet and word not in stop_words:
            vocabularySet.add(word)
            vocabulary.append(word)
            vocabularyCount = vocabularyCount + 1
            
    
    class_labels = list(dict.fromkeys(class_labels))    
    
    class_eachtoken_count = [[0 for x in range(vocabularyCount)] for y in range(len(class_labels))]    
        
            
    return vocabularyCount