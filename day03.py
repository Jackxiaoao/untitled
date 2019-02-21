#问题1：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和
# a = 2.0
# b = 1.0
# s = 0
# for i in range(1,21):
#     s += a/b
#     t = a
#     a = a + b
#     b = t
# print(s)

#问题2：输入一个数a，求1+2!+3!+...+a!的和
# sum = 0
# factorial = 1
# num = int(input('请输入一个数字:'))
# for i in range(1,num+1):
#     factorial = factorial * i
#     sum += factorial
# print("阶乘之和:",sum)

#问题3：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if (i != j) and (i != k) and (j != k):
#                 print(i,j,k)


#4.实现100-200里面所有的质数字,打印这些质数并且求出个数
# a = 100
# sum = 0
# for i in range(a,201):
#     if (i % 2 != 0) and (i % 3 != 0) and (i % 5 != 0) and (i % 7 != 0) and (i % 9 != 0) and (i % 11 != 0) and (i % 13 != 0) and (i % 17 != 0) and (i % 19 != 0):
#         print(i)
#         sum += 1
# print("个数:",sum)
#
# a=[]
# for i in range(100,201):
#     b=0
#     for x in range(2,i-1):
#         if i%x==0:
#             b+=1
#     if b==0:
#         a.append(i)
# print(a)
# print(len(a))



