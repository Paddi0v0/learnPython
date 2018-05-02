#一个函数在函数里面调用了自己,这叫做递归
def digui(num):
    if num > 1:
        return num * digui(num-1)
    else:
        return num
num = int(input("请输入阶乘数:"))
if num >0 :
    result = digui(num)
    print(result)
elif num == 0:
    print(1)
else:
    print("您的输入有误,请重新输入")













'''
def jiecheng():
    test = int(input("请输入要阶乘的值:"))
    i = 1
    while test>0:
        i *= test
        test -= 1
    print(i)
jiecheng()
'''
