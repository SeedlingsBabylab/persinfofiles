import csv
import sys
import os

from Tkinter import Tk
import tkFileDialog

root_dir = ""

found_persinfo = []
nopersinfo = []

def walk_tree():
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if "personal_info.csv" in file:
                prefix = file[0:5]
                found_persinfo.append(prefix)

    

if __name__ == "__main__":

    Tk().withdraw()

    root_dir = tkFileDialog.askdirectory()

    walk_tree()

    print found_persinfo

    
