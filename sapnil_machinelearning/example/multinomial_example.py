'''
Created on Aug 21, 2019

@author: Nasir uddin
'''

from dataset_pre.dataset_load import load_cvs_dataset
from dataset_pre.dataset_load import splitDataset
from feature_eng.count_word import count_word_fit
from classifier.multinomial_nativebayes import multi_nativebayes_predict

def main():
    trainDF = load_cvs_dataset("../corpus.csv")
    txt_label = trainDF['label']
    txt_text = trainDF['text']
    trainSet, testcopy, labelset, testlabelcopy=splitDataset(txt_text, txt_label,0.2)
    model_input=count_word_fit(trainSet,labelset)

    final_doc_class_label=multi_nativebayes_predict(model_input,testcopy,testlabelcopy)
    print(final_doc_class_label)
if __name__ == '__main__':
    main()