# 定义一个存放名片字典的列表
card = []

# 功能提示函数
def print_menu():
    '''这是一个用来打印功能提示的函数'''
    print("="*60)
    titlt = "名片管理系统V0.01"
    print(titlt.center(60),"\n")
    print(" 1. 添加一个新的名片\n")
    print(" 2. 删除一个名片\n")
    print(" 3. 修改一个名片\n")
    print(" 4. 查找一个名片\n")
    print(" 5. 显示所有的名片\n")
    print(" 6. 退出系统\n")
    print("="*60)

# 接受数据函数
def input_function():    
    '''这是一个用来接受数据，并把数据打包成字典，存放到列表里的函数'''
    global card
    new_name = input("请输入新的名字:")
    new_addr = input("请输入新的地址:")
    new_age = input("请输入新的年龄:")
    new_tel = input("请输入新的手机号:")
    #定义一个新的字典,来存储一个新的名片
    new_infor = {}
    new_infor['name'] = new_name
    new_infor['addr'] = new_addr
    new_infor['age'] = new_age
    new_infor['tel'] = new_tel
    #把字典存放到列表里
    card.append(new_infor)

# 定义一个查找函数
def search_card():
    '''查找有没有此人的名片'''
    name_search = input("请输入要查找的名字:")
    global card
    for search in card:
        if name_search == search['name']:
            print("找到了")
            break
    else:
        print("查无此人")

# 定义一个显示名片的功能
def show_all_card():
    '''显示所有的名片信息'''
    global card
    print("姓名\t地址\t年龄\t手机号")
    for temp in card:
        print("%s\t%s\t%s\t%s"%(temp['name'], temp['addr'], temp['age'], temp['tel']))

def main():
    #调用打印菜单函数
    print_menu()

    while True:
        # 获取用户的输入
        num = input("请输入功能序号")
        if num.isdigit():
            num = int(num)
            if num == 1:
                input_function()
    #            print(card) for test
            elif num == 2:
                pass
            elif num == 3:
                pass
            elif num == 4:
                search_card()
            elif num == 5:
                show_all_card()
            elif num == 6:  
                out_function = input("您确定要退出程序吗? yes/no\n")
                if out_function.lower() == "yes":
                    break
                else:
                    print("您的输入有误，请重新选择")
        else:
            print("您的输入有误")
main()

'''
查找函数的另一种写法:
    search_flag = 0
    for search in card:
        if name_search == search['name']:
            print("找到了")
            search_flag = 1
            break
    if search_flag == 0:
        print("查无此人")
'''

