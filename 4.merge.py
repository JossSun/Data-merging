#coding=utf-8
import os
import os.path
import csv

# Get all file-paths in a folder

def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir.decode('gbk'))
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            if s == ".DS_Store" or s == "qincommon.csv" or s == "split.py":
                continue
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)
    return fileList
    
# Get all file-name in file-paths list

list1 = GetFileList('/Users/JamesLee/Documents/logisticR/data-merge', [])
list2 = GetFileList('/Users/JamesLee/Documents/logisticR/2data-merge', [])
file1 = []
file2 = []
for e in list1:
        fp = e
        filename = os.path.basename(fp)
        file1.append(filename)
for e in list2 :
        fp = e
        filename = os.path.basename(fp)
        file2.append(filename)


out1 = open("data-with-info.csv","w")
out2 = open("data-only.txt","w")
out3 = open("dealed-files.csv","w")

# Deal with files that have same name
filecount =0
for e in file1 :
        #print e
        if e in file2 :
                filecount +=1
                print "same files : %s" % e
                fp1 = '/Users/JamesLee/Documents/logisticR/data-merge/'+e
                fp2 = '/Users/JamesLee/Documents/logisticR/2data-merge/'+e
                out3.write(fp1+'\r\n')
                f1 = open(fp1,"r")
                rf1 = csv.reader(f1)
                f2 = open(fp2,"r")
                rf2 = csv.reader(f2)
                for line1 in  rf1 :
                        if line1:
                                #print "id number in file1 is : %s" % line1[1]
                                #print "content in file1 :%s" % line1[0]
                                for line2 in rf2 :
                                        if line2:
                                                #print "id number in file2 is : %s" % line2[1]
                                                #print "content in file2 : %s" %line2[0]
                                                if line1[1] == line2[1] :
                                                        out1.write( line1[0]+','+line1[1]+','+line1[2]+','+line1[3]+','+line2[2]+'\r\n')
                                                        out2.write(line2[2]+','+line1[2]+','+line1[3]+'\r\n')
                                                        print "Dealed file numbers: %d" %filecount
                                                        print "Dealing with file: %s" %fp1
                                                        print line1[0]+','+line1[1]+','+line1[2]+','+line1[3]+','+line2[2]

                                f2.seek(0)
                f1.close()
                f2.close()

out1.close()
out2.close()
out3.close()
