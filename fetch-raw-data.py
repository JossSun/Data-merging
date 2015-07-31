import csv
# find chaji of A1 and QC1
a = []
b = []
f1 = open("A1.csv","r")
rf1 = csv.reader(f1)
for line in rf1 :
        a.append(line[0])
        print line[0]
        print "AAAAAAAAAA"

f2 = open("QC1.csv","r")
rf2 = csv.reader(f2)
for line2 in rf2 :
        b.append(line2[0])
        print line2[0]
        print "BBBBBBBBBB"
print "This is list a"
print a

print "This is list b"
print b
df = open("delet-A1.csv","w")
for i in a:
        if i not in b :
                df.write(i+'\r\n')
                print i
                print "FFFFFFFFFFFFFFF"
f1.close()
f2.close()
df.close()
