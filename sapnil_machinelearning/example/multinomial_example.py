'''
Created on Aug 21, 2019

@author: Nasir uddin
'''

from dataset_pre.dataset_load import load_cvs_dataset
from dataset_pre.dataset_load import splitDataset
from feature_eng.count_word import count_ver_word_fit
from classifier.multinomial_nativebayes import multi_nativebayes_verna_predict
from classifier.multinomial_nativebayes import accuracy_score

def main():
    trainDF = load_cvs_dataset("../xss.csv")
    txt_label = trainDF['label']
    txt_text = trainDF['payload']
    #trainSet, testcopy, labelset, testlabelcopy=splitDataset(txt_text, txt_label,0.2)
    model_input=count_ver_word_fit(txt_text,txt_label)
    trainDF_test = load_cvs_dataset("../xss_test.csv")
    txt_label1 = trainDF_test['label']
    txt_text1 = trainDF_test['payload']
    final_doc_class_label=multi_nativebayes_verna_predict(model_input,txt_text1)
    print(final_doc_class_label)
    print("the accuracy_score ",accuracy_score(txt_label1,final_doc_class_label))
if __name__ == '__main__':
    main()