import pandas as pd
import numpy as np
import csv
from csv import writer
# a1 = pd.read_csv("byte_metadata.csv")
# a2 = pd.read_csv("byte_1_gram.csv")
# a3 = pd.read_csv("byte_img1.csv")
# a4 = pd.read_csv("byte_img2.csv")
# a5 = pd.read_csv("byte_string.csv")
# joined = a1.join(a2).join(a3).join(a4).join(a5)
# print joined
# joined.to_csv("test_byte_code.csv", index=False)

# SORT
# a = []
# x_csv = open('new_sorted_test_id.csv', 'w')
# x_w = writer(x_csv)
# x_w.writerows([['Id']])
# with open('sorted_test_id.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line = 0
#     for row in csv_reader:
#         if line == 0:
#             line += 1
#             continue
#         else:
#             a += row
# a = np.sort(a)
# print a
# for i in a:
#     x_w.writerows([[i]])


# ASM
#a1 = pd.read_csv("asm_metadata.csv")
#a2 = pd.read_csv("asm_symbol.csv")
#a3 = pd.read_csv("asm_opcode.csv")
#a4 = pd.read_csv("asm_registers.csv")
#a5 = pd.read_csv("asm_apis.csv")
#a6 = pd.read_csv("asm_section.csv")
#a7 = pd.read_csv("asm_data_define.csv")
#a8 = pd.read_csv("asm_misc.csv")


a = pd.read_csv("id_test_sorted.csv")
b = pd.read_csv("result_ann.csv")

joined = a.join(b)
print joined.shape

joined.to_csv('my_submission_ann.csv', index=False)
# MERGE RESULT
# a1 = pd.read_csv("new_sorted_test_id.csv")
# a2 = pd.read_csv("test_result.csv")
# joined = a1.join(a2)
# print joined

# joined.to_csv("byte_submission.csv", index=False)
