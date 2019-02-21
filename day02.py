#字符串赋值,切片的打印效果
# var1 = 'Hello World!'
# var2 = 'Runoob!'
# print("var1[0]:",var1[0])
# print("var2[1:5]",var2[1:5])

#整除/取余
# print(7//2) #整除
# print(7%2)  #取余

#查看类型
# a = 100
# print(type(a))
#
# a = 1.12
# print(type(a))
#
# a = 1.1 + 2.2j
# print(type(a))

#字符串赋值,相加
# import string     #全小写字母 字符串
#
# a = string.ascii_lowercase
# print(a)
# import string     #大写加小写字母 字符串
# b = string.ascii_letters
# print(b)

# import string
# print(string.digits)              #数字0-9
# print(string.ascii_uppercase)     #全部大写字母

# str0 = 'abcdefghijklmnopqrstuvwxyz'
# str1 = str0 + str0.upper()        #upper() 小写转大写
# print(str1)

#字符串切片,相加
# var1 = 'Hello World!'
# print("已更新字符串:",var1[:6] + 'Runoob!')

#字符串相加
# str0 = 'abcdefghijklmnopqrstuvwxyz'
# str1 = str0 + str0.upper()
# print(str1)

# a = int(16**0.5) #相当于16的开平方,自动比较
# b = int(2**2)
# print('a==b')

#生成一个10以内的随机数
# import random
# print(random.choice(range(10)))

#随机数宝塔
# import random
# str0 = 'abcdefghijklmnopqrstuvwxyz'
# str1 = str0 + str0.upper()
# print(str1)
# rand_str = ''
# for i in range(1,101):
#     rand_str += random.choice(str1)
#     print(i,rand_str)

#返回数字的绝对值
# print(abs(-10))

#返回数字的上入整数
# import math
# print(math.ceil(4.1))

#返回e的x次幂(e x)   返回e的几次幂
# import math
# print(math.exp(1))

#返回数字的绝对值
# import math
# print(math.fabs(-10))

#向下舍整数
# import math
# print(math.floor(4.9))

#
# import math
# print(math.log(100,10))

# choice() 方法返回一个列表，元组或字符串的随机项。
# import random
# ram1 = random.choice(range(10))
# print(ram1)
#
# print("从range(100)返回一个随机数:",random.choice(range(100)))
#
# print("从列表中[1,2,3,5,9]返回一个随机元素:",random.choice([1,2,3,5,9]))
#
# print("从字符串中'Runoob'返回一个随机字符:",random.choice('Runoob'))

#randrange() 方法返回指定递增基数集合中的一个随机数，基数缺省值为1。
# 规则
# import random
# random.randrange ([start,] stop [,step])
#从0-99选取一个随机数
# import random
# print("randrange(1,100,2):",random.randrange(1,100,2))
# #从0-99选取一个随机数
# print("randrange(100):",random.randrange(100))
# random():
# random() 方法返回随机生成的一个实数，它在[0,1)范围内。

# import random
# #第一个随机数
# print("random():",random.random())
# #第二个随机数
# print("random():",random.random())

import random
random.seed()
print("使用默认种子生成随机数:",random.random())
random.seed(10)
print("使用整数种子生成随机数:",random.random())
random.seed("hello",2)
print("使用字符串种子生成随机数:",random.random())