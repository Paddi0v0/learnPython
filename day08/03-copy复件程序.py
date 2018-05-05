#1.获取要拷贝的文件名
name = input("请输入要拷贝的文件名:")
#2.对获取的文件名进行添加 [复件] 操作
'''
第一种方法切割法
names = name.split('.')
namesWr = names[0]+'复件.'+names[1]
'''
position = name.rfind('.')
names = name[0:position]+'[复件]'+name[position:]

f = open(name, 'r')
test = f.read()
f.close()
wr = open(names, 'w')
wr.write(test)
wr.close()
