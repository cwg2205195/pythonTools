

import os
import sys


def recGetFiles(path,buf):
    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path,file)
        if os.path.isdir(file_path):
            recGetFiles(file_path,buf)
        else:
            buf.append(file_path)

def isXXFileFormat(filepath):
    f=open(filepath,"rb")
    magic=[0x02, 0x23, 0x21, 0x53, 0x49, 0x4C, 0x4B, 0x5F, 0x56, 0x33]
    data = f.read(10)
    if len(data) < 10:
        return False 
    #type(data)
    for i in range(len(magic)):
        if magic[i] != data[i]:
            return False 
    #print(data)
    return True 

def Wrapper(path="I:\\Git\\fileFinder\\"):
    files = []
    recGetFiles(path,files)
    if len(files) > 0 :
        print("[%d] files to check \n" % len(files))
        for file in files:
            #print(file)
            if isXXFileFormat(file) == True :
                print("Found one : ")
                print(file)
    else:
        print("Shit , nothing found !\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Wrapper(sys.argv[1])
    else:
        Wrapper()

        #print()
#if isXXFileFormat("3CA6CE5070DA2E9DBCF72D0C09854FF1.amr") == True :
    #print("Found you mf\n")
'''    
files=[]
recGetFiles("E:\\thunder\\0702\\",files)
print(files)
'''
'''
def getAllFileFromHere(path):
    files=[]
    dirs = []
    files,dirs=getCurDirFilesAndSubDirs(path)
    while len(dirs) > 2 :
        for i in range(len(dirs)-2):
            path1=dirs[i]
            retFiles,redDirs=getCurDirFilesAndSubDirs(path1)
'''            
#getCurDirFiles("E:\\thunder\\0702")