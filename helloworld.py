print ("hello world")
print ("The quick brown fox","jump over","the lazy dog.")

# print absolute value of an integer:
a = -10
if a > 0:
    print (a)
else:
    print (-a)

a = 10e2
print (a)

b = 1.2e-2
print (b)

print ('I\'m \"OK\"!')
print ('I\'m OK')
print ('\\\t\\')
print ('\\t\\')

print ('''line1,
line2
line3''')

print (True and True)
print (True and False)
print (False and False)
print ("")
print (True or True)
print (True or False)
print (False or False)
print ("")
print (not True)
print (not False)

# out age judgment
age = 25
if age >=18:
    print ('adult')
else:
    print ('teenager')

Answer = True
print (Answer)
Answer = False
print (Answer)

x = 10
print (x)
x = x + 2
print (x)

a = 'ABC'
b = a
print (b)
a = 'XYZ' #后续赋值不影响
print (b)

# /represent floting number division
print (10/3)
print (9/3)

# //represent integer division
print (10//3)

# % represent remainder 余数除
print (10%3)

# show integer codes of strings 字符串的整数表示
print (ord ('A'))
print (ord ('a'))
print (ord('中'))

# show the value of integer codes 转换编码为对应字符
print (chr(12)) # no value assigned from 0 to 11?
print (chr(66))

# 十六进制表示
print ('\u4e2d\u6587')

# 字符串默认为str (string), 变成以字节为单位存储为bytes
x = 'ABC'
y = b'ABC'
print (x)
print (y)

# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
# 'ABC'encode('ascii') cmd结果全部带前缀b，显示数据类型为bytes
# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
'ABC'.encode('ascii')
'中文'.encode('utf-8')
# 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
b'ABC'.decode('ascii')
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8') # cmd结果显示'中文'
b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore') # cmd结果显示'中'

# 要计算str包含多少个字符，可以用len()函数
len ('ABC') # cmd结果为3
len ('中文') # cmd结果为2

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
len (b'ABC') # cmd结果为3
len (b'\xe4\xb8\xad\xe6\x96\x87') # cmd结果为6
len ('中文'.encode('utf-8')) # 先转换为utf-8编码的bytes,6个字节数
# 可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节

# 占位符的使用 %d 整数； %f 浮点数； %s 字符串； %x 十六进制整数
print ('hello, %s' % 'world')
print ('hello, %s' % ('AB'))
print ('Hi, %s, you have $%d.' % ('Michael', 10000))

# 转义： %%表示一个%
print ('growth rate: %d %%' %7)
print ('growth rate: %f%%' %7.2)

# format()占位符
print ('Hello, {0}, 成绩提高了 {1}%'.format('小明',17.125)) #17.125为字符串
print ('Hello, {0}, 成绩提高了 {1:1f}%'.format('小明',17.125)) #17.125为浮点数

s1=72
s2=85
s3=(s2-s1)/s1*100
print ('小明的成绩提高了%f%%' %s3)
print ('小明的成绩提高了%.2f%%' %s3)

print('%s成绩提升的百分比是：%.1f%%' %('小明',s3))
print('%s成绩提升的百分比是：%.2f%%' %('小明',s3))
print('%s成绩提升的百分比是：%.3f%%' %('小明',s3))

print ('{0}的成绩提高了{1}%'.format('小明',s3))
print ('{0}的成绩提高了{1:1f}%'.format('小明',s3)) #1f,2f语法无法在format形式的占位符中使用？

# List: 有序的可变集合，可以随时添加和删除其中的元素
classmates = ['Bob','Michael','Tracy']
print (len (classmates)) # 获取list的个数
print (classmates [0])
print (classmates [1])
print (classmates [-1]) # 获取list中倒数第一个元素
print (classmates [-2]) # 获取list中倒数第二个元素

# 向list中追加元素
classmates.append('Adam') # 默认追加到list末尾
print (classmates)
classmates.insert(0,'AB') # 追加到指定位置
print (classmates)

# 在list中删除元素
classmates.pop() # 删除队末的元素
print (classmates)
classmates.pop(0) # 删除指定位置的元素
print (classmates)

# 替换list中的元素
classmates[2] = 'Sarah' # 直接替换指定位置
print (classmates)

# list中可以是不同数据类型的元素，甚至是另一个list，注意该处的True是布尔值
list1 = ['123','AB',classmates,True]
print (list1)
print (len(list1)) # 元素的个数，其中包含的list为一个元素
classmates.append('Tracy')
print (list1)

# 空数组
list2 = []
print (len(list2))

# 可变的有序集合 list []，不可变的有序集合tuple () "元组" 一旦初始化后即不可更改其中元素，更加安全
classmates2 = ('Bob','Michael','Tracy')
print (classmates2)

# 括号可以表示负号，如果要定义只包含1的tuple，必须加逗号以消除歧义
t1 = (1)
print (t1)
t2 = (1,)
print (t2)

# "可变的tuple"：包含一个list的tuple
classmates3 = ('AB',classmates)
print (classmates3)
classmates3[1][0] = 'Tom' # 更改Tuple的第二个元素(一个list)中的第一个元素
print (classmates3)

# 条件判断
age = 20
if age >= 18:
    print ('Adult')

age = 16
if age >= 18:
    print ('Adult')
else:
    print ("Adolescent")

# elif (else if) 多重条件判断
age = 8
if age >= 18:
    print ('Adult')
elif age >= 8:
    print ('Teenager')
else:
    print ('Kid')

