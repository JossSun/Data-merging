#coding=utf-8
import csv

# Read in content of a csv file by line
f1 = open("rlvncy.csv","r")
f2 = open("Q1.csv","w")
line = f1.readline()

a =set()

iter = 0
num  = 0
  
while (num<200000000) :
        if line :
                line.split(',')
                query =','.join(line.split(',')[:-2])
                a.add(query)
                print"Updated query list count : %d" %len(a)
                line = f1.readline()
        else :
                break
        num +=1
        print "Read in lines : %d" %num

for val in a :
        f2.write(val+'\r\n')

f1.close()
f2.close()
