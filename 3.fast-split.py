#coding=utf-8
import csv
qlist = {}
num = 0

f1 = open("qincommon.csv", "r")
rf1 = csv.reader(f1)
for line in rf1 :
        qlist[line[0]] = num
        print "Query list is adding... %d" %num
        num +=1
print "$$$$$$$$$$$$$    finished step one !!!    $$$$$$$$$$$$$$$$$$$$$$$"
f2 = open("rlvncy.csv","r")
print "rlvncy.csv is open !!"
line2 = f2.readline()

# open every file for writing
j =0
ff = []
while (j<num) :
        str1 = str(j)
        ff.append(open(str1+".csv","w"))
        j+=1
print "$$$$$$$$$$$$    every file for writing is open!!!    $$$$$$$$$$$$$$$$$$$$$$$"


linelist =[]
linecount =0
while 1 :
        if line2 :
                linelist = line2.split(',')
                #print "linelist is :"
                #print linelist
                query =','.join(line2.split(',')[:-2])
                print "query is : %s" % query
                if query in qlist :
                        print query
                        ff[qlist[query]].write(query+','+linelist[1]+','+linelist[2]+'\r\n')
                        print query+','+linelist[1]+','+linelist[2]+'\r\n'
        else :
                break
        line2 = f2.readline()
        linecount +=1
        print "Dealing with line: %d" %linecount

f1.close()
f2.close()
j =0
while(j<num) :
        ff[j] .close()
        j+=1
