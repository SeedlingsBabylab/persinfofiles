import csv
import sys
import os

from Tkinter import Tk
import tkFileDialog


persinfo = ['02_14', '02_16', '14_15', '14_13', '14_12', '01_17', '01_15', '30_12', '30_10', '30_08', '30_13', '39_11', '39_09', '39_08', '39_10', '09_15', '09_13', '09_12', '17_14', '17_11', '17_10', '28_09', '28_08', '11_12', '27_11', '27_10', '27_08', '27_12', '27_13', '27_09', '03_14', '03_13', '45_06', '45_07', '34_11', '34_10', '21_12', '21_11', '13_14', '13_15', '13_13', '38_11', '38_09', '35_08', '32_11', '32_10', '04_17', '04_13', '04_14', '40_11', '40_08', '40_10', '40_09', '26_12', '26_08', '26_10', '12_15', '25_11', '25_13', '29_08', '29_11', '29_09', '29_10', '29_12', '42_11', '42_09', '37_10', '06_17', '33_09', '18_13', '18_15', '18_10', '18_12', '36_09', '36_08', '43_11', '43_06', '43_07', '08_12', '20_13', '20_11', '15_15', '15_14', '41_06', '41_11', '41_09', '41_10', '07_14', '07_17', '07_12', '10_16', '10_14', '10_12', '10_17', '10_15']

root_dir = ""

found_persinfo = []
nopersinfo = ['25_10', '25_11', '25_12', '13_12', '26_09', '42_10', '36_10', '36_11', '38_08', '31_08', '31_09', '01_16', '01_14', '01_15', '42_08', '06_16', '06_15', '06_14', '06_13', '06_12', '21_10', '21_13', '42_06', '42_07', '45_06', '45_09', '45_08', '16_15', '16_13', '11_12', '04_15', '04_16', '45_11', '08_13', '08_15', '08_14', '08_17', '08_16', '19_13', '19_11', '19_10', '19_15', '19_14', '20_15', '35_11', '20_12', '20_10', '39_08', '39_09', '28_09', '08_09', '35_10', '22_11', '22_10', '22_13', '16_14', '15_14', '16_12', '15_12', '35_09', '11_13', '02_17', '02_15', '33_12', '33_11', '33_10', '46_08', '46_09', '17_15', '17_11', '17_10', '17_13', '17_12', '41_09', '41_08', '41_06', '37_11', '37_10', '29_10', '29_11', '33_08', '03_14', '03_15', '03_16', '37_08', '37_09', '14_14', '28_12', '28_11', '28_10', '43_07', '09_13', '09_16', '09_17', '09_14', '30_09', '28_13', '43_09', '43_08', '41_11', '32_09', '32_08', '25_09', '26_11', '31_11', '26_13', '23_13', '23_10', '12_13', '11_15', '10_13', '07_15', '40_08', '43_10', '30_10', '30_11', '11_16', '18_14', '44_08', '18_11', '12_12', '31_10', '31_12', '44_06', '44_07', '12_14', '11_14']

def walk_tree():
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if "personal_info.csv" in file:
                prefix = file[0:5]
                found_persinfo.append(prefix)

def read_nopersinfo():
    path = tkFileDialog.askopenfilename()
    with open(path, "rU") as file:
        for line in file:

            nopersinfo.append(line[0:5])
            

if __name__ == "__main__":

    Tk().withdraw()

    #root_dir = tkFileDialog.askdirectory()

    #walk_tree()
    #read_nopersinfo()
    unique_nopersinfo = set(nopersinfo)

    unique_persinfo = set(persinfo)

    
    print "No Personal Info (from nopersonalinfo.txt)"
    print unique_nopersinfo
    print
    print
    print "Files with personal_info.csv's associated"
    print unique_persinfo
    print
    print
    
    print "Intersection between persinfo and nopersinfo:\n"
    intersection = unique_nopersinfo.intersection(unique_persinfo)
    print intersection
    print 
    
    print "Difference between persinfo and nopersinfo: \n"
    difference_pers_no = unique_persinfo.difference(unique_nopersinfo)
    print
    
    print 
    print "length of nopersinfo:   {}".format(len(unique_nopersinfo))
    print "length of persinfo:     {}".format(len(unique_persinfo))
    print "length of intersection: {}".format(len(intersection))
    print "length of difference:   {}".format(len(difference_pers_no))
    
