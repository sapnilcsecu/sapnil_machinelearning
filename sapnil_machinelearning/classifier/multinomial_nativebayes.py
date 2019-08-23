'''
Created on Aug 7, 2019

@author: Nasir(programmer)
'''
import math




def multi_nativebayes_predict(self,model_data):
    condProbabilityOfTermClass={}
    for class_label in model_data.get_class_labels(): 
        condProbabilityOfTermClass[class_label]=0
    for class_label in model_data.get_class_labels():
        total_class_token=model_data.get_total_class_token()
        for word in model_data.get_vocabulary():
            class_eachtoken_count=model_data.get_class_eachtoken_count()
            
            condProbabilityOfTermClass[class_label] =condProbabilityOfTermClass[class_label]+math.log((class_eachtoken_count[class_label][word]+1)/(total_class_token[class_label]+1))
    
    
    scoreClass =0
    label_count=0
    max_score=0
    vocabularyCount=model_data.get_vocabularyCount()
    for class_label in model_data.get_class_labels:
        total_class_token=model_data.get_total_class_token()
        for word in model_data.get_vocabulary():
            scoreClass = math.log(total_class_token/vocabularyCount) + condProbabilityOfTermClass[class_label]
            if(max_score<scoreClass):
                max_score=scoreClass
                final_class_label=class_label
        ++label_count
    return final_class_label