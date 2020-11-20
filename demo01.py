print("您好！世界。")
"""
a=input("请输入：")
print("input输入的内容为：",a)
"""
#type 获取数据类型
print(type("字符串"))   #字符串
print(type(111))    #整数
print(type(22.2))   #小数
print(type(True))   #布尔型
print(type(()))     #元组
print(type([]))     #数组
print(type({}))     #字典

#数据类型转换
b = int("23333")
print(type(b))

'''
#字符串相加，用len获得字符串长度
h = input("第一段：")
c = input("第二段：")
y = input("第三段：")
print(len(h + c + y))
'''

#元组
a = (1,2,3,"嘻嘻","哈哈","哈哈","哈哈","哈哈","哈哈","哈哈",True,False)    #定义一个元组
print(a.index("嘻嘻"))     #查找值的下标
print(a.count("哈哈"))     #统计值的数量
#切片
print(a[:3])    #左闭右开
print(a[3:10])
print(a[10:])

#二位元组
b = (a,"嘻嘻","哈哈")   #b里面有3个元素
print(b[0][2])  #拿到a里面的3

#数组
c = [1,2,3,"嘻嘻","哈哈","哈哈","哈哈","哈哈","哈哈","哈哈",True,False]
'''
元组和数组的区别：
    元组一旦写好过后不能修改，而数组可以
'''
c.append("append")  #在数组尾巴上添加
print(c)

c.insert(0,"insert")    #在数组指定位置上添加
print(c)

d = c.pop(4)    #剪切数据
print(c)
print(d)

xx = ["你好","合并数组啦"]  #合并数组
c.extend(xx)
print(c)

#c.clear()  清空数组

#字典的特点
    #字典里面的元素没有顺序
    #字典的结构必须是 键值对的结构 key：value
e = {"name":"zhangsan","age":20,"high":183}
#取值
print(e["name"])
#新增
e["xinbie"] = "男"
print(e)
#修改
e["name"] = "pengzizhou"
print(e)

name = e.get("name")
print(name)

pname = e.pop("name")
print(pname)

e.update(high = 184)
print(e)
