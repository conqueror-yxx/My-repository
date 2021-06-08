print("有以下两个数，使用+，-号实现两个数的调换。")
print("请输入两个整数：")
a = int(input("第一个整数："))
b = int(input("第二个整数："))
a = a+b
b = a-b
a = a-b
print("使用求和法得出结果：")
print("a变换后为：%d"% a)
print("b变换后为：%d"% b)