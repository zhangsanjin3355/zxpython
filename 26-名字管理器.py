# 1、打印功能提示
print("="*50)
print("      名字关系器 1.2           ")
print("1:增加一个新名字")
print("2:删除一个名字")
print("3:修改一个名字")
print("4:查询一个名字")
print("5:退出")
print("="*50)
names = []
while True:
# 2、获取用户选择
    num  = int(input("请输入功能序号:"))
    if num==1:
        new_name = input("请输入你的名字:")
        names.append(new_name)
        print(names)
    elif num==2:
        del_name = input("请输入你想删除的名字：")
        if del_name in names: 
            names.remove(del_name)
            print("已删除")
        else:
            print("未找到")
        print(names)

    elif num==3:
        pass
    elif num==4:
        find_name = input("请输入你想查询的名字：")
        if find_name in names:
            print("找到了")
        elif find_name not in names:
            print("没有找到")
    elif num==5:
        break
    else:
        print("输入信息有误")
