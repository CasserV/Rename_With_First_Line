#-*- coding:utf-8-*-

import os


os.chdir(os.getcwd())
dir=os.listdir()
dirlist=[]
for file in dir:
    dirlist.append(os.path.abspath(os.getcwd())+"\\"+file)
print(dirlist)

for p in dirlist:
    with open(p,'r',errors="ignore") as f:
        new_name=os.path.split(p)[1].split('.')[0]+f.readline().strip()
    try:
        os.rename(p,os.path.abspath(os.getcwd())+"\\"+new_name+os.path.splitext(p)[1])
        print(os.path.abspath(os.getcwd())+"\\"+new_name+os.path.splitext(p)[1]+' 重命名已完成')
    except:
        print('重命名 失败')
