#coding=utf-8
import os
#将CSL修改为自己的用户名即可
file='C:\\Users\\CSL\\Desktop\\datasample\\png'
def rename(path):
	files=os.listdir(path)
	for file in files:
		dir=os.path.join(path,file)
		# 检查是否为文件夹，如果是，则递归
		if os.path.isdir(dir):
			rename(dir)
			continue
		file_split=file.split('.')
		if file_split[-1] == "jpg":
			file_split[-1]='png'
			str="\\"+".".join(file_split)
			os.rename(dir,path+str)
rename(file)
print("All  Done")