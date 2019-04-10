"""Ham doc du lieu tu file nen .bytes.gz roi ghi ra file .csv"""

from multiprocessing import Pool
from csv import writer
from feature_extraction import *
from header_construction import *
from settings import *
from handle_io import io
import os, gzip, time, numpy, traceback, sys

# Duong dan den dataset
path = DATASET_PATH
# Lay duong dan tuyet doi
os.chdir(path)

# function: ham giai file ra .bytes sau do ghi ra .csv
# params: dataset_type: 'train' hoac 'test'
# returns: void 
def byte_extraction(dataset_type):
    directory_name = dataset_type + 'gz/test/'  # directory_name = train_gz hoac test_gz
    files = os.listdir(directory_name)  # doc ra het ten file .gz
    files = numpy.sort(files)   # sap xep theo ten file
    # print files[0:100]
    # sys.exit()
    # chi lay ra file .bytes
    byte_files = [i for i in files if i.endswith('.bytes.gz')]

    # tao ra cac file .csv de ghi du lieu
    all_csv = open(SAVED_PATH_CSV + dataset_type + '/test_all_byte_code.csv', 'w')

    # Dinh nghia header cac cot khi in ra
    meta_data_colnames = header_byte_meta_data()
    onegram_colnames = header_byte_1gram()
    img1_colnames = header_byte_img1()
    img2_colnames = header_byte_img2()
    str_len_colnames = header_byte_str_len()

    # Khai bao cac bien dung de ghi du lieu
    # meta data
    all_csv_w = writer(all_csv)

    all_csv_w.writerows([meta_data_colnames + onegram_colnames + img1_colnames  + img2_colnames + str_len_colnames])

    # sys.exit()
    # Creating row set
    rows = []
    for t, fname in enumerate(byte_files):
        f = gzip.open(directory_name+fname, 'r')
        try:

            # One Gram
            oneg = byte_1gram(f)
            f.seek(0)
            #Meta data
            meta_data = byte_meta_data(directory_name+fname, f)
            f.seek(0)
            # Images 1        
            image1 = byte_image1(f)
            f.seek(0)
            # Images 2
            image2 = byte_image2(f)
            f.seek(0)
            # Strings
            str_lengths = byte_string_lengths(f)

            all_csv_w.writerows([oneg + meta_data + image1 + image2 + str_lengths])

        except Exception, err:
            print err, traceback.print_exc()
            print "Error", fname

        # Writing rows after every 10 files processed
        if (t+1)%10==0:
            print(t+1, 'byte files loaded from ', dataset_type)
            #fw.writerows(rows)
            rows = []
            #break

byte_extraction('train')