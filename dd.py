#电脑随机生成1~100随机数，用户输入一个数字，电脑提示用户大或者小，猜错，继续提示；猜对，则程序终止。
import random
a = random.randint(1,101)
for i in range(1,101):
    b = int(input("请输入一个数字:"))
    if b > a:
        print("大")
    elif b == a:
        print("猜对")
        break
    elif b < a:
        print("小")