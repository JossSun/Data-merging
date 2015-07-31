import csv

a =set([])
b = set([])

f1 = open("Q1.csv","r")
r1 = csv.reader(f1)
f2 = open("Q2.csv","r")
r2 = csv.reader(f2)
f3 = open("qincommon.csv","w")

for line1 in r1 :
        a.add(line1[0])
        print "Set A is adding"
for line2 in r2 :
        b.add(line2[0])
        print "Set B is adding"
tmp  = a&b
print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     Finished!!!    $$$$$$$$$$$$$$$$$$$$$$$$"
for ele in tmp :
        f3.write(ele+'\r\n')
        print ele
f1.close()
f2.close()
f3.close()
