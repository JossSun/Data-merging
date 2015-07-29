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
            if s == ".DS_Store":
                continue
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)
    return fileList

# Get all file-name in file-paths list

list1 = GetFileList('/Users/JamesLee/Documents/logisticR/log/folder1', [])
list2 = GetFileList('/Users/JamesLee/Documents/logisticR/log/folder2', [])
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


# Deal with files that have same name
for e in file1 :
        #print e
        if e in file2 :
                #print "same files : %s" % e
                fp1 = '/Users/JamesLee/Documents/logisticR/log/folder1/'+e
                fp2 = '/Users/JamesLee/Documents/logisticR/log/folder2/'+e
                f1 = open(fp1,"r")
                rf1 = csv.reader(f1)
                f2 = open(fp2,"r")
                rf2 = csv.reader(f2)
                for line1 in  rf1 :
                        print "content in file1 :%s" % line1[0]
                        for line2 in rf2 :
                                print "content in file2 : %s" %line2[0]
                                #if line1[0] == line2[0] :
                                        #print line1[0]
