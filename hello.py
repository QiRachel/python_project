# 单行注释
# print("HELLO IMOOC")
"""
多行块注释
print("2020")
print(2020)
"""

'''
这是一个注释
'''
# ##############################变量类型
"""
Python有五个标准的数据类型：
Numbers（数字）
String（字符串）
List（列表）
Tuple（元组）
Dictionary（字典）
"""

'''
name = 'qiqi'
print(type(name))
age=22
print(type(age))
salary=1111.11
print(type(salary))
isBig = True

print(type(5 + 4))
print(100 / 4)
print(type(100 / 4))

print(1/2) # 0.5
print(1/0) # ZeroDivisionError: division by zero
print(6/3) # 2.0

print(7//3) # 2


result = (18/9) ** (8%3)
print(result)

m = 10
n = 5
# 变量m的值加3，n的值加5
m = m + 3
n = n + 5
# 求m和n的平均值
averageResult = (m + n)/2
# 求m的平方乘以n的平方
productResult = m**2 * n**2
# 根据效果图进行输出averageResult、productResult
print("m和n的平均值：",averageResult,"\nm的平方乘以n的平方值：",productResult)
'''

"""
price = input('请输入单价：')
print(price)
num = input('请输入数量：')
print(num)
total = float(price) * int(num)
print(total)
"""

# name = " "
# print(type(name))
# strText = 'Hello'
# srtInt = 2020
# resultStr = strText + str(srtInt)
# print(resultStr)

# name = "mA li"
# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.title())
# print(name.swapcase())

# str.format
"""
print("我叫{}，今年{}岁，身高{}，体重{}".format('qiqi', 22, 170, 122))
print("我叫{3}，今年{0}岁，身高{1}，体重{2}".format(22, 170, 122, 'qiqi'))
print("我叫{name}，来自{where}，今年{age}岁，身高{h}，体重{w}".format(w=122, name='qiqi', where='yc',age=22, h=170, ))
"""

# format()数字格式化，返回的是字符串

"""
print(format(1231111456, ','))
print(format(1231111456, '0,.2f'))
print(type(format(1231111456, ',')))

print(format(123.456, '0.2f'))
print(format(123.456, '.2f'))
"""

# str.format()数字格式化，0代表整数部分,.代表小数部分
# 如果遇到格式化输出的是数字，需要在{ }内增加冒号：前缀，之后写上数字格式化语句时，
# 数字格式化语句的千分位分隔符为(,)及保留x位小数的格式为（0.Xf）|(.Xf)
"""
print("{:.2f}".format(3.1415926))   # 3.14
print("{:0.2f}".format(4523.1415926))   #4523.14
print("{:0,.2f}".format(4523.1415926))   #4,523.14
acount = 1001111
money = 123456789
print("请向账户{}转帐￥{:0,.2f}元".format(acount, money))
print("请向账户{1}转帐￥{0:0,.2f}元".format(money, acount))
print("请向账户{acount}转帐￥{money:0,.2f}元".format(money=money, acount=acount))
"""

# 早期字符串格式化
"""
name = 'alice'
age = 18
weight = 48.5
print('我叫%s, 今年%d岁，体重%.2fkg' % (name, age, weight))
"""

# ##############字符串
"""
len(str)
string.capitalize()     把字符串的第一个字符大写
string.lower()          转换所有大写字符为小写.
string.upper()          转换所有小写字母为大写
string.title()          翻转 string 中的大小写
string.swapcase()       所有单词都是以大写开始，其余字母均为小写

string.lstrip()         截掉 string 左边的空格
string.rstrip()         删除 string 字符串末尾的空格.
string.strip([obj])     在 string 上执行 lstrip()和 rstrip()

string.count(str, beg=0, end=len(string))   返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
string.find(str, beg=0, end=len(string))    测字符串中是否包含子字符串 str ,包含子字符串返回开始的索引值。如果不包含索引值，返回-1
string.rfind(str, beg=0,end=len(string) )   类似于 find()函数，不过是从右边开始查找.
string.index(str, beg=0,end=len(string) )   该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。
string.rindex(str, beg=0,end=len(string))   类似于 index()，不过是从右边开始.
string.join(seq)        将序列(列表、元组、字符串)中的元素以指定的字符连接生成一个新的字符串
string.format()         格式化字符串
string.replace(old, new[, max])             把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次

"""
"""
table = "name\tsex\tage\nalice\tfel\t18"
print(table)

str = "   hello world    "

print(str)
print(len(str))
# print(str.strip())
# print(len(str.strip()))
# print(str.rstrip())
# print(len(str.ltrip()))
print(str.lstrip())

str1 = "  imooc      "
# 定义变量lenStr,存放字符串的长度
lenStr = len(str1)
# 根据效果图输出字符串的长度
print("字符串长度："+str(lenStr))
# 定义变量strC，存放去掉左右空白的字符串
strC = str1.strip()
# 根据效果图对去掉空白后的字符串及字符串的长度进行输出
print("去除空白后的字符串："+strC)
print("去除空白后字符串的长度："+str(len(strC)))

str.find(str, beg=0, end=len(string))返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1
str.replace(old, new[, max])把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次
print('aabbbcccc'.replace('b', 'm', 3))
print('aabbbcccc'.replace('b', 'm', 4))

print(len(' '))
print(len('\t'))
"""

# 比较运算符 ==
# 数字不等于数字字符串
# sting == True 为false
# (1 | 1.0) == True 为True
# (0 | 0.0) == False 为True
# 字符串区分大小写

"""
print(1 == 1.0)  # True
print(1 == '1')  # False
print("1" == 1.0)  # False
print('1' == '1.0')  # False
print(1 == '1.0')  # False

print(1 == True)  # True
print(1.0 == True)  # True
print(0 == True)  # False


print(0 == False)  # True
print(0.0 == False)  # True
print("0 "== False)   #  False

print(2222 == True)  # False
print("1" == True)  # False
print("0" == True)  # False
"""

# 数字与字符串比较
"""
# if "2" > 1: #TypeError: '>' not supported between instances of 'str' and 'int'
#     print("'2' > 1")

if "2" > '1':
    print("'2' > '1'")  # '2' > '1'

if "0" > '1':
    print("0>1")
else:
    print("0<1")    #0<1
"""

# 流程控制
"""
顺序控制
分支控制
循环控制
"""
# age = 3
# if age < 5:
#     print('幼儿')
#     print('青少年')
# # else if age < 10:
# #     print('少年')
# else:
#     print('成年')
#
# print('老年')

# 判断是否是闰年
"""
# 定义变量year，并接收“请输入正确的年份：”
year = input('请输入正确的年份:')
year = int(year)
# 判断是否是闰年：1、能被4整除,但是不能被100整除的年份 2、能被400整除的年份
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("{0}年是闰年".format(year))
else:
    print("{0}年不是闰年".format(year))
"""

# 水仙花数
"""
num = int(input("请输入一个三位数："))
# 分别求出三位数的个位，十位，百位
# num = 153
gw = num % 10
sw = (num - gw) % 100 / 10
bw = (num - gw - sw * 10) / 100
# print(gw, sw, bw)
# 定义变量total，保存各位数字立方和
# total = gw ** 3 + sw ** 3 + bw ** 3
total = pow(gw, 3) + pow(sw, 3) + pow(bw, 3)
# print(total)
# 用if语句判断条件是否成立，并做出相应的输出
# 补全代码
if total == num:
    print("{}是水仙花数".format(num))
else:
    print("{}不是水仙花数".format(num))
    
"""
# int("101.1")报错,int(101.1)=101
"""
# total = int(input("请输入您要充值的金额："))
# if total > 100:
#     print("大于100")
# else:
#     print("小于等于100")

# num = int("101.1")#ValueError: invalid literal for int() with base 10: '101.1'
# num = int(101.1) # 101
# print(num)   
"""

"""
# 定义变量x接收输入的第一个数
x = input("请输入第一个数：")
# 定义变量y接收输入的第二个数
y = input("请输入第二个数：")
# 判断x是否等与y
if x == y:
    print("两数相同")
# 判断x是否大于y，条件成立输出 x，反之输出y
else:
    if x > y:
        print("较大数为:", x)
    else:
        print("较大数为:", y)

# str = 'hello'
# print(str, str, str)
"""

"""
sum1 = 0
num1 = 1
while num1 <= 1000:
    if num1 % 2 == 1:
        sum1 = sum1 + num1
    num1 = num1 + 1
print(sum1)
"""

"""
num = 1
count = 0
# 循环条件
while num <= 100:
    # 循环体，设置条件
    # 补全代码
    if (num % 3 == 0 or num % 7 == 0) and not (num % 3 == 0 and num % 7 == 0):
        # print(num)
        count = count + 1
    num = num + 1
print(count)
"""

"""
n = 1
t = 4
# 使用while循环条件，控制输出的行数
while n <= t:
    x = 1  # n-x
    # 使用while循环条件，输出空格
    # t = n - x
    while x <= 4-n:
        print(' ', end='')
        x = x + 1
    # 2 * n - 1
    y = 1
    while y <= 2 * n - 1:
        print('*', end='')
        y = y + 1
    print('')
    n = n + 1
"""
# in 成员运算符
# is 身份运算符
# 2020 == "2020" false
"""
a = 20
b = 20
if a is b:
    print("1 - a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有相同的标识")

a = 20
b = 20.0
if a is not b:
    print("2 - a 和 b 没有相同的标识")
else:
    print("2 - a 和 b 有相同的标识")

a = [1, 2, 3]
b = a
if b is a:
    print("3 - a 和 b 有相同的标识")

b = a[:]
print(b)
print(b is a)

str1 = 2020
str2 = "2020"
print('数值比较结果:', str1 == str2)  # 数值比较结果: False
print('内存地址比较结果:', str1 is str2)    # 内存地址比较结果: False
"""

# 位运算
"""
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0

c = a & b  # 12 = 0000 1100
print("1 - c 的值为：", c)

c = a | b  # 61 = 0011 1101
print("2 - c 的值为：", c)

c = a ^ b  # 49 = 0011 0001
print("3 - c 的值为：", c)

c = ~a  # -61 = 1100 0011= -(~1100 0011+1)=-(00111100+1)=-00111101
print("4 - c 的值为：", c)

c = a << 2  # 240 = 1111 0000
print("5 - c 的值为：", c)

c = a << 3  # 480 = 11 1100000
print("5 - c 的值为：", c)

c = a >> 2  # 15 = 0000 1111
print("6 - c 的值为：", c)

c = a >> 3  # 7 = 0000011 1
print("6 - c 的值为：", c)
"""

"""
a = 34  # 00100010
b = 27  # 00011011
c = a & b  # 00000010
print(c)

a = 56  # 111000
b = 19  # 010011
c = a | b  # 111011
print(c)
"""

# #######列表
"""
# 范围取值是左闭右开，python大部分范围取值都适用
len(list)
list(seq)   将元组转换为列表
list.append(obj)        在列表末尾添加新的对象
list.count(obj)         统计某个元素在列表中出现的次数
list.extend(seq)        在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list.index(obj)         从列表中找出某个值第一个匹配项的索引位置
list.insert(index, obj) 将对象插入列表
list.pop([index=-1])    移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list.remove(obj)        移除列表中某个值的第一个匹配项
list.reverse()          反向列表中元素
list.sort(cmp=None, key=None, reverse=False)    对原列表进行排序
"""

"""
aList = [123, 'xyz', 'zara', 'abc', 123]
bList = aList[1: 4]  # ['xyz', 'zara', 'abc']
cList = aList[0: 1]  # [123]
print(bList, cList)
"""

# list + list
"""
aList = [123, 'xyz', 'zara', 'abc', 123]
bList = [2009, 'manni',123]
cList = aList + bList
print("Extended List : ", aList)
print("Extended List : ", cList)
"""

# list.index(item) 函数用于从列表中找出某个值第一个匹配项的索引位置。
"""
aList = [123, 'xyz', 'zara', 'abc', 123]
print("index List : ", aList.index(123))  # 0
print("index List : ", aList.index('123'))  # ValueError: '123' is not in list
"""

# for ... in ...
"""
aList = [123, 'xyz', 'zara', 'abc', 123]
for item in aList:
    print(item)
# 123
# xyz
# zara
# abc
# 123

numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 1
for item in numList:
    if item % 2 == 0:
        print("第{}个偶数{}".format(i, item))
        i += 1
# 第1个偶数2
# 第2个偶数4
# 第3个偶数6
# 第4个偶数8
# 第5个偶数10
"""

# list.reverse() 函数用于反向列表中元素。
"""
aList = [123, 'xyz', 'zara', 'abc', 123, '456', 456]
aList.reverse()
print(aList)  # [456, '456', 123, 'abc', 'zara', 'xyz', 123]
"""

# list.sort(cmp=None, key=None, reverse=False)
# cmp -- 可选参数, 如果指定了该参数会使用该参数的方法进行排序。
# key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
"""
aList = [28, 32, 1, 56, 99, 10, 12]
aList.sort()
print(aList)  # [1, 10, 12, 28, 32, 56, 99]

aList.sort(reverse=True)
print(aList)  # [99, 56, 32, 28, 12, 10, 1]

aList = [123, 'Google', 'Runoob', 'Taobao', 'Facebook']
aList.sort()
print(aList)  
# TypeError: '<' not supported between instances of 'str' and 'int'
# 1.Python3中，在使用sort()方法排序时，列表中的数据类型不能有不同类型的元素，否则会报错
#2.在Python2中是没有要求的

aList = ['e', 'a', 'u', 'o', 'i']
aList.sort()
print(aList)  # ['a', 'e', 'i', 'o', 'u']
"""

#  #######冒泡排序，前后2个值两两比较

# #####列表新增，修改，删除操作#####
"""
list.append(item)             在列表末尾添加新元素
list.insert(index,item)       指定指定位置插入新元素
list1.extend(list2)           在列表末尾一次性追加另一个序列中的多个值
list[index] = 新值            更新指定位置数据
list[start:end] = 新列表      更新指定范围内数据,范围取值左闭右开
list.remove(元素)             删除指定的元素
list.pop(索引)                删除指定位置元素
del list[索引]
"""

# list.append(item)在列表末尾添加新元素
"""
aList = [123, 'xyz', 'zara', 'abc', 123]
aList.append(456)
print("append List : ", aList)  
# append List :  [123, 'xyz', 'zara', 'abc', 123, 456]

#补充
aList = [123, 'xyz', 'zara', 'abc']
aList.append([456,789])
print("append List : ", aList)
#append List :  [123, 'xyz', 'zara', 'abc', [456, 789]]
"""

# list1.extend(list2)
"""
aList = [123, 'xyz', 'zara', 'abc', 123]
bList = [2009, 'manni',123]
aList.extend(bList)
print("Extended List : ", aList)
"""

# list.insert(index,item)指定指定位置插入新元素
"""
aList = [123, 'xyz', 'zara', 'abc']
aList.insert(2, 'mmm')
print("List : ", aList)
# List :  [123, 'xyz', 'mmm', 'zara', 'abc']

#补充
aList = [123, 'xyz', 'zara', 'abc']
aList.insert(2, [333,444])
print("List : ", aList)
#List :  [123, 'xyz', [333, 444], 'zara', 'abc']
"""

# list.pop([index=-1])移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
"""
aList = [123, 'xyz', 'zara', 'abc']
aList.pop()  # [123, 'xyz', 'zara']
# aList.pop(1) # [123, 'zara', 'abc']
print(aList)
aList = [123, 'xyz', 'zara', 'abc']
del aList[1]  # [123, 'zara', 'abc']
print(aList)
# 范围删除
aList = [123, 'xyz', 'zara', 'abc']
del aList[1:3]  # [123, 'abc']
print(aList)
# 范围删除
aList = [123, 'xyz', 'zara', 'abc']
aList[1:3] = []  # [123, 'abc']
print(aList)
"""

# list.remove(item)移除列表中某个值的第一个匹配项
"""
aList = [123, 'xyz', 'zara', 'abc', 'xyz']
print("xyz : ", aList.count('xyz'))
aList.remove('xyz')
print("List : ", aList)
aList.remove('abc')
print("List : ", aList)
"""

# list.copy() 复制
"""
aList = [1, 2, 3, 'a', 'b', 'c']
bList = aList.copy()
cList = aList
dList = aList[:]
# print("bList : ", bList)  # bList :  [1, 2, 3, 'a', 'b', 'c']
# print("cList : ", cList)  # cList :  [1, 2, 3, 'a', 'b', 'c']
# print("dList : ", dList)  # dList :  [1, 2, 3, 'a', 'b', 'c']
# # is 身份运算符用于判断2个变量是否指向同一块内存
# print("bList is aList : ", bList is aList)  # bList is aList :  False
# print("cList is aList : ", cList is aList)  # cList is aList :  True
# print("dList is aList : ", dList is aList)  # dList is aList :  False

# print(id(aList))    # 1496204468808
# print(id(cList))    # 1496204468808

# print(id(bList))    # 1496204468872

# aList = [3, 'a']
# print("aList = [3, 'a']")
# print(id(aList))    # 1496204954440
# print(id(cList))    # 1496204468808
# print("aList : ", aList)    # aList :  [3, 'a']
# print("bList : ", bList)    # bList :  [1, 2, 3, 'a', 'b', 'c']
# print("cList : ", cList)    # cList :  [1, 2, 3, 'a', 'b', 'c']
# ？？？？这里的cList并没有改变
# 这是给变量aList赋了一个新的列表。更换了aList的引用的地址，而cList还是引用之前的地址。

# print(id(aList))    # 2532405109320
# print(id(cList))    # 2532405109320
# print("aList[:] = [3, 'a']")
# aList[:] = [3, 'a']
# print(id(aList))    # 2532405109320
# print(id(cList))    # 2532405109320
# print("aList : ", aList)    # aList :  [3, 'a']
# print("bList : ", bList)    # bList :  [1, 2, 3, 'a', 'b', 'c']
# print("cList : ", cList)    # cList :  [3, 'a']
# ？？？？？？？？aList变了，cList也变了
# aList[:] = [3, 'a']这是先获取当前的列表aList，然后给这个列表重新赋值，列表的地址不变

# cList = [1, 2, 3]
# print("aList : ", aList)  # aList :  [1, 2, 3, 'a', 'b', 'c']
# print("cList : ", cList)  # cList :  [1, 2, 3]

# cList[:] = [1, 2, 3]
# print("aList : ", aList)  # aList :  [1, 2, 3]
# print("cList : ", cList)  # cList :  [1, 2, 3]

# aList.append(5555)
# print("aList : ", aList)    # aList :  [1, 2, 3, 'a', 'b', 'c', 5555]
# print("cList : ", cList)    # cList :  [1, 2, 3, 'a', 'b', 'c', 5555]

# 注意：引用的地址不变，操作变量数据，应该原始跟赋值是一起变，除非是某一个更换了引用地址

"""

# list.clear() 清空列表
"""
aList = [1, 2, 3, 'a', 'b', 'c']
bList = aList.copy()
cList = aList  # 指向同一块内存
dList = aList[:]

# aList.clear()
# print("aList : ", aList)  # aList :  []
# print("bList : ", bList)  # bList :  [1, 2, 3, 'a', 'b', 'c']
# print("cList : ", cList)  # cList :  []
# print("dList : ", dList)  # dList :  [1, 2, 3, 'a', 'b', 'c']
#print(aList[0])  # IndexError: list index out of range

# cList.clear()
# print("aList : ", aList)  # aList : []
# print("cList : ", cList)  # cList : []

"""

# 定义一个列表list1为[23, 98, 56, 55, 76, 98, 55]，对列表去重之后降序排序
"""
list1 = [23, 98, 56, 55, 76, 98, 55]
list2 = []
for item in list1:
    if item not in list2:
        list2.append(item)

list2.sort(reverse=True)
print(list2)
"""

# 根据提示，在终端输入月份，并判断该月份属于春，夏，秋，冬中的哪一个季节。
"""
month = int(input("请输入月份："))
reason = [[3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 1, 2]]
rea = ['春', '夏', '秋', '冬']
i = 0
# print(month)
if 0 < month <= 12:
    for item in reason:
        if month in item:
            print('{0}月是{1}季'.format(month, rea[i]))
            break
        i += 1
else:
    print("您输入的月份有误！")
"""

# ##########字典
# 键必须不可变，所以可以用数字，字符串或元组充当,定义时候key:value所以用列表就不行
"""
dict1 = {}
print(type(dict1))

dict2 = {'name': 'alice', 'age': 18}
print(dict2)
print(dict2['name'])

dict3 = dict(name='anna', age=20)
print(dict3)

# 在创建字典时，fromkeys()的第一个参数可以是列表也可以是元组,第二个参数为默认值
dict4 = dict.fromkeys(['name', 'age', 'sex', 'salary'], '')
print(dict4)

# seq = ("name", "sex", "score") # 元组
seq = ["name", "sex", "score"]  # 列表
dict5 = dict.fromkeys(seq)
print(dict5)

dict6 = {'姓名': 'alice', 'age': 18}
print(dict6)
print(dict6['姓名'])  # alice
print(dict6.get('age'))    # 18
print(dict6.get('salary'))  # None
print(dict6.get('salary'), 0)  # 0
print('age' in dict6)   # True
for key in dict6:
    print(key)
    print(dict6[key])

for k, v in dict6.items():
    print(k, v)
    
"""

# 字典的增删改查操作
"""
dict.update(dict2) 把字典dict2的键/值对更新到dict里。有则跟新，无则新增
dict.pop(key[,default]) 删除原字典给定键 key 及对应的值,有返回值返回删除的值
dict.popitem()  返回并删除字典中的最后一对键和值
dict.clear()  清空所有
dict6.get(key), default=None)  # 返回指定键的值，如果值不在字典中返回默认值,不会在原字典添加新键
"""
"""
team = {
    'grade': 'a',
    'name': 'alice',
    'age': 18,
    'sex': '女',
    'salary': 1000
}

print(team.get('salary', 0))  # 0
print(team)  # {'grade': 'a', 'name': 'alice', 'age': 18}

print(team)
team['grade'] = 'b'
print(team)

dict2 = {
    'grade': 'c',
    'age': 20,
    'address': 'china'
}
team.update(dict2)
print(team)

team.update(grade='d', salary=2000, phone=123456)
print(team)

item = team.pop('address')
print(item, team)

team.popitem()
team.popitem()
team.popitem()
team.popitem()
team.popitem()
team.popitem()
team.popitem()
item = team.popitem()    # opitem(): dictionary is empty
print(item, team)
"""

# 为字典设置默认值
"""
dict.setdefault(key, default=None)  # 如果键不存在于字典中，将会添加键并将值设为默认值,如果字典中包含有给定键，则返回该键对应的值，否则返回为该键设置的值。
"""

"""
team = {
    'grade': 'a',
    'name': 'alice',
    'age': 18,
}
print(team.get('salary', 0))  # 0
print(team)  # {'grade': 'a', 'name': 'alice', 'age': 18}

team.setdefault('salary', 1000)
print(team)  # {'grade': 'a', 'name': 'alice', 'age': 18, 'salary': 1000}

print(team.setdefault('salary', 1000))  # 1000
print(team.setdefault('grade', 'b'))  # a

"""

# 获取字典的视图
"""
dict.keys() 以列表返回一个字典所有的键
"""
"""
team = {
    'grade': 'a',
    'name': 'alice',
    'age': 18,
}
ks = team.keys()
print(ks)  # dict_keys(['grade', 'name', 'age'])
print(type(ks))  # <class 'dict_keys'> 字典的视图对象

vals = team.values()
print(vals)    # dict_values(['a', 'alice', 18])
print(type(vals))  # <class 'dict_values'> 字典的视图对象

kvs = team.items()
print(kvs)    # dict_items([('grade', 'a'), ('name', 'alice'), ('age', 18)])
print(type(kvs))  # <class 'dict_items'> 字典的视图对象

# 注意，视图 是原始数据的子集，keys，values，items都是字典的一部分，会跟着原始数据的变化产生相应的变化
team['grade'] = 'b'
print(vals)  # dict_values(['b', 'alice', 18])
print(kvs)  # dict_items([('grade', 'b'), ('name', 'alice'), ('age', 18)])
"""

# 字典格式化字符串
"""
format_map
"""
"""
team = {
    'grade': 'a',
    'name': 'alice',
    'age': 18,
}
# print("Equivalent String : %s" % str(dict))

# 老版本格式化
emp_str = "姓名%(name)s等级%(grade)s" % team
print(emp_str)  # 姓名alice等级a

# 新版本格式化
emp_str1 = "姓名{name},等级{grade}".format_map(team)
print(emp_str1)  # 姓名alice,等级a
"""

# hash() 散列值
# 1.同一次运行，值是一样的
# 2.多次运行程序，值是不一样的
# 3.对于整数来说，跟整数值完全相同
"""
h1 = hash('abc')
print(h1)   # 4809744470002676350

h2 = hash(1249236)  # 1249236 就是整数值本身，多次运行，值不会变
print(h2)
h4 = hash(124.9236)  # 2129676603309752444 多次运行，值不会变
print(h4)
h5 = hash(-124)  # -124 多次运行，值不会变
print(h5)
h6 = hash(-124.4562)  # -1051925580803276924 多次运行，值不会变
print(h6)

h3 = hash('abc')
print(h3)   # 4809744470002676350 同一次运行，值是一样的，多次运行，值会变有可能是-3602241439469237472

# 字典存储原理 :key (-》转换) hash() (-》存储)  内存地址->保存value 不是连续存储是分散存储
"""

# split,range()
"""
source = "alice,18,a$nana,23,b$david,50,f"
list1 = source.split('$')
print(list1)
emplpyee = {}
# for i in range(0, len(list1)):    # 遍历下标
#     print(list1[i])
#     e = list1[i].split(',')
#     tem = {
#         'name':e[0],
#         'age':e[1],
#         'grade':e[2]
#     }
#     emplpyee[i] = tem
#
# print(emplpyee)

# for item in aList:
#     print(item) 输出的是value，不是下标

for li in list1:
    print(li)
    e = li.split(',')
    tem = {
        'name':e[0],
        'age':e[1],
        'grade':e[2]
    }
    emplopyee[e[0]] = tem

print(emplpyee)
"""

# ###########################元组与集合###########################

# 元组(tuple)
"""
元组是不可变的列表，元组的元素不能修改
元组使用小括号，列表使用方括号

元组获取数据跟列表一样使用
元组运算符 + *

# 注意如果元组只有一个元素，必须在这个元素后增加逗号，说明这是个元组
# 若元组中存在列表，列表里面内容可以被修改
# 元组运算符同样适用于列表，（不要混合使用，元组+列表）
"""
"""
tup1 = ()
print(tup1)  # ()
print(type(tup1))  # <class 'tuple'>

tup2 = (1, 2, 3)
print(tup2[1])  # 2
print(tup2[-1])  # 3
print(tup2[1:3])  # (2, 3)
print(tup2[1:4])  # (2, 3)
tup3 = (3, 4, 5)

# 元组运算符 + *
tup4 = tup2 + tup3
print(tup4)  # (1, 2, 3, 3, 4, 5)

tup5 = tup2 * 2
print(tup5)  # (1, 2, 3, 1, 2, 3)
# 注意如果元组只有一个元素，必须在这个元素后增加逗号，说明这是个元组
print(( 'se' ) * 6)   # sesesesesese 当成运算优先级
print(( 10 ) * 2)   # 20

print(( 'se', ) * 6)   # ('se', 'se', 'se', 'se', 'se', 'se')
print(( 10, ) * 2)   # (10, 10)

# tup2[0] = 2  # TypeError: 'tuple' object does not support item assignment
# tup2.insert(2, 3)  # TypeError: 'tuple' object does not support item assignment

# 元组中存在列表，列表里面内容可以被修改
tup6 = (['anna',1],['nana',2])
print(tup6) # (['anna', 1], ['nana', 2])
tup6[0][1] = 5
print(tup6) # (['anna', 5], ['nana', 2])
"""

# #####################序列:有序的队列，数据结构的统称
# 序列包括 字符串，列表，元组，数字序列（range）
# range 一旦创建不可变
"""
r = range(0, 10)  # 左闭右开
print(r)    # range(0, 10) range只会定义起始值和结束值
print(type(r))    # <class 'range'>
print(r[9])    # 9
print(r[2:5])    # range(2, 5)

# for i in range(0, 10):
#     print(i)

# 增长步长
r2 = range(1, 10, 2)
print(r2)   # range(1, 10, 2)
print(r2[1])   # 3
# r2[4] = 5   # TypeError: 'range' object does not support item assignment
print(5 in r2)  # True
print(6 in r2)  # False

print(r2[3:5])  # range(7, 11, 2)

# 利用range遍历其他序列
c = 'abcdefg'
print(c[3])     # d
# c[3] = 'h'  #TypeError: 'str' object does not support item assignment
for i in range(0, len(c)):
    print(c[i])

# 斐波那契数列
# 1,1,2,3,5,6,13,...
result = []
for i in range(0, 50):
    if i == 0 or i == 1:
        result.append(1)
    else:
        result.append(result[i-1] + result[i-2])
print(result)   # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,...]

# 质数 只能被1和他本身整除
is_prime = True
l = 4562353
for i in range(2, l):
    if l % i == 0:
        is_prime = False
        print(i)
        break

if is_prime:
    print("是质数")
else:
    print('不是质数')
    
    
# 有四个数字1、2、3、4，能组成多少个互不相同且数字不重复的两位数
count = 0
list = []
for i in range(1, 5):
    for j in range(1, 5):
        if i == j:
            continue
        list.append(i*10+j)
        count +=1
print(count)
print(list)

"""

# 序列类型的强制转换
"""
list() 转换为列表
tuple() 转换为元组
join() str() 转换为字符串

l1 = ['a', 'b', 'c']
t1 = ('d', 'e', 'f')
s1 = 'abc123'
s2 = 'abc,123'
r1 = range(1, 4)


print(list(t1))   # ['d', 'e', 'f']
print(list(s1))  # ['a', 'b', 'c', '1', '2', '3']
print(list(s2))  # ['a', 'b', 'c', '1', '2', '3']
print(s2.split(','))  # ['abc', '123']
print(list(r1))   # [1, 2, 3]

print(tuple(l1))    # ('a', 'b', 'c')

# str() 用于将单个数据转换为字符串
# join() 方法用于将序列(列表、元组、字符串)中的元素(必须是字符串元素)以指定的字符连接生成一个新的字符串。
# join() 对所有元素为字符串的列表，元组，进行连接
# join() 要求要拼接的都是字符串不能是数字，但可以把数字转成数字字符串
print(str(l1))  # ['a', 'b', 'c']
print(type(str(l1)))    # <class 'str'>
print(''.join(l1))   # abc
print(','.join(l1))   # a,b,c
print(' '.join(t1))   # d e f
print(' '.join(s2.split(',')))   # abc 123
# l1 = [1, 2, 3]
# print(' '.join(l1))   # TypeError: sequence item 0: expected str instance, int found
# print(' '.join((r1)))   #TypeError: sequence item 0: expected str instance, int found

res = ''
for i in range(1, 20):
    res += str(i)
print(res)  # 12345678910111213141516171819
print(type(res))    # <class 'str'>
print(','.join(res))    # 1,2,3,4,5,6,7,8,9,1,0,1,1,1,2,1,3,1,4,1,5,1,6,1,7,1,8,1,9

"""

# ################集合################phtyon 数据结构
# {}
# 集合没有value,只有key
# 集合元素是无序的
# 集合元素不能重复
# 集合是可变的
# 集合允许数学运算
# 集合是分散存储
# key =》转换成  hash()  =》 存储  内存地址存hash值，hash值映射数据
# set()是个集合函数，括号里的参数可以是字典类型，列表类型，元组类型，字符串类型，不能是数字类型。

"""
college = {
    "哲学", '法学', '经济学', '教育学'
}
print(college)  # {'教育学', '经济学', '法学', '哲学'}
# {'法学', '哲学', '教育学', '经济学'} 每次运行打印顺序不一样，因为产生的散列值不一样，在内存存在位置不一致

# set() 将其他数据结构转换成集合
# 括号里的参数可以是字典类型，列表类型，元组类型，字符串类型，不能是数字类型。

d1 = {"a":"哲学", "b":'法学', "c":'经济学', "d":'教育学'}
print(set(d1))  # {'a', 'd', 'c', 'b'}

l1 = [1, 2, 3, 4, 5]
print(set(l1))  # {1, 2, 3, 4, 5}
l2 = ["哲学", '法学', '经济学', '教育学']
print(set(l2))  # {'经济学', '哲学', '教育学', '法学'}

t1 = (1,2,3,4,5)
print(set(t1))  # {1, 2, 3, 4, 5}
t2 = ("1","a","f","4","2")
print(set(t2))  # {'1', 'f', '4', '2', 'a'}

print(set("中华人民"))  # {'华', '人', '民', '中'}

print(set("1423456")) # {'1', '4', '3', '6', '2', '5'}

print(set(1423456)) # TypeError: 'int' object is not iterable

print(set())  # set() 空集合
"""

# 集合的数据运算 交集，并集，差集
"""
college1 = {
    "哲学", '法学', '经济学', '教育学'
}
college2 = {
    "历史学", '物理学', '经济学', '数学', '文学', "哲学"
}

# ##交集
# set1.intersection(set2) 产生一个新集合  intersection:交叉
# set1.intersection_update(set2) 更新原始集合
c3 = college1.intersection(college2)    # 创建一个新的集合
print(c3)  # {'经济学', '哲学'}
print(college1)  # {'法学', '哲学', '经济学', '教育学'}

college1.intersection_update(college2)  # 更新原始集合
print(college1)  # {'经济学', '哲学'}

# ##并集
# set1.union(set2) 并集

college1 = {
    "哲学", '法学', '经济学', '教育学'
}
college2 = {
    "历史学", '物理学', '经济学', '数学', '文学', "哲学"
}
c4 = college1.union(college2)
print(c4)   # {'哲学', '历史学', '经济学', '法学', '物理学', '数学', '文学', '教育学'}

# ##差集
# set1.difference(set2) 单向差集
# set1.symmetric_difference(set2) 双向差集   symmetric:对称的
# set1.difference_update(set2) 单向差集,更新原始集合
# set1.symmetric_difference_update(set2) 双向差集,更新原始集合
college1 = {
    "哲学", '法学', '经济学', '教育学'
}
college2 = {
    "历史学", '物理学', '经济学', '数学', '文学', "哲学"
}
c5 = college1.difference(college2)
print(c5)   # {'教育学', '法学'}

c6 = college2.difference(college1)
print(c6)   # {'物理学', '历史学', '文学', '数学'}

c7 = college1.symmetric_difference(college2)    # {'物理学', '法学', '教育学', '数学', '文学', '历史学'}
print(c7)

college1.difference_update(college2)
print(college1)   # {'法学', '教育学'}

s1 = {'love','imooc','good'}
s2 = {'love','imooc','wonderful'}
s1.symmetric_difference_update(s2)
print(s1)
"""

"""
a_list = [1, 2, 3, 4, 5]
b_list = [1, 4, 7, 9]

a_s = set(a_list)
b_s = set(b_list)
# 求两个列表之间的交集
int_list = list(a_s.intersection(b_s))
print(int_list)
# print(int_list)
# 求两个列表之间的并集
uni_list = list(a_s.union(b_s))
print(uni_list)
# 求两个列表之间的差集（a_list在b_list中不存在的部分）
dif_list = list(a_s.difference(b_s))
print(dif_list)
"""

# 集合间的关系操作
"""
issubset 判断是否是子集
issuperset 判断是否是父集
isdisjoint 判断是否 没有重复 元素
"""
"""
s1 = {1, 2, 3, 4, 5, 6}
s2 = {6, 5, 4, 3, 2, 1}
print(s1)  # {1, 2, 3, 4, 5, 6}
print(s2)  # {1, 2, 3, 4, 5, 6}
print(s1 == s2)  # True

s3 = {1, 2, 3, 4}
s4 = {1, 2, 5, 6, 7, 3, 4, }
# issubset判断是否是子集
print(s3.issubset(s4))  # True
# issuperset判断是否是父集
print(s4.issuperset(s3))  # True
# isdisjoint 判断是否没有重复元素
s5 = {5}
s6 = {1, 3, 5, 7, 9}
print(s5.isdisjoint(s6))  # False
print(s6.isdisjoint(s5))  # False
s7 = {6}
print(s7.isdisjoint(s6))  # True
print(s6.isdisjoint(s7))  # True
"""

# 集合的增删改查
"""
set.add(item)  一次只能添加一个元素
set.update([,,])  一次只能添加多个元素
set.remove(item)  一次只能删除一个元素，删除不存在的会报错
set.discard(item)  一次只能删除一个元素，删除不存在的,则忽略删除操作

不支持更新操作,可以先删再增
"""
"""
college = {
    "历史学", '物理学', '经济学'
}
for i in college:
    print(i)

print("历史学" in college)

# 集合不支持按索引提取数据
college.add('生物学')
college.add('经济学')
print(college)  # {'物理学', '历史学', '经济学', '生物学'}

college.update(['生物学', '法学', '文学'])
print(college)  # {'法学', '物理学', '历史学', '生物学', '经济学', '文学'}


college.remove('生物学')
print(college)  # {'物理学', '法学', '历史学', '文学', '经济学'}

# college.remove('美学')    #KeyError: '美学'
college.discard('美学')
"""

# 三种内置生成式
# 列表生成式，字典生成式，集合生成式
# 语法：
# 列表: [被追加数据 循环语句 循环|判断语句]
# 字典,集合 {被追加数据 循环语句 循环|判断语句}
"""
ls1 = []
for i in range(1, 10):
    ls1.append(i * 10)
print(ls1)  # [10, 20, 30, 40, 50, 60, 70, 80, 90]
# 列表生成式
ls2 = [i * 10 for i in range(1, 10)]
print(ls2)  # [10, 20, 30, 40, 50, 60, 70, 80, 90]

ls3 = [i * 10 for i in range(10, 20) if i % 2 == 0]
print(ls3)  # [100, 120, 140, 160, 180]

ls4 = [i * j for i in range(1, 5) for j in range(1, 5)]
print(ls4)  # [1, 2, 3, 4, 2, 4, 6, 8, 3, 6, 9, 12, 4, 8, 12, 16]

# 字典生成式
list5 = ['alice', 'david', 'jeffe', 'nana']
dict1 = {i: list5[i] for i in range(0, len(list5))}
print(dict1)  # {0: 'alice', 1: 'david', 2: 'jeffe', 3: 'nana'}

# 集合生成式
set1 = {i * j for i in range(1, 4) for j in range(1, 4) if i == j}
print(set1)     # {1, 4, 9}

lst = [23,45,22,44,25,66,78]
# 1、生成lst列表中所有奇数组成的列表
lst1 = [i for i in lst if i % 2 == 1]
print(lst1) #[23, 45, 25]
# 2、与lst列表相比较，使用相应的列表生成式，使得输出结果[28, 50, 27, 49, 30, 71, 83]
lst2 = [i+5 for i in lst]
print(lst2)
"""

# #############################################Python函数与模块###############################################
# ##############函数
"""
def fun(参数名):
    return 1
fun(参数名)   

关键字传参
def fun(参数名):
    return 1
fun(参数名=参数值)

混合传参,参数为*号时代表它之后必须使用关键字传参，
def fun(参数名1, *,参数名2, 参数名3):
    return 1
fun(参数值, 参数名2=参数值, 参数名3=参数值)
"""

"""
def login(username, password):
    if username == 'imooc' and password == 123456:
        return "登录成功"
    else:
        return "请重新登录"


login("imooc", 123456)
login(username="imooc", password=123456)
login(password=123456, username="imooc")

def info(*, desc,birth, name='imooc'):

    print("{name}-{desc}出生于{birth}".format(name=name,desc=desc,birth=birth))

info(desc="程序员的梦工厂",birth="2013年8月")
"""

"""
# 1序列传参
def cal(a, b, c):
    return a + b + c


l = [1, 2, 3]
print(cal(*l))  # 6


# 2字典传参
def info(desc, birth, name='qiqi'):
    return "{name}-{desc}出生于{birth}".format(name=name, desc=desc, birth=birth)


param = {"desc": '我', "birth": "2000/01/01"}
print(info(**param))  # qiqi-我出生于2000/01/01

def fun_dict(name, hiredate, tel, dept):
    print("{0}隶属于{3}，电话:{2}, 入职日期：{1}".format(name, hiredate, tel, dept))
    # 小葫芦隶属于技术部，电话:18795642135, 入职日期：2017-9-23


dict1 = {'name': '小葫芦', 'hiredate': '2017-9-23', 'tel': 18795642135, 'dept': '技术部'}
fun_dict(**dict1)

def seq(num, num1, num2):
    # if判断num小于88
    if num < 88:
        return num1 * num2
    else:
        return num1 + num2

# 3元组传参
tuple1 = (5, 2, 1)
print(seq(*tuple1))  # 2
tuple2 = (88, 2, 1)
print(seq(*tuple2))  # 3



"""

# ####################模块
"""
标准模块（内置模块，标准库）
第三方库（pypi.org）
import sys
sys.path
模块查找的顺序是，当前包->内置函数->系统变量
"""
"""
import random

r = random.randint(1, 16)  # 左闭右闭
print(r)
"""

# 模块属性
"""
dir(模块) 列出对象的所有属性和方法
help(模块) 查看类，方法的帮助信息
__name__ 模块名称
__file__ 模块全路径
__doc__ 注释
"""

"""
测试模块使用

if __name__  == "__main__":
    xxfunc()
"""

# 包
"""
用来组织模块，可以包含其他模块
目录必须包含__init__.py
解决模块重命名问题

1.引入整个包import module
2.只引入所需要的属性和方法：from module.xx.xx import xxx
3.指定别名：from module.xx.xx import xxx as xx
4.引入所以：from module.xx.xx import *

使用import module
导入子包需要用,要使用包中的模块，在包中的__init__.py要先引入
__init__.py 中导入 from . import xxx   # .表示当前目录

import顺序
1，标准库
2，三方库
3，自定义包/模块
"""

"""
import random
import django
import pay





# import tools
# tools.main_tool()   # main.tools的工具

# from pay.alipay import tools
# tools.pay()

# from pay.alipay.tools import pay as alipay
# from pay.wxpay.tools import pay as wxpay
# alipay()
# wxpay()

import pay
# pay.alipay.tools.pay()
# pay.tools.main_tool()
pay.alipay.pay()    # alipay  pay/alipay/__init__.py  from .tools import pay
pay.pay_tool()    # 主包下的工具  pay/__init__  from .tools import *

"""

# ##############os模块  (很重要)  文件/目录方法
"""
os.environ 包含环境变量的映射
os.system() 在子shell中执行操作系统命令
os.getcwd() 文件所在目录
os.listdir() 
os.open(file, flags[, mode]) 打开一个文件
os.mkdir(path[, mode]) 创建一个名为path的文件夹
os.makedirs(path[, mode]) 递归文件夹创建函数。
os.sep 查询操作系统路径的分隔符
os.remove(path) 删除路径为path的文件。
	
os.rmdir(path) 删除path指定的空目录，
os.rename(src, dst) 更改名字


import os
os.system("calc")   # 打开计算器
"""
# ##############os模块之path
"""
os.path.split()
os.path.splitext()
os.path.isdir()
os.path.isfile()
os.path.exists()

os.path.basename()

f='D:\\python_project\\desktop.xxx.ini'
os.path.isfile(f)   # True
os.path.split(f)   # ('D:\\python_project', 'desktop.xxx.ini')
os.path.splitext(f) # ('D:\\python_project\\desktop.xxx', '.ini')
"""

# ##############datetime模块
"""
date    date类表示一个日期
datetime.strftime   将datetime对象格式转换成字符串
datetime.strptime   将字符串按照一定格式转换成datetime对象
timedelta 对日期时间进行加减操作

time    表示一个时间的类
datetime.now    系统的当前时间
"""

"""
import datetime
print(dir(datetime))
print(datetime.time)    # <class 'datetime.time'>
print(datetime.time())    # 00:00:00
print(datetime.datetime)  # <class 'datetime.datetime'>
print(datetime.datetime.now())  # 2019-11-16 12:18:28.997073
print(datetime.timedelta)  # <class 'datetime.timedelta'>
print(dir(datetime.datetime))
"""
"""
from datetime import datetime
print(dir(datetime))
print(datetime.now()) # 2019-11-16 12:25:45.101088
print(datetime.today()) # 2019-11-16 12:25:45.809381

now_time = datetime.now()
print(now_time) # 2019-11-16 12:24:33.101088
print(now_time.time()) # 12:24:51.370251
print(now_time.date()) # 2019-11-16
print(now_time.year) # 2019
print(now_time.month) # 11
print(now_time.day) # 16
"""

# ##############time模块（注意有个单独的time模块，也有datetime.time）
# import time
# print(dir(time))    # ...'sleep', 'strftime', 'strptime'....
# print(time.time())  # 1573878671.5353472
"""
import time
print(dir(time))
print("Start : %s" % time.ctime())
time.sleep( 5 )
print("End : %s" % time.ctime())

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))     # 2019-11-16 13:42:58

import calendar
cal = calendar.month(2019, 1)
print("以下输出2019年1月份的日历:")
print(cal)

# 以下输出2019年1月份的日历:
#     January 2019
# Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30 31

"""

# #############datetime模块之时间转换
"""
%A 星期名称，“Monday”
%B 月份名称，“January”
%y 两位年份
%Y 四位年份
%m 月份
%d 日
%H 时    二十四小时
%M 分
%S 秒
%I 时    十二小时
"""
"""
from datetime import datetime, date, time

d = datetime(2019, 11, 11, 11, 10)
print(d)  # 2019-11-11 11:10:00

d1 = date(2019, 11, 11)
print(d1)  # 2019-11-11

t = time(9, 0)  # 09:00:00
print(t)
print(time())
"""

# ######日期，时间，与字符串之间的相互转换
"""
from datetime import datetime

# datetime对象原字符串中年月日之间以‘-’相连且年的表示方式为四位数字全部显示
ds = "2019-01-01 13:50:59"
d2 = datetime.strptime(ds, "%Y-%m-%d %H:%M:%S")  # 2019-01-01 13:50:59
print(d2)
print(type(d2))  # <class 'datetime.datetime'>

ds = "2019/01/01 13:50:59"
# d3 = datetime.strptime(ds, "%Y-%m-%d %H:%M:%S") # time data '2019/01/01 13:50:59' does not match format '%Y-%m-%d %H:%M:%S'
d3 = datetime.strptime(ds, "%Y/%m/%d %H:%M:%S")  # 2019-01-01 13:50:59
print(d3)

dc = datetime.now()
dcs = datetime.strftime(dc, "%Y/%m/%d %H:%M:%S")
print(dcs)  # 2019/11/16 13:00:18
print(type(dcs))  # <class 'str'>
dcs1 = datetime.strftime(dc, "%Y/%m/%d")
print(dcs1)  # 2019/11/16

"""

# #######datetime之间的加减操作timedelta
"""
from datetime import datetime, timedelta

# 加法操作  (获取某个时间差 之后或之前的时间点)
n = datetime.now()
print(n)  # 2019-11-16 13:04:09.578615
n_next = n + timedelta(days=7, hours=12)
n_before = n + timedelta(days=-7)
print(n_next)  # 2019-11-24 01:06:09.613146
print(n_before)  # 2019-11-09 13:53:20.396082

# 减法操作 (获取时间点 之间的时间差)
d1 = datetime(2019, 11, 11)
d2 = datetime(2019, 11, 2)
# rest = d2 - d1  # -9 days, 0:00:00
rest = d1 - d2  # 9 days, 0:00:00timedelta
print(rest)
print(type(rest))  # <class 'datetime.timedelta'>
print(dir(rest))  # ... 'days', 'max', 'microseconds', 'min', 'resolution', 'seconds', 'total_seconds'...
print(rest.days)  # 9
"""

# ####################### python第三方模块
"""
Django,Flask,mysqlClient
https://pypi.org/
pip -- help
安装
1.直接安装pip install Django
2.下载安装 进入下载的包里面安装 执行 python setup.py install
3.下载安装 直接安装压缩包 pip install Flask.zip

pip uninstall Flask
"""

# ###################虚拟环境
"""
virtualenv
pipenv
"""

#   ######################类
# #类的属性和方法
# __bases__ 用于返回一个元组显示所继承的所有父类
# class Cat(object):
"""
class Cat:
    # 类的属性
    tag = 'cat base'

    # 构造方法
    def __init__(self, name, age):
        # 实例化的属性
        self.name = name
        self.__age = age    # 私有变量，无法直接访问修改，可以定义方法获得修改
        pass

    def set_age(self, age):
        self.__age = age
        print("我的年龄:{}岁".format(self.__age))

    def show(self):
        print("我叫{}，今年{}岁".format(self.name, self.__age))

    def eat(self):
        print("猫喜欢吃鱼")


    # 析构方法
    def __del__(self):
        pass

class Tiger(Cat):
    pass

if __name__ == "__main__":
    # cat = Cat()
    # cat.eat()
    cat = Cat('money',3)
    cat.eat()   # 猫喜欢吃鱼
    cat.show()  # 我叫money，今年3岁

    print(cat.name) # money
    cat.name = "huahua"
    print(cat.name) # huahua

    # print(cat.__age) # 私有变量AttributeError: 'Cat' object has no attribute '__age'
    cat.__age = 5
    cat.show()  # 我叫huahua，今年3岁

    cat.set_age(5)
    cat.show()  # 我叫huahua，今年5岁
    print(isinstance(cat, Cat))     # True

    tiger = Tiger('huaniu',10)
    print(isinstance(tiger, Cat))   #True
"""

# #类的实例判断
# isinstance(o,c)
"""
class Vehicle(object):
    # 自定义Vehicle类属性
    trans_type = 'SUV'

    # 自定义实例的初始化方法
    def __init__(self, speed=0, size=()):
        self.speed = speed
        self.size = size

    # 自定义实例方法show_info，打印实例的速度和体积
    def show_info(self):
        # print(type(self))
        print("我的所属属性为{}，速度：{}km/h，体积：{}".format(self.trans_type, self.speed, self.size))

    # 自定义实例方法move,打印“我已向前移动了50米”
    def move(self):
        print("我已向前移动了50米")

    # 自定义实例方法set_speed，设置对应的速度值
    def set_speed(self, new_speed):
        self.speed = new_speed

    # 自定义实例方法get_speed，打印当前的速度值
    def get_speed(self):
        print("我的时速为： {}km/h".format(self.speed))

    # 自定义实例方法speed_up，实现对实例的加速
    def speed_up(self):
        old_speed = self.speed
        self.speed += 10
        print("我的速度由{} km/提升到了{} km/h".format(old_speed, self.speed))

    # 自定义实例方法speed_down，实现对实例的减速
    def speed_down(self):
        old_speed = self.speed
        self.speed -= 15
        print("我的速度由{} km/下降到了{} km/h".format(old_speed, self.speed))

    # 自定义实例方法transport_identify，实现对实例所属类型的判断
    def transport_identify(self):
        if isinstance(self, Vehicle):
            print("类型匹配")
        else:
            print("类型不匹配")


if __name__ == "__main__":
    tool_1 = Vehicle(20, (3.6, 1.9, 1.75))
    # 调用实例方法 打印实例的速度和体积
    tool_1.show_info()
    # 调用实例方法 实现实例的前移
    tool_1.move()
    tool_1.set_speed(40)
    # 调用实例方法 打印当前速度
    tool_1.get_speed()
    # 调用实例方法 对实例进行加速
    tool_1.speed_up()
    # 调用实例方法 对实例进行减速
    tool_1.speed_down()
    # 调用实例方法 判断当前实例的类型
    tool_1.transport_identify()
"""

# ######类的继承
# 子类的判断 issubclass(cls=,classinfo=)
# 调用父类的方法
# def fun(self):
#     super(父类，self).fun()
"""
class BaseCat(object):
    '''
    猫科动物的基础类
    '''
    tag = "猫科动物"

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("所有猫类都要吃东西")


class Tiger(BaseCat):
    '''
    老虎
    '''
    tag = "老虎"

    def eat(self):
        super(Tiger, self).eat()
        print("我还喜欢吃肉")


class Panda(BaseCat):
    '''
    熊猫类
    '''
    tag = "熊猫类"

    def eat(self):
        super(Panda, self).eat()
        print("我还喜欢吃竹子")


panda = Panda('yuan zi')
panda.eat()
# 所有猫类都要吃东西 \n 我还喜欢吃竹子
# 子类eat函数 没有super(Panda, self).eat() 我还喜欢吃竹子
# Panda 里面没有eat方法，则执行父类eat方法   # 所有猫类都要吃东西
#
"""

"""
class Person(object):


# 重写实例对象的构造（初始化）方法

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    # 自定义实例方法，格式化打印实例属性name的值
    def speak(self):
        print("hello ! 我是{}".format(self.name))

    # 自定义实例方法，占位作用
    def relation(self):
        pass

class Student(Person):
    # 重写实例对象的构造（初始化）方法，并调用父类构造方法，实现对实例属性的赋值
    def __init__(self, name, gender,score, major):
        super(Person, self).__init__(name, gender)
        self.score = score
        self.major = major
        self.__stu_num = "2018014002"

    # 自定义实例方法，格式化打印实例属性stu_num的值
    def speak(self):
        # super(Student, self).speak()
        print("我的学号为{}，很高兴认识大家". format(self.__stu_num))

    # 自定义实例方法，判断学号是否为既定值，并根据判断结构 进行分类打印
    def identify_stu(self):
        if self.__stu_num == '2018014002':
            print("我的分组已经完成")
        else:
            print("请稍后，马上为你自动分组")

    # 自定义实例方法，设置实例对象的学号为传入的值
    def set_num(self, new_num):
        self.__stu_num = new_num

    # 自定义实例方法，判断该类是否为Person类的子类，并进行分类打印
    def relation(self):
        if issubclass(Student, Person):
            print("我的父类是Person")
        else:
            print("父类正在查询中······")


if __name__ == '__main__':
    stu = Student('小明', '男', 90, '数学')
    # 调用speak方法 打印stu对应的值
    stu.speak()
    # 调用实例方法 鉴别学号是否为指定值
    stu.identify_stu()
    # 调用实例方法 鉴别实例对象所属的类的父类是否为Person
    stu.relation()

    print("******************")
    stu_2 = Student('小红', '女', 89, '英语')
    # 调用实例方法 设置stu_2的学号为'2018040625'
    stu.set_num('2018040625')
    # 调用实例方法 打印stu_2对应的值
    stu.speak()
    # 调用实例方法 鉴别学号是否为指定值
    stu.identify_stu()
"""

# ####类的多重继承
# class C(A, B)

# ####类的多态
"""
class BaseCat(object):
    '''
    猫科动物的基础类
    '''
    tag = "猫科动物"

    def __init__(self, name):
        print('BaseCat init')
        self.name = name

    def eat(self):
        print("所有猫类都要吃东西")


class Tiger(BaseCat):
    '''
    老虎
    '''
    tag = "老虎"

    def __init__(self, name, color):
        print('tiger init')

        super(Tiger, self).__init__(name)
        self.color = color

    def eat(self):
        super(Tiger, self).eat()
        print("我还喜欢吃肉")

    def show(self):
        print("{},{}".format(self.name, self.color))


panda = Tiger('yuan zi', 'yellow')
panda.show()
"""


# ######### 类的高级特性property
# 1.@property: 将类的方法当作属性来使用
# 2.__slots__:静态属性列表
# _slots__方法用元组定义允许绑定的属性名称和方法名而不是列表
"""
class BaseCat(object):
    '''
    猫科动物的基础类
    '''
    tag = "猫科动物"

    __slots__ = ('name','__age')
    def __init__(self, name, age):
        print('BaseCat init')
        self.name = name
        self.__age = age

    # 私有属性的获取
    @property
    def age(self):
        return self.__age

    # 私有属性的修改
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            print("不合法")
            return
        if value < 0 or value > 100:
            print("不合法")
            return
        self.__age = value

    @property
    def show_info(self):
        print("{},{}".format(self.name, self.age))

    def __str__(self):
        return "{}".format(self.name)

class Tiger(BaseCat):
    __slots__ = ('color')


small_cat = BaseCat('hua hua', 2)
small_cat.show_info     # hua hua,2

print(small_cat)  # hua hua   __str__

# print(small_cat.get_age)  # 'BaseCat' object has no attribute 'age'

small_cat.age = 6  # 私有属性如何修改，
small_cat.show_info  # hua hua,6

# 使用__slots__后不允许给实例添加新的属性
# small_cat.color = '白色'  # __slots__  AttributeError: 'BaseCat' object has no attribute 'color'

tiger = Tiger('ddd', 5)
# small_cat.color = '白色'      # AttributeError: 'BaseCat' object has no attribute 'color'
tiger.color = '白色'
print(tiger.color)  # 白色    # 白色

"""

# ###########类的静态方法和实例方法

class Cat(object):

    tag = 'cat'

    def __init__(self, name):
        print('BaseCat init')
        self.name = name

    @staticmethod
    def breath():
        print('猫都需要呼吸空气')

    # def show_info(self):
    #     print('类的属性{}，对象的属性{}'.format(self.tag, self.name))
    @classmethod
    def show_info(cls):
        print('类的属性{}，对象的属性{}'.format(cls.tag, cls.name))   # type object 'Cat' has no attribute 'name'


if __name__ == '__main__':
    Cat.breath()

    small_cat = Cat('money')
    small_cat.breath()
    # small_cat.show_info()