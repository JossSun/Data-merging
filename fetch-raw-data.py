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

f2 = open("a.csv","r")
rf2 = csv.reader(f2)

f3 = open("data-B-1.csv","w")
for line2 in rf2 :
        i = 0
        while (i < 2) :
                print qlist[i]
                print line2[0]
                if line2[0] == qlist[i] :
                        f3.write(line2[0]+','+line2[1]+','+line2[2]+'\r\n')
                        print line2[0]
                i +=1
