#coding=utf-8
import os
#将CSL修改为自己的用户名即可
file_jpg='C:\\Users\\CSL\\Desktop\\datasample\\jpg'
#设置jpg格式图片的存储路径
file_png='C:\\Users\\CSL\\Desktop\\datasample\\png'
#设置png格式图片的存储路径

#名称：rename()函数
#参数：path：文件的存储路径
#作用：将path文件夹下的jpg图片转换为png文件，并存储到file_png的路径下
def rename(path):
	files=os.listdir(path)
	#os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
	for file in files:
		dir=os.path.join(path,file)
		#os.path.join()，将join()里面得参数拼接成一个完整得路径。
		# 检查是否为文件夹，如果是，则递归
		if os.path.isdir(dir):
			rename(dir)
			continue
		file_split=file.split('.')
		#file.split将file列表数据以"."分割，并赋值给file_split
		#print(file_split)
		#可以通过print函数查看file_split的数据
		if file_split[-1] == "jpg":
			file_list = file_split[0]+'_'+file_split[4]+'_'+file_split[-2]
			#file_split[0] = "PA_YT543"
			#file_split[4] = "0001"
			#file_split[-2] = "1399237097"
			#通过"_"连接file_split[0]、file_split[4]、file_split[-2]存储到file_list列表
			str="\\"+"".join(file_list)+".png"
			#"".join(file_list)通过""将file_list列表的各个元素连接成字符串
			print(str)
			#查看连接完成的字符串
			os.rename(dir,file_png+str)
			#os.rename()重名命函数
		    #dir：原先的路径下的文件
		    #file_png+str：新的存储路径和文件名

rename(file_jpg)
#调用rename()函数
print("All  Done")
#执行完成输出