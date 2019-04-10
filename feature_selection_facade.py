"""File co chuc nang lua chon feature"""

import sys
import os
from pandas.io.parsers import read_csv
from Measures import multiclass_log_loss
import xgboost as xgb
#from sklearn.cross_validation import KFold
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score, confusion_matrix
import pandas as pd
import numpy as np
from dataSetInfo import dataSetInformaion
from settings import *
from handle_io import io
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
import sys
from csv import writer

# function: tong hop features
# params: no
# returns: void
def feature_fusion():
    # Name of train file
    trainName = '/SortedTrain.csv'
    # Path of a folder contains all single feature categories
    savePath = COMBINED_PATH_CSV
    path = SAVED_PATH_CSV + 'train/'
    os.chdir(path)
    
    # Read the name of each folder
    featureCategoryFolders = io.get_files_in_directory(path ,file_extension='csv')
    # ['/media/huydung/Storage/data-huydung/Microsoft-Malware-Challenge/Dataset/FeatureCategories/train/byte_img1.csv', 
    # '/media/huydung/Storage/data-huydung/Microsoft-Malware-Challenge/Dataset/FeatureCategories/train/byte_img2.csv', 
    # ...
    # '/media/huydung/Storage/data-huydung/Microsoft-Malware-Challenge/Dataset/FeatureCategories/train/byte_meta_data.csv']

    # Load train files
    featureCategoriesLen = len(featureCategoryFolders)

    # read file trainLabels.csv
    class_lable = read_csv(TRAIN_ID_PATH, delimiter=',')
    #                         Id  Class
    #0      01kcPWA9K2BOxQeS5Rju      1

    #print (class_lable.ix[1541:,0]) # lay het hang, cot thi lay cot index 0
    #0      01kcPWA9K2BOxQeS5Rju
    
    new_idx = np.argsort(class_lable.ix[:,0]) # tra ve chi so cua tung hang sau khi sap xep 01>01>0A...
    # >>> x = np.array([3, 1, 2])
    # >>> np.argsort(x)
    # array([1, 2, 0])
    #print new_idx
    
    class_lable = class_lable.ix[new_idx,]    
    #class_lable = class_lable.reset_index(drop=True)
    
    arr = class_lable.values
    print (arr)
    #sys.exit()
    file_dir = '/media/huydung/Storage/data-huydung/Microsoft-Malware-Challenge/my_source/sorted_train_label2.csv'
    # with open(file_dir, 'wb') as f:
    #     writerx = writer(f, delimiter = ',')
    #     for row in arr:
    #         writerx.writerow([row])

    label_csv = open(file_dir, 'w')
    label_csv_w = writer(label_csv, delimiter = ',')
    label_csv_w.writerow(['Labels'])
    for i in arr:    
        label_csv_w.writerow([i])
    sys.exit()

    singleTrains = list()
    # Duyet cac file features rieng le
    for k in range(featureCategoriesLen):
        # Doc file csv features
        dataSet = read_csv(featureCategoryFolders[k], delimiter=',')
        
        data = dataSet#.ix[:, ]

        # print featureCategoryFolders[k][featureCategoryFolders[k].rfind('/')+1:-4] => Lay ra ten file: byte_img1,...
        
        singleTrain = dataSetInformaion(featureCategoryFolders[k][featureCategoryFolders[k].rfind('/')+1:-4],
                                        data, class_lable[0:data.shape[0]])
        # singleTrain[0].data => ra dataset
        # singleTrain[0].dataSetName => ra ten file 
        # singleTrain[0].className => class phan loai tuong ung
        singleTrains.append(singleTrain)
    
    # Save the combined datasets
    os.chdir(savePath)
    for ds in singleTrains:
        jointFile = pd.concat([ds.data, ds.classLabel], axis=1, join='inner')
        if not os.path.exists(savePath + ds.dataSetName):
            os.makedirs(savePath + ds.dataSetName)
        jointFile.to_csv(COMBINED_PATH_CSV + ds.dataSetName + '/NewTrain.csv', sep=',', index=False)
feature_fusion()