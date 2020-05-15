import zipfile
import os.path
import os
import shutil
if __name__=="__main__":
    #下面这个可以做全局变量
    srcCatalog='../../Resources/'
    zipName='单词分类_1582023289869.zip'
    arr=[]
    with zipfile.ZipFile(srcCatalog+zipName) as tmp:
        tmp.extractall(srcCatalog+'/TempRes')#这里又解压出来一个zip，助教怎么想的。。。
#记得删掉爸爸压缩包
    pathDir=os.listdir(srcCatalog+'TempRes')

    with zipfile.ZipFile(srcCatalog+'/TempRes/'+pathDir[0]) as z:
        #print(z.namelist())
        z.extract(z.namelist()[3],srcCatalog+'/TempRes')  #   Resources/TempRes/.mooctest/answer.py
        z.extract(z.namelist()[4], srcCatalog+'/TempRes')#   Resources/TempRes/.mooctest/testCases.json
    #   todo: 读取  anwser.py   和   testCases.json
        print(z.filelist)

    shutil.rmtree(srcCatalog+'TempRes')#读完就删







