import csv
qlist = []
num = 0

f1 = open("QC1.csv", "r")
rf1 = csv.reader(f1)
for line in rf1 :
        qlist.append(line[0])
        print "QQQQQQQQQQ"
        print line[0]
        num +=1
print "$$$$$$$$$$$$$$$$$$$     finished step one       $$$$$$$$$$$$$$$$$$$$$$$$$$"
f2 = open("rlvncy.csv","r")
rf2 = csv.reader(f2)
j =0
while (j<num) :
        str1 = str(j)
        ff = open(str1+".csv","w")
        j+=1
print "$$$$$$$$$$$$$$$$$$$$    finished step two       $$$$$$$$$$$$$$$$$$$$$$$$$$$ "
count = 0
for line2 in rf2 :
        count +=1
        print "Line count is : %d" %count
        i = 0
        while (i < num) :
                strtmp = str(i)
                if line2[0] == qlist[i] :

                        w = open(strtmp+".csv","a")
                        w.write(line2[0]+','+line2[1]+','+line2[2]+'\r\n')
                        print line2[0]
                        w.close()  
                i +=1

f1.close()
f2.close()
