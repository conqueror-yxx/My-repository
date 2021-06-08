print("从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）")
a=float(input("请输入第一条边："))
b=float(input("请输入第二条边："))
c=float(input("请输入第三条边："))
if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("三角形为等边三角形")
    elif a==b or a==c or b==c:
        print("三角形为等腰三角形")
    elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        print("三角形为直角三角形")
    else:
        print("三角形为普通三角形")
else:
    print("不能形成三角形")