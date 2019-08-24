'''
Created on Aug 7, 2019

@author: Nasir(programmer)
'''
import math
from nltk.tokenize import word_tokenize



def multi_nativebayes_predict(self,model_data,test_dataset,testlabelcopy):
    condProbabilityOfTermClass={}
    final_doc_class_label={}
    doccount=0;
    for doc in test_dataset:
        final_doc_class_label[doc]=0
        words = word_tokenize(doc)
        for class_label in model_data.get_class_labels(): 
            condProbabilityOfTermClass[class_label]=0
            total_class_token=model_data.get_total_class_token()
            for word in words:
                class_eachtoken_count=model_data.get_class_eachtoken_count()
                if(class_eachtoken_count[class_label][word]):
                    condProbabilityOfTermClass[class_label] =condProbabilityOfTermClass[class_label]+math.log((class_eachtoken_count[class_label][word]+1)/(total_class_token[class_label]+1))
                else:
                    condProbabilityOfTermClass[class_label] =condProbabilityOfTermClass[class_label]+math.log(1/(total_class_token[class_label]+1))
        
        score_Class =0
        max_score=0
        final_class_label=''
       
        vocabularyCount=model_data.get_vocabularyCount()
        for class_label in model_data.get_class_labels:
            total_class_token=model_data.get_total_class_token()
            for word in model_data.get_vocabulary():
                score_Class = math.log(total_class_token/vocabularyCount) + condProbabilityOfTermClass[class_label]
                if(max_score<score_Class):
                    max_score=score_Class
                    final_class_label=class_label
        final_doc_class_label[doc]=final_class_label
        
        ++doccount            
                    
        
    return final_doc_class_label