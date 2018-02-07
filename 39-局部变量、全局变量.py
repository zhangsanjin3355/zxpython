#局部变量
'''def get_wendu():
    wendu = 33
    return wendu

def print_wendu(wendu):
    print("当前的温度是：%d"%wendu)

result = get_wendu()
print_wendu(result)
'''
#全局变量
#定义一个全局变量
wendu = 0

def get_wendu():
    #如果wendu这个变量已经在全局变量的位置定义了，此时还想在函数中掉这个全局变量进行修改的话
    #那么仅仅是 wendu=一个值， 这还不够，此时wendu这个变量是个局部变量 ,仅仅和全局变量的名字 
    #相同罢了

    #使用global对一个全局变量的声明，那么这个函数中的wendu=33就不是定义一个局部变量，而是对全局
    #变量修改
    global wendu
    wendu = 33
   # return wendu

def print_wendu():
    print("当前的温度是：%d"%wendu)

get_wendu()
print_wendu()
