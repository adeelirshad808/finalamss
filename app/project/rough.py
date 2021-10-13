# # importing required modules
# from os import error
# import PyPDF2
# import difflib
import difflib

from difflib import SequenceMatcher
with open(r"C:\Users\AdeeL\Desktop\AMS\app\project\file3.txt", errors="ignore") as file1, open(r"C:\Users\AdeeL\Desktop\AMS\app\project\file2.txt", errors="ignore") as file2:
    file1_data = file1.read()
    file2_data = file2.read()
    print(difflib.SequenceMatcher(None, file1_data, file2_data).ratio()*100)

#     file1_data = 'adeel ali ahmed'
#     file2_data = 'adeel ali ahmedd'
#     similarity = SequenceMatcher(None, file1, file2_data)

#     print(similarity.ratio())
# import difflib

# # assign parameters
# par1 = 'aghgh'
# par2 = 'gfg'

# # compare
# print(difflib.SequenceMatcher(None, par1, par2).ratio())
