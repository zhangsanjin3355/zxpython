import random
play = int(input("请输入：剪刀（0）\t石头（1）\t布（2）"))
computer = random.randint(0,2)
if (play==0 and computer==2) or (play==1 and computer==0) or (play==2 and computer==1):
    print("恭喜你赢了，再来一局")
elif play==computer:
    print("打平了，不要走决战到天亮")
else:
    print("输了回家拿钱")
    
