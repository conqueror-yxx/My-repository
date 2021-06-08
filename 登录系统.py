print("实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）")
name = "root"
password = "admin"
i = 1
while i <= 3:
    n = input("请输入用户名：")
    p = input("请输入密码：")
    if n == name and p == password:
        print("恭喜，登陆成功！")
        break
    else:
        print("密码输入失败！")
        if i == 3:
            print("三次密码输入错误！系统已锁定，请在30分钟后重新登陆！")
            break
        i = i + 1
