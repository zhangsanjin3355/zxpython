sex = input("请输入你的性别：")
if sex=="男":
    color = input("你白吗？")
    money = input("请输入的是资产：")
    beautiful = input("你美吗？")
    if color=="白" and money>"100" and beautiful=="美":
        print("白富美...")
    else:
        print("丑")
else:
    higt = input("你高吗？")
    money = input("你的资产总和：")
    beautiful = input("你帅吗？")
    if higt>"180" and money>"500" and beautiful=="帅":
        print("高富帅...")
    else:
        print("丑")    
