import time

now = time.strftime("%y-%m-%d %H:%M:%S")
text = input("请输入今天学的知识：")
with open("D:\软件安装\Python\日记.txt","a",encoding="utf8") as f:
    f.write(now+"\n")
    f.write(text+"\n")
    f.write("-------------------------------")
