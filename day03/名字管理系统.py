#1.打印功能提示
title = "名字管理系统V1.0"
print("="*60)
print(title.center(55),"\n")
print("1:添加一个新的名字\n")
print("2:删除一个名字\n")
print("3:修改一个名字\n")
print("4:查找一个名字\n")
print("5:退出程序\n")
print("="*60)
#2.获取用户的选择
names = []
while(True):
    num = input("请输入功能序号:")
    if num.isdigit():
        num = int(num)
#3.根据用户的选择，执行相应的功能
        if num == 1:
            name = input("请输入要添加的姓名:")
            names.append(name)
            print(names)
        elif num == 2:
            name = input("请输入要删除的名字:")
            names.remove(name)
            print(names)
        elif num == 3:
            print(names)
            name_num = int(input("请输入您要修改名字的下标:"))
            names[name_num] = input("请输入修改后的名字")
            print(names)
        elif num == 4:
            find_name = input("请输入要删除的名字:")
            if find_name in names:
                print("找到了")
            else:
                print("差不此人")
        elif num == 5:
            out = input("您确定要退出吗?yes/no\n")
            if out.lower() == "yes":
                break
            else:
                print("请输入正确的yes/no")
        else:
            print("请输入正确的功能序号:")
    else:
            print("请输入正确的功能序号:")
print("感谢使用.")
