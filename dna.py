from cs50 import get_string
from sys import argv
import csv
import re

# dictionary that will be used to store STRs
seq = {}

# the program only accepts 2 command line arguments
if len(argv) != 3:
    print("Incorrect usage")
    exit(1)

# open csv file into memory
with open(argv[1], mode="r") as csv_file:
    csv_reader = csv.reader(csv_file)
    # store the STRs into a variable
    STRS = next(csv_reader)
    # removes the 'name' from the first row, kepping only the STRs as a list
    STRS.pop(0)

# open txt file to get the DNA sequence
with open(argv[2], mode = "r") as dna_sequence:
    # stores the contents of the txt file within the txt_reader variable
    txt_reader = dna_sequence.read()
    for row in txt_reader:
        dnalist = row

DNA = dnalist[0]

# copy STRs names
for s in STRS:
    seq[s] = 1

# check the longest repeated STR
for key in STRS:
    
    # using regular expressions to match the STRs
    match = re.findall(fr"(?:{key})+", txt_reader)
    
    # check the size of the list
    list_size = len(match)
    
    # check if the length of the list is different than zero
    if list_size != 0:
        
        # divides the size of longest run of repeated STRs by the length of the STR
        longest_str = len(max(match,key = len))
        strlen = len(key)
        result = longest_str / strlen
        
        # copy the result of the lengths to the dictionary that will contain the sequences
        seq[key] = int(result)
    
with open(argv[1]) as persons_list:
    
    persons = csv.DictReader(persons_list)
    equal = 0
    
    for person in persons:
        # compares the sequences to every person and prints name
        for DNA in seq:
            
            if seq[DNA] == int(person[DNA]):
                equal += 1
                
            if equal == len(seq):
                print(person['name'])
                quit()
                
    print('No Match')