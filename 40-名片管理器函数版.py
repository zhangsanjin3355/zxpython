#全局变量
#用来存储名片
card_infors = []
def print_menu():
    """完成打印功能菜单"""
		print("="*50)
		print("      名片管理器1.0     ")
		print("1.添加一个新名片")
		print("2.删除一个名片")
		print("3.修改一个名片")
		print("4.查询一个名片")
		print("5.显示所有的名片")
		print("6.退出系统")
		print("="*50)
        

def add_new_card_infor():
    """完成新建一个名片"""
    new_name = input("请输入姓名:")
    new_qq = input("请输入QQ:")
    new_addr = input("请输入地址:")
    new_weixin = input("请输入你的微信号:")
    #定义一个字典，用来存储新的名片
    new_infor = {}
    new_infor["name"] = new_name
    new_infor["qq"] = new_qq
    new_infor["addr"] = new_addr
    new_infor["weixin"] = new_weixin
    #将一个字典放到一个列表中
    global car_infors
    card_infors.append(new_infor)
   # print(card_infors)

def find_card_infor():
    """用来查询一个名片"""
    global card_infors
    find_name = input("请输入要查询的姓名:")
    for temp in card_infors:
        if find_name == temp["name"]:
            print("%s\t%s\t%s\t%s"%(temp["name"],temp["qq"],temp["addr"],temp["weixin"]))
            break
        else:
            print("查无此人")

def show_allcard():
    """用来显示所有名片"""
    global card_infors
    print("姓名\tqq\t住址\t微信")
    for temp in card_infors:
        print("%s\t%s\t%s\t%s"%(temp["name"],temp["qq"],temp["addr"],temp["weixin"]))

def main():
#1、打印功能输入
    print_menu()



    while  True:

#2、获取用户输入
        num = int(input("请输入你所执行的序号："))
#3、根据用户的数据执行响应的功能
        if num==1:
            add_new_card_infor()
        elif num==2:
            pass
        elif num==3:
            pass
        elif num==4:
            find_card_infor()

        elif num==5:
            show_allcard()
        elif num==6:
            break
        else:
            print("你输入信息非法，请重新输入")
main()
