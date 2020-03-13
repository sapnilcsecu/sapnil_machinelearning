'''
Created on Aug 7, 2019

@author: Nasir(programmer)
'''
import math
from nltk.tokenize import word_tokenize
import re


def multi_nativebayes_predict(model_data, test_dataset):
    condProbabilityOfTermClass = {}
    final_doc_class_label = {}
    doccount = 0;

    for doc in test_dataset:
        final_doc_class_label['doc' + '-' + str(doccount)] = ''
        words = word_tokenize(doc)
        
        for class_label in model_data.get_class_labels(): 
            condProbabilityOfTermClass[class_label] = 0
            total_class_token = model_data.get_total_class_token()
            for word in words:
                class_eachtoken_count = model_data.get_class_eachtoken_count()
                if(word in class_eachtoken_count):
                    condProbabilityOfTermClass[class_label] = condProbabilityOfTermClass[class_label] + math.log((class_eachtoken_count[class_label][word] + 1) / (total_class_token[class_label] + 1))
                else:
                    condProbabilityOfTermClass[class_label] = condProbabilityOfTermClass[class_label] + math.log(1 / (total_class_token[class_label] + 1))
        
        score_Class = 0
        max_score = 0
        final_class_label = ''
       
        vocabularyCount = model_data.get_vocabularyCount()
        total_class_token = model_data.get_total_class_token()
        for class_label in model_data.get_class_labels():
            # print('total_class_token',total_class_token[class_label])
            score_Class = math.log(total_class_token[class_label] / vocabularyCount) + condProbabilityOfTermClass[class_label]
            # print('the score_Class ',score_Class)
            if(max_score > score_Class):
                max_score = score_Class
                final_class_label = class_label
                # print('the class label '+final_class_label)
        final_doc_class_label['doc' + '-' + str(doccount)] = final_class_label
        # print(final_doc_class_label['doc'+'-'+str(doccount)])
        doccount = doccount + 1            
        
    return final_doc_class_label


def multi_nativebayes_verna_predict(model_data, test_dataset):
    condProbabilityOfTermClass = {}
    final_doc_class_label = {}
    doccount = 0;

    for doc in test_dataset:
        #doc=re.sub("\d+", " ", doc)
        final_doc_class_label['doc' + '-' + str(doccount)] = ''
        words = word_tokenize(doc)
        print('the doc is'+str(doccount)+'',words)
        for class_label in model_data.get_class_labels(): 
            condProbabilityOfTermClass[class_label] = 0
            total_class_token = model_data.get_total_class_token()
            for word in words:
                word=word.lower()
                class_eachtoken_count = model_data.get_class_eachtoken_count()
                vocabulary = model_data.get_vocabulary()
                if(word in vocabulary):
                   # print("word exist in voca")
                    condProbabilityOfTermClass[class_label] = condProbabilityOfTermClass[class_label] + math.log((class_eachtoken_count[class_label][word] + 1) / (total_class_token[class_label] + 1))
                else:
                    print("word not exist in voca"+word)
                    condProbabilityOfTermClass[class_label] = condProbabilityOfTermClass[class_label]+0;
        
        score_Class = 0
        max_score = 0
        final_class_label = ''
        is_norm = 0
        vocabularyCount = model_data.get_vocabularyCount()
        total_class_token = model_data.get_total_class_token()
        for class_label in model_data.get_class_labels():
            if(condProbabilityOfTermClass[class_label] == 0):
                is_norm = 1
                continue
            # print('total_class_token',total_class_token[class_label])
            score_Class = math.log(total_class_token[class_label] / vocabularyCount) + condProbabilityOfTermClass[class_label]
          #  print('the score_Class ',score_Class)
            if(max_score > score_Class):
                max_score = score_Class
                final_class_label = class_label
                # print('the class label '+final_class_label)
        if(is_norm == 1):
            final_doc_class_label['doc' + '-' + str(doccount)] = "norm" 
        else:         
            final_doc_class_label['doc' + '-' + str(doccount)] = final_class_label
        # print(final_doc_class_label['doc'+'-'+str(doccount)])
        doccount = doccount + 1            
    
    return final_doc_class_label


def live_nativebayes_verna_predict(model_data, test_dataset):
    condProbabilityOfTermClass = {}
    final_doc_class_label = {}
    doccount = 0;

   # for doc in test_dataset:
    test_dataset=re.sub("\d+", " ", test_dataset)
    final_doc_class_label['doc' + '-' + str(doccount)] = ''
    words = word_tokenize(test_dataset)
    
    for class_label in model_data.get_class_labels(): 
        condProbabilityOfTermClass[class_label] = 0
        total_class_token = model_data.get_total_class_token()
        for word in words:
            word=word.lower()
            class_eachtoken_count = model_data.get_class_eachtoken_count()
            vocabulary = model_data.get_vocabulary()
            if(word in vocabulary):
                print("word exist in voca")
                condProbabilityOfTermClass[class_label] = condProbabilityOfTermClass[class_label] + math.log((class_eachtoken_count[class_label][word] + 1) / (total_class_token[class_label] + 1))
            else:
                print("word not exist in voca")
                condProbabilityOfTermClass[class_label] = 0;
    
    score_Class = 0
    max_score = 0
    final_class_label = ''
    is_norm = 0
    vocabularyCount = model_data.get_vocabularyCount()
    total_class_token = model_data.get_total_class_token()
    for class_label in model_data.get_class_labels():
        if(condProbabilityOfTermClass[class_label] == 0):
            is_norm = 1
            continue
        # print('total_class_token',total_class_token[class_label])
        score_Class = math.log(total_class_token[class_label] / vocabularyCount) + condProbabilityOfTermClass[class_label]
        # print('the score_Class ',score_Class)
        if(max_score > score_Class):
            max_score = score_Class
            final_class_label = class_label
            # print('the class label '+final_class_label)
    if(is_norm == 1):
        final_class_label = "norm" 
    #else:         
        #final_doc_class_label['doc' + '-' + str(doccount)] = final_class_label
    # print(final_doc_class_label['doc'+'-'+str(doccount)])
    doccount = doccount + 1            
    
    return final_class_label




def live_nativebayes_predict(model_data, input_doc):
    condProbabilityOfTermClass = {}
       
    words = word_tokenize(input_doc)
    
    for class_label in model_data.get_class_labels(): 
        condProbabilityOfTermClass[class_label] = 0
        total_class_token = model_data.get_total_class_token()
        for word in words:
            
            class_eachtoken_count = model_data.get_class_eachtoken_count()
            if(word in class_eachtoken_count):
                condProbabilityOfTermClass[class_label] = condProbabilityOfTermClass[class_label] + math.log((class_eachtoken_count[class_label][word] + 1) / (total_class_token[class_label] + 1))
            else:
                condProbabilityOfTermClass[class_label] = condProbabilityOfTermClass[class_label] + math.log(1 / (total_class_token[class_label] + 1))
    
    score_Class = 0
    max_score = 0
    final_class_label = ''
   
    vocabularyCount = model_data.get_vocabularyCount()
    total_class_token = model_data.get_total_class_token()
    for class_label in model_data.get_class_labels():
        score_Class = math.log(total_class_token[class_label] / vocabularyCount) + condProbabilityOfTermClass[class_label]
        # print('the score_Class ',score_Class)
        if(max_score > score_Class):
            max_score = score_Class
            final_class_label = class_label
            # print('the class label '+final_class_label)
    
    return final_class_label


def accuracy_score(testlabelcopy, final_doc_class_label):
    label_count = 0
    wrong_count = 0
    for label in testlabelcopy:
       # print(final_doc_class_label['doc' + '-' + str(label_count)]+' '+str(label_count))
        if label != final_doc_class_label['doc' + '-' + str(label_count)] :
            wrong_count = wrong_count + 1
        label_count = label_count + 1
    
    accuracy = ((len(testlabelcopy) - wrong_count)*100 )/ len(testlabelcopy)
    
    return accuracy     
        
