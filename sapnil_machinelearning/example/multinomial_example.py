'''
Created on Aug 21, 2019

@author: Nasir uddin
'''

from dataset_pre.dataset_load import load_cvs_dataset
from dataset_pre.dataset_load import splitDataset
from feature_eng.count_word import count_word_fit
from classifier.multinomial_nativebayes import multi_nativebayes_fit

def main():
    trainDF = load_cvs_dataset("../corpus.csv")
    txt_label = trainDF['label']
    txt_text = trainDF['text']
    trainSet, testcopy, labelset, testlabelcopy=splitDataset(txt_text, txt_label,0.2)
    model_input=count_word_fit(trainSet,labelset)

    multi_nativebayes_fit(model_input[0],model_input[1],model_input[2],model_input[3],model_input[4])
    
if __name__ == '__main__':
    main()