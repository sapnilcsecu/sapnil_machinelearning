'''
Created on Aug 19, 2019

@author: Nasir uddin
'''
from stop_words import get_stop_words


def count_word_fit(doc_list,class_labels):
    vocabularyCount = 0
    vocabulary = []
    vocabularySet = set()
    
    
    
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
    
    #class_eachtoken_count = [[0 for x in range(vocabularyCount)] for y in range(len(class_labels))]    
    #class_eachtoken_count=nd.nested_dict()
    '''
    class_labels = list(dict.fromkeys(class_labels))
    class_eachtoken_count = {'__label__1  ': {'name': 'John', 'age': '27', 'sex': 'Male'},
          '2': {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
    print(class_eachtoken_count['__label__1  ']['name'])
    '''
    
    total_class_token={}
    
    #print(vocabulary)
    class_eachtoken_count={} 
    
    for class_label in class_labels: 
        class_eachtoken_count[class_label]={}
        for voc in vocabulary:
            class_eachtoken_count[class_label] [voc] = 0
            print(class_eachtoken_count[str(class_label)] [voc])
            
    
    #test purpose
    '''     
    doc_count=0;        
    stop_words = get_stop_words('english')
    for doc in doc_list:
        words = doc.split(" ")
        for word in words:                        
            if word not in vocabularySet and word not in stop_words:
                vocabularySet.add(word)
                vocabulary.append(word)
                label=class_labels[doc_count].strip()
                ++class_eachtoken_count['label'][word] 
                ++total_class_token[doc_count] 
                vocabularyCount = vocabularyCount + 1   
        ++doc_count 
    
        #test purpose
    '''
            
    doc_count=0
    for doc in doc_list:
        words = doc.split(" ");
        for word in words:
            if word in vocabularySet:
                label=class_labels[doc_count]
                ++class_eachtoken_count[label][word] 
               # ++total_class_token[doc_count] 
               
        ++doc_count 
    print(class_eachtoken_count)         
            
    return vocabularyCount,class_eachtoken_count,total_class_token,class_labels,vocabulary