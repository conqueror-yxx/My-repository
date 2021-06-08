print("实现输入10个数字，并打印10个数的求和结果")
i=0
t=[]
while i<10:
    num = input("请输入数字：")
    t.append(int(num))
    i=i+1
print("和：",sum(t))