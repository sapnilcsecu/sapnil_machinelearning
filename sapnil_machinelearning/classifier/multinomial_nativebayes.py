'''
Created on Aug 7, 2019

@author: Nasir(programmer)
'''
import math
from nltk.tokenize import word_tokenize



def multi_nativebayes_predict(model_data,test_dataset):
    condProbabilityOfTermClass={}
    final_doc_class_label={}
    doccount=0;

    for doc in test_dataset:
        final_doc_class_label['doc'+'-'+str(doccount)]=''
        words = word_tokenize(doc)
        
        for class_label in model_data.get_class_labels(): 
            condProbabilityOfTermClass[class_label]=0
            total_class_token=model_data.get_total_class_token()
            for word in words:
                class_eachtoken_count=model_data.get_class_eachtoken_count()
                if(word in class_eachtoken_count):
                    condProbabilityOfTermClass[class_label] =condProbabilityOfTermClass[class_label]+math.log((class_eachtoken_count[class_label][word]+1)/(total_class_token[class_label]+1))
                else:
                    condProbabilityOfTermClass[class_label] =condProbabilityOfTermClass[class_label]+math.log(1/(total_class_token[class_label]+1))
        
        score_Class =0
        max_score=0
        final_class_label=''
       
        vocabularyCount=model_data.get_vocabularyCount()
        total_class_token=model_data.get_total_class_token()
        for class_label in model_data.get_class_labels():
            score_Class = math.log(total_class_token[class_label]/vocabularyCount) + condProbabilityOfTermClass[class_label]
            # print('the score_Class ',score_Class)
            if(max_score>score_Class):
                max_score=score_Class
                final_class_label=class_label
                #print('the class label '+final_class_label)
        final_doc_class_label['doc'+'-'+str(doccount)]=final_class_label
        #print(final_doc_class_label['doc'+'-'+str(doccount)])
        doccount=doccount+1            
                    
        
    return final_doc_class_label



def accuracy_score(testlabelcopy,final_doc_class_label):
    label_count=0
    wrong_count=0
    for label in testlabelcopy:
        if label !=final_doc_class_label['doc'+'-'+str(label_count)] :
            wrong_count=wrong_count+1
    label_count=label_count+1
    
    accuracy = ((len(testlabelcopy)-wrong_count)/len(testlabelcopy))*100
    
    return accuracy     
        
        