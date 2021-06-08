print("一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。")
bai = 3
wan = 2
h = 20
count = 0
high = 0
while True:
    count = count + 1

    high = high + bai
    if high >= h:
        break
    high = high - wan

print("第",count,"天能爬出来！")