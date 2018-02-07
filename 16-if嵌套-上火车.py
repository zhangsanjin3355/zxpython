ticket = 1
knifeLenght = 11
if ticket == 1:
    print("有车票可以进入车站")
    if knifeLenght <=10:
        print("通过安检，可以进去候车大厅")
    else:
        print("安检异常，等待公安机关")
else:
    print("无车票不能进入")
