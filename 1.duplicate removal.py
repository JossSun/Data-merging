#coding=utf-8
import csv

# Read in content of a csv file by line
f1 = open("rlvncy.csv","r")
f2 = open("Q1.csv","w")
line = f1.readline()

a = []

iter = 0
num  = 0
  
while (num<24) :
                if iter == 6 :
                        a = list(set(a))
                        print "The Length of query list is : %d" %len(a)
                        iter = 0
                if line :

                        line.split(',')
                        query =','.join(line.split(',')[:-2])
                        a.append(query)
                        print query
                        line = f1.readline()
                else :
                        break
                num +=1
                iter +=1
for val in a :
        f2.write(val+'\r\n')

f1.close()
f2.close()
