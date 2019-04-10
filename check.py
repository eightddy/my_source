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
# Lay doc file apis, luu vao mangr => 1 phan tu
defined_apis = io.read_all_lines(APIS_PATH)
# Lay ra phan tu dau tien va split thanh mang theo ,
defined_apis = defined_apis[0].split(',')

# function: ham giai file ra .asm sau do ghi ra .csv
# params: dataset_type: 'train' hoac 'test'
# returns: void
def asm_extraction(dataset_type):
    directory_name = dataset_type + '_gz/' # directory_name = train_gz hoac test_gz
    files = os.listdir(directory_name)  # doc ra het ten file .gz
    files = numpy.sort(files) # sap xep theo ten file
    # chi lay ra file .asm
    byte_files = [i for i in files if i.endswith('.asm.gz')]
    
    # tao ra cac file .csv de ghi du lieu
    all_csv = open(SAVED_PATH_CSV + dataset_type + '/all_asm.csv', 'w')
    # apis_csv = open(SAVED_PATH_CSV + dataset_type + '/asm_apis.csv', 'w')
    #sys.exit() 
    for t, fname in enumerate(byte_files):
        f = gzip.open(directory_name+fname, 'r')
        try:
            # sections
            sections, names = asm_sections(f)
        except Exception, err:
            print err, traceback.print_exc()
            print "Error", fname

        # Writing rows after every 10 files processed
        if (t+1)%10 == 0:
            print(t+1, 'asm files loaded from ', dataset_type)
            #fw.writerows(rows)
            rows = []
            #break

asm_extraction('train')