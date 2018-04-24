#求接收到3个数的总和
def test(a,b,c):
    result = a+b+c
   # print("%d+%d+%d=%d"%(a,b,c,result))
    return result
#求3个数的平均值
def test2(a,b,c):
    result = test(a,b,c)  #调用求和函数返还的结果
    result/=3
   # print("平均值:%d"%result)
#求三个数平均值的平方
    return result
def pingfang(a,b,c):
    result = test2(a,b,c) #调用平均值函数返还的结果
    result *= 2
    print('平均值的平方:%d'%result)
num1 = int(input("请输入第1个数字:"))
num2 = int(input("请输入第2个数字:"))
num3 = int(input("请输入第3个数字:"))
pingfang(num1,num2,num3)
