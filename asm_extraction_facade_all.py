"""Ham doc du lieu tu file nen .asm.gz roi ghi ra file .csv"""

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


    # Dinh nghia header cac cot khi in ra
    misc_colnames = header_asm_misc()
    meta_data_colnames = header_asm_meta_data()
    sym_colnames = header_asm_sym()
    registers_colnames = header_asm_registers()
    opcodes_colnames = header_asm_opcodes()
    sections_colnames = header_asm_sections()
    data_define_colnames = header_asm_data_define()
    # apis_colnames = header_asm_apis()

    # Khai bao cac bien dung de ghi du lieu
    all_csv_w = writer(all_csv)

    all_csv_w.writerows([misc_colnames + sym_colnames + registers_colnames + opcodes_colnames + sections_colnames + data_define_colnames])

    # apis
    # apis_csv_w = writer(apis_csv)
    # apis_csv_w.writerows([apis_colnames])

    # Creating row set
    rows = []
    for t, fname in enumerate(byte_files):
        f = gzip.open(directory_name+fname, 'r')
        try:
            # MISC
            misc = asm_misc(f)
            f.seek(0)

            # symbols
            symbols = asm_symbols(f)
            f.seek(0)

            # register
            registers = asm_registers(f)
            f.seek(0)

            # opcodes
            opcodes = asm_opcodes(f)
            f.seek(0)

            # sections
            sections, names = asm_sections(f)
            f.seek(0)

            # data_defines
            data_defines = asm_data_define(f)

            all_csv_w.writerows([misc + symbols + registers + opcodes + sections + data_defines])

            # # apis
            # apis = asm_APIs(f,defined_apis)
            # apis_csv_w.writerows([apis])

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