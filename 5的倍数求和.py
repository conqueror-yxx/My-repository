print("有以下一个列表，求其中是5的倍数的和")
a = [1,5,21,30,15,9,30,24]
sum = 0
for data in a:
    if data % 5 == 0:    #data除以5的余数等于0
        sum =  sum + data
print("5的倍数总和为：",sum)
