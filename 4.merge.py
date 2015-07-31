#coding=utf-8
import os
import os.path
import csv
import sys


# Get all file-paths in a folder

def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir.decode('gbk'))
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            if s == ".DS_Store":
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

out1 = open("fast-data-with-info.csv","w")
out2 = open("fast-data-only.txt","w")
out3 = open("fast-dealed-file","w")

# Deal with files that have same name
filecount =0
for e in file1 :
        if e in file2 :
                filecount +=1
                dic1 = {}
                dic2 = {}
                #print "same files : %s" % e
                fp1 = '/Users/JamesLee/Documents/logisticR/data-merge/'+e
                fp2 = '/Users/JamesLee/Documents/logisticR/2data-merge/'+e
                out3.write(fp1+'\r\n')
                f1 = open(fp1,"r")
                rf1 = csv.reader(f1)
                lines1 =f1.readlines()
                f2 = open(fp2,"r")
                rf2 = csv.reader(f2)
                lines2 = f2.readlines()
                num1 =0
                for line1 in lines1 :
                        if line1 == '\r\n' :
                                num1+= 1
                                continue
                        if line1 :
                                #line1 = line1.strip('\r\n')
                                query,id,score,srank =line1.split(',')
                                #print 'id: ', id
                                dic1[id]=num1
                                num1 +=1
                        else :
                                break
                num2 =0
                for line2 in lines2 :
                        if line2 == '\r\n' :
                                num2+=1
                                continue
                        if line2 :
                                #line2 = line2.strip('\r\n')
                                query, id, rank = line2.split(',')
                                #print 'id: ', id
                                dic2[id] =num2
                                num2 +=1
                        else :
                                break

                for key in dic1 :
                        if dic2.has_key(key) :
                                LL1 = lines1[dic1[key]:dic1[key]+1]
                                #print 'LL1[0] : ', LL1[0]
                                query1,id1,score1,srank1 = LL1[0].split(',')

                                LL2 = lines2[dic2[key]:dic2[key]+1]
                                #print 'LL2[0]: ', LL2[0]
                                query2,id2,rank2 = LL2[0].split(',')

                                srank1 = srank1.strip()
                                rank2 = rank2.strip()
                                out1.write(query1+','+id1+','+score1+','+srank1+','+rank2+'\r\n')
                                out2.write(rank2+' '+score1+' '+srank1+'\r\n')
                                print "Dealed file number: %d" %filecount
                                print "Dealing with file : %s" %fp1
                                print query1+','+id1+','+score1+','+srank1+','+rank2


                        else :
                                continue

                f1.close()
                f2.close()

out1.close()
out2.close()
out3.close()

