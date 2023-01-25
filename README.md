## DNA Identification Program

This program is a command line application that can be used to identify a person based on their DNA. It is designed for Harvard's CS50x course and is implemented in Python. The program takes in two command line arguments: a CSV file containing a DNA database and a text file containing a DNA sequence. It compares the DNA sequence in the text file to the DNA database and returns the name of the person whose DNA in the database most closely matches the DNA sequence in the text file.

### Getting Started

To get started, first log into the CS50 IDE and open a terminal window. Then, execute the following commands to download the problem and set up the necessary files:

```
cd ~
mkdir pset6
cd pset6
wget https://cdn.cs50.net/2019/fall/psets/6/dna/dna.zip
unzip dna.zip
rm dna.zip
ls
```


You should see a directory called dna, which was inside of the downloaded ZIP file. Change into that directory by executing `cd dna` and then execute `ls` to see the sample databases and sequences.

### Background

DNA profiling is a technique used in forensic science to identify a person based on their DNA. DNA is a sequence of nucleotides, the building blocks of genetic information in living things. Each nucleotide contains one of four different bases: adenine (A), cytosine (C), guanine (G), or thymine (T). Some portions of the DNA sequence are similar across almost all humans, but other portions have high genetic diversity and vary more across the population.

Short Tandem Repeats (STRs) are one place where DNA has high genetic diversity. An STR is a short sequence of DNA bases that tends to repeat consecutively numerous times at specific locations inside of a person's DNA. The number of times any particular STR repeats varies a lot among individuals. Using multiple STRs, rather than just one, can improve the accuracy of DNA profiling.

The program uses a CSV file as the DNA database, where each row corresponds to an individual and each column corresponds to a particular STR. The program compares the DNA sequence in the text file to the STRs in the database and returns the name of the person whose DNA in the database most closely matches the DNA sequence in the text file.

### Usage

The program is executed from the command line, with the following syntax:
```
python dna.py databases/large.csv sequences/5.txt
```

This will compare the DNA sequence in the file sequences/5.txt to the DNA database in the file databases/large.csv and return the name of the person whose DNA in the database most closely matches the DNA sequence in the text file.

### Note

The program is only for educational purpose and not for any real world implementation as it's not accurate enough and many other factors are considered while identifying a person based on their DNA.
