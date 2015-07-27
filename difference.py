bold = []
f = open("rlvncy.csv","r")
rf = csv.reader(f)
for line in rf :
        bold.append(line[0])
df = open("delet-B.csv","w")
for element in set(b).difference(set(bold)) :
        df.write(element +'\r\n')
        print element
