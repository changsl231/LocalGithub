weekstr = "星期一星期二星期三星期四星期五星期六星期日"
weekid = eval(input("请输入数字1-7：\n"))
pos = (weekid - 1)*3
print(weekstr[pos:pos+3])