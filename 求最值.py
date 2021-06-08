print("从键盘依次输入10个数字，并打印最大的数、10个数的和、和平均数")
i=0
t=[]
while i<10:
    num = input("请输入数字：")
    t.append(int(num))
    i=i+1
print("最大值为：",max(t),sum(t),sum(t)/10)