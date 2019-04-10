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
    directory_name = dataset_type + 'gz/'  # directory_name = train_gz hoac test_gz
    files = os.listdir(directory_name)  # doc ra het ten file .gz
    files = numpy.sort(files)   # sap xep theo ten file
    # print files[0:100]
    # sys.exit()
    # chi lay ra file .bytes
    byte_files = [i for i in files if i.endswith('.bytes.gz')]

    # tao ra cac file .csv de ghi du lieu
    oneg_csv = open(SAVED_PATH_CSV + dataset_type + '/byte_oneg.csv', 'w')
    m_data_csv = open(SAVED_PATH_CSV + dataset_type + '/byte_meta_data.csv', 'w')
    img1_csv = open(SAVED_PATH_CSV + dataset_type + '/byte_img1.csv', 'w')
    img2_csv = open(SAVED_PATH_CSV + dataset_type + '/byte_img2.csv', 'w')
    #entropy_csv = open(SAVED_PATH_CSV + dataset_type + '/byte_entropy.csv', 'w')
    str_lengths_csv = open(SAVED_PATH_CSV + dataset_type + '/byte_str_lengths.csv', 'w')

    # Dinh nghia header cac cot khi in ra
    meta_data_colnames = header_byte_meta_data()
    onegram_colnames = header_byte_1gram()
    img1_colnames = header_byte_img1()
    img2_colnames = header_byte_img2()
    #entropy_colnames = header_byte_entropy()
    str_len_colnames = header_byte_str_len()

    # Khai bao cac bien dung de ghi du lieu
    # meta data
    m_data_csv_w = writer(m_data_csv)
    m_data_csv_w.writerows([meta_data_colnames])
    # one byte gram
    oneg_csv_w = writer(oneg_csv)
    oneg_csv_w.writerows([onegram_colnames])
    # img1
    img1_csv_w = writer(img1_csv)
    img1_csv_w.writerows([img1_colnames])
    # img2
    img2_csv_w = writer(img2_csv)
    img2_csv_w.writerows([img2_colnames])
    # entropy
    #entropy_csv_w = writer(entropy_csv)
    #entropy_csv_w.writerows([entropy_colnames])
    # str_lengths
    str_lengths_csv_w = writer(str_lengths_csv)
    str_lengths_csv_w.writerows([str_len_colnames])

    # Creating row set
    rows = []
    for t, fname in enumerate(byte_files):
        f = gzip.open(directory_name+fname, 'r')
        try:

            # One Gram
            oneg = byte_1gram(f)
            oneg_csv_w.writerows([oneg])

            f.seek(0)

            #Meta data
            meta_data = byte_meta_data(directory_name+fname, f)
            m_data_csv_w.writerows([meta_data])

            f.seek(0)

            # Images 1        
            image1 = byte_image1(f)
            img1_csv_w.writerows([image1])

            f.seek(0)

            # Images 2
            image2 = byte_image2(f)
            img2_csv_w.writerows([image2])

            f.seek(0)

            # Entropy
            #entropy = byte_entropy(f)
            #entropy_csv_w.writerows([entropy])

            #f.seek(0)

            # Strings
            str_lengths = byte_string_lengths(f)
            str_lengths_csv_w.writerows([str_lengths])

        except Exception, err:
            print err, traceback.print_exc()
            print "Error", fname

        # Writing rows after every 100 files processed
        if (t+1)%100==0:
            print(t+1, 'byte files loaded from ', dataset_type)
            #fw.writerows(rows)
            rows = []
            #break

byte_extraction('train')