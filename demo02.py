'''
#判断 python代码块以空格为考量依据
age = int(input("请输入您的年龄："))
if age > 60:
    print("您该退休了。")
elif age >= 30:
    print("您的家庭负担很重吧。")
elif age >= 20:
    print("一定要做好未来规划啊！")
else:
    print("好好学习啊！")

#while循环
a = 1
while a < 10:
    print("hhhhhh",a)
    a += 1

#for循环
b = ["ninhao","wohaishihui","mengjianni","pengzizhou","qojvran","bugandaofannao","wojvran","haixiang","jvxumengjianni"]
for i in b:
    print(i)

#rage() 数列生成器
c1 = range(100)
print(c1)
c2 = list(range(0,100))
print(c2)
c3 = list(range(0,100,2))   #步进/步长
print(c3)


#打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(j,"×",i,"=",i*j,end="  ")     #end 不换行
    print() #换行
'''    

#方法
def jiajian(a,b):
    '''
        这个方法用于实现两个数的相加
    '''
    if type(a) is int and type(b) is int:
        print(a+b)
    else:
        print("您的输入有误，请输入数字！")


jiajian(22,66)