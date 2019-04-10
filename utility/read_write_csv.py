import sys
from csv import writer
import csv
from header_construction import *

# API
# api_csv = open('asm_apis.csv', 'w')
# apis_colnames = header_asm_apis()
# api_csv_w = writer(api_csv)
# api_csv_w.writerows([apis_colnames])

# DP
# data_define_csv = open('asm_data_define.csv', 'w')
# data_define_colnames = header_asm_data_define()
# data_define_w = writer(data_define_csv)
# data_define_w.writerows([data_define_colnames])

# SYM
# symbol_csv = open('asm_symbol.csv', 'w')
# symbol_colnames = header_asm_sym()
# symbol_w = writer(symbol_csv)
# symbol_w.writerows([symbol_colnames])

# OPC
# opcode_csv = open('asm_opcode.csv', 'w')
# opcode_colnames = header_asm_opcodes2()
# opcode_w = writer(opcode_csv)
# opcode_w.writerows([opcode_colnames])


x_csv = open('test_asm.csv', 'w')
x_colnames = header_asm_meta_data() + header_asm_sym() + header_asm_opcodes2() + header_asm_registers() + header_asm_apis() + header_asm_sections() + header_asm_data_define() + header_asm_misc()

x_w = writer(x_csv)
x_w.writerows([x_colnames])

with open('../../Dataset/test/LargeTest.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count = 0
    api_arr = []
    for row in csv_reader:
        if line_count == 0:
        #     register_arr = row[1373:1399] #26
        #     api_arr = row[323:1117] #794
        #     data_define_arr = row[1494:1518] #24
        #     opcode_arr = row[1399:1465] #66
        #     symbol_arr = row[1688:1696] #8
        #     metadata_arr = row[1686:1688] #2
        #     misc_arr = row[0:95] #95
        #     section_arr = row[304:305] + row[299:300] + row[298:299] + row[302:303] + row[300:302] + row[303:304] + row[305:306] + row[310:311] + row[307:310] + row[314:323] + row[311:314]

        #     print register_arr, len(register_arr)
        #     print api_arr, len(api_arr)
        #     print data_define_arr, len(data_define_arr)
        #     print opcode_arr, len(opcode_arr)
        #     print symbol_arr, len(symbol_arr)
        #     print metadata_arr, len(metadata_arr)
        #     print misc_arr, len(misc_arr)
        #     print section_arr, len(section_arr)
        #     sys.exit()
            # for i in range (len(row)):
            #     if (row[i] == 'regs_esp'):
            #         print (row[1373:1399], i)
                    
            #         sys.exit()
            line_count += 1
        else:
            register_arr = row[1373:1399] #26
            api_arr = row[323:1117] #794
            data_define_arr = row[1494:1518] #24
            opcode_arr = row[1399:1465] #66
            symbol_arr = row[1688:1696] #8
            metadata_arr = row[1686:1688] #2
            misc_arr = row[0:95] #95
            section_arr = row[304:305] + row[299:300] + row[298:299] + row[302:303] + row[300:302] + row[303:304] + row[305:306] + row[310:311] + row[307:310] + row[314:323] + row[311:314]
            
            all_arr = metadata_arr + symbol_arr + opcode_arr + register_arr + api_arr + section_arr + data_define_arr + misc_arr

            #print all_arr
            #sys.exit()
            x_w.writerows([all_arr])
            
            
#apis
#wcslen 323
#CreateDCA 1116

# datadefine
# db_por 1494
# db3_all_zero 1518

# symbol
# 1688:1696 Star:ExtendedAscii

# opcode
# asm_commands_xor:asm_commands_xor

# meta data
# line_count_asm : asm_size









# ------------------TEST FILE-----------------------------------
# .bytes:
# metadata: FileSize
# 1 gram: TB_00 TB_ff
# image1: Img0 Img51 
# image2: Img0.1 Img107
# string: string_len_counts_1 string_ratio

# x_csv = open('byte_img2.csv', 'w')
# x_colnames = header_byte_img2()
# x_w = writer(x_csv)
# x_w.writerows([x_colnames])
# with open('../../Dataset/test/LargeTest.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')

#     line_count = 0
#     api_arr = []
#     for row in csv_reader:
#         if line_count == 0:
#             # for i in range (len(row)):
#             #     if (row[i] == 'string_ratio'):
#             #         print (row[1518:1634], i)
#             #         sys.exit()
#             line_count += 1
#         else:
#             # x_arr = row[1492:1494]
#             # x_arr = row[1117:1373]
#             #x_arr = row[1634:1686]
#             x_arr = row[1696:1804]
#             #x_arr = row[1518:1634]
#             x_w.writerows([x_arr])

#             # data_define_arr = row[1494:1518]
#             # data_define_w.writerows([data_define_arr])

#             # symbol_arr = row[1688:1696]
#             # symbol_w.writerows([symbol_arr])

#             # opcode_arr = row[1399:1465]
#             # opcode_w.writerows([opcode_arr])
            
#             line_count += 1
