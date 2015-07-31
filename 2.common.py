
b = []
f1 = open("qdis.csv","r")
r1 = csv.reader(f1)
f2 = open("qdis2.csv","r")
r2 = csv.reader(f2)
f3 = open("qincommon.csv","w")

for line1 in r1 :
        a.append(line1[0])
for line2 in r2 :
        b.append(line2[0])

tmp  = [val for val in a if val in b]
for ele in tmp :
        f3.write(ele+'\r\n')
        print ele
f1.close()
f2.close()
f3.close()
