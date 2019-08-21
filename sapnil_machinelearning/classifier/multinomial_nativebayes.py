'''
Created on Aug 7, 2019

@author: Nasir(programmer)
'''
import math

def multi_nativebayes(vocabularyCount,class_eachtoken_count,total_class_token,class_labels,vocabulary):
    condProbabilityOfTermClass={}
    '''
    for class_label in class_labels:
        for word in vocabulary:
            condProbabilityOfTermClass[class_label] =condProbabilityOfTermClass[class_label]+math.log((class_eachtoken_count[class_label][word]+1)/(total_class_token[class_label]+1))
    
    '''
    scoreClass =0
    label_count=0
    max_score=0
    
    for class_label in class_labels:
        for word in vocabulary:
            scoreClass = math.log(total_class_token[label_count]/vocabularyCount) + math.log((class_eachtoken_count[class_label][word]+1)/(total_class_token[class_label]+1))
            if(max_score<scoreClass):
                max_score=scoreClass
                final_class_label=class_label
        ++label_count
    return final_class_label