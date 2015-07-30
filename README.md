# Data-merging
duplication removal :
a much faster version of finding distinguished queries using set

distinguish-queries.py:
find distinguished queries in files 

common.py:
find common parts in two sets

difference.py:
find the different part in two sets

fetch-raw-data.py:
if the query is in common part, record this piece of data

split-file.py:
if the query in file "large-data.csv" is the same as the query in "QC1.csv", record the piece of data in a file. create a file named after the order of the query in list of "QC1.csv"
