def test(a,b,c=33,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
A = [11,22,330]
B = {'name':'liuwendang', 'age':21}
#test(11,22,33,44,55,66,name='liuyongshuo',age=21)
test(11,22,33,*A,**B)
