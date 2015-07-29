# Data-merging
import csv
output = open("qdis.csv","w")
qlist = []
num = 0
file = open('large_data_A34.csv')
csvfile = csv.reader(file)
for query,id,rank in csvfile :
        i =0
        flag = True
        while(i < num ) :
                if query == qlist[i] :
                        flag = False
                        break
                else :
                        i +=1
        if flag :
                output.write (query+'\r\n')
                print query
                qlist.append(query)
                num +=1
output.close()
