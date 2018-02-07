
def sum_2_nums(a,b):
    if a  == '' and b == '':
        print("输入信息非法，请重新输入")
        exit()
    else:
        result = a+b
        print("%d+%d=%d"%(a,b,result))
    







num1 = int(input("请输入第1个数字："))
num2 = int(input("请输入第2个数字："))
'''if num2 != int:
    print("输入信息非法，请重新输入")'''


sum_2_nums(num1,num2)
