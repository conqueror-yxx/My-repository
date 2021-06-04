import  random
num = random.randint(0,1000)
i = 0
amount = 5000
while i <= 15 and amount > 0:
    number = input("请输入您要猜的数：")
    number = int(number)
    if number > num:
        amount = amount - 500
        print("大了,余额剩：",amount)
    elif number < num:
        amount = amount - 500
        print("小了，余额剩：",amount)
    else:
        amount = amount + 3000
        print("恭喜猜中！本次数字为：",num,"余额剩：",amount)
        i = i + 1
    break

