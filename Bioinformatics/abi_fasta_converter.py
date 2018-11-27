#!/usr/bin/env python3

###This script is for converting many ab1 files to fasta files
###Need full path to directory that contain all ab1 files
###Copy this script to that directory and run it in the directory
###Updated by Nat Pombubpa on November 27, 2018


###Import os for getting list of files in data directory
import os

###Full path of data directory is necessary for this script
DATA = '/rhome/npomb001/bigdata/ab1_to_fasta'

###Use Bio.SeqIO for converting abi to fasta
from Bio import SeqIO

for filename in os.listdir(DATA):
    ###Checking for ".ab1" file and convert these files
    if filename.endswith(".ab1"):
        outputfile = filename.split(".")[0] + ".fasta"
        count = SeqIO.convert(filename, "abi", outputfile, "fasta")
        print("conerted %i records" % count)
    else:
    ###if the file is not ".ab1", there will be no conversion
        print("Not ab1 file: no conversion")

