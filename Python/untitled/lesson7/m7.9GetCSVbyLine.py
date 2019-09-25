fo = open(r'G:\Python\untitled\lesson7\price2016.csv','r')
ls = []  #创建一个ls列表
for line in fo:
    line = line.replace("\n","")
    ls = line.split(",")
    lns = ""
    for s in ls:
        lns += "{}\t".format(s)
    print(lns)
fo.close()