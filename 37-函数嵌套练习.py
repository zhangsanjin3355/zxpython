def sum_3_num(a,b,c):
    result = a+b+c
   # print("%d+%d+%d=%d"%(a,b,c,result))
   # print(result)
    return result



def average_3_num(a,b,c):
    result2 = sum_3_num(a,b,c)
    result2 /= 3
    #print("平均值是：%d" % result2)
    return result2

    
def square_3_sum(a2,b2,c2):
    result3 = average_3_num(a2,b2,c2)
    result = result3*result3
    
    print("三个数平均值的平方是：%d"%result)
num1 = int(input("第1个值："))
num2 = int(input("第2个值："))
num3 = int(input("第3个值："))

#sum_3_num(num1,num2,num3)
#average_3_num(num1,num2,num3)
square_3_sum(num1,num2,num3)









