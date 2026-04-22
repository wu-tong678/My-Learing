#各个库的安装以及验证
#import matplotlib.pyplot as plt
#plt.plot([1,2,3])
#plt.show()

#numpy的属性
'''import numpy as np
array=np.array([[1,2,3],
               [4,5,6]])
print(array)#打出矩阵
print('number of dim:',array.ndim)#几维数组
print('shape',array.shape)#几行几列
print('size',array.size)#总共多少元素
'''
#numpy创建array
'''
import numpy as np
a=np.array([1,2,3],dtype=np.int64)#dtype来改变数组类型
print(a)

b=np.array([1,2,3],
           [4,5,6])#两行三列的矩阵
print(b)

import numpy as np
c=np.zeros((3,4))#打造三行四列的全是0的矩阵
d=np.ones((3,4),dtype=np.int64)#全是1，并且将数组定为整数
e=np.empty((3,4))#生成接近于0的数字
print(e)
'''
'''
import numpy as np
#a=np.arange(0,12,1).reshape((3,4))#arange与range一样，reshape来决定几行几列
#print(a)
b=np.linspace(1,10,5)             #从1开始到10结束，步长为5（随机分配）
print(b)
'''
#numpy的基础运算
'''
import numpy as np
a=np.array([10,20,30,40])
b=np.arange(4)
c=a-b
d=a+b
e=b**2
f=10*np.sin(a)#三角函数值的运算
print(a,b)
print(c,d)
print(e)
print(f)
print(b<3)#输出b里小于3的
'''
'''
import numpy as np
a=np.array([[1,0],
           [1,2]])
b=np.arange(4).reshape((2,2))
c=a*b        #矩阵对应相乘
d=np.dot(a,b)#或者a.dot(b),矩阵计算方法
print(a,b)
print(c,d)
'''
'''
import numpy as np
a=np.random.random((3,4))#随机生成三行四列
print(a)
print(np.sum(a,axis=1))#每一行总和
print(np.max(a,axis=0))#每一列最大
print(np.min(a,axis=1))#每一行最小
'''
#numpy基础运算2
'''
import numpy as np
a=np.arange(2,14).reshape((3,4))
print(a)
print(np.argmin(a))     #最小值的索引
print(np.argmax(a))     #最大值的索引
print(np.mean(a))       #平均值（a.mean()）
print(np.average(a))    #平均值
print(np.median(a))     #中位数
print(np.cumsum(a))     #累加方法，第二个数等于前两个数的和，第三个等于前三个和，以此类推
print(np.diff(a))       #累差，第二位等于原本第二位减去第一位的值
print(np.nonzero(a))    #输出非0的数
print(np.sort(a))       #排序
print(np.transpose(a))  #矩阵的反向，行变列，列边行
print(np.clip(a,5,9))   #小于5全是5，大于9全是9，其余不变
print(np.mean(a,axis=0)) #求列平均值，行也是一样
'''
#numpy的索引
'''
import numpy as np
a=np.array([[1,2,3],
           [4,5,6]])
print(a)

print(a[1][1])#第二行第二个
print(a[1,:])#第二行的所有数，直接用冒号代替
print(a[:,1])#第二列的所有数，直接用冒号代替
print(a[1,0:1])#第二行第一列第二位数之前（不包括第二位数）
for row in a.flatten():#迭代出一个一个的项目
    print(row)
'''
#numpy的合并
'''
import numpy as np
a=np.array([1,2,3])[:,np.newaxis]#也可以直接加在后面
b=np.array([4,5,6])[:,np.newaxis]

c=np.vstack((a,b))#列项合并
d=np.hstack((a,b))#横向合并
print(c)
print(d)
print(c.shape,d.shape)
print(a[:,np.newaxis])#将a变为列项

C=np.concatenate((a,b,b,a),axis=1)#多项合并，横向合并，纵向是0
print(C)
'''
#numpy的分割
'''
import numpy as np
a=np.arange(12).reshape((3,4))
print(a)
print(np.split(a,2,axis=1))#等量横向分割，分成两块
print(np.array_split(a,3,axis=1))#不等量分割
print(np.vsplit(a,3))#横向分成三块
print(np.hsplit(a,2))#纵向分成两块
'''
#import的copy
'''
import numpy as np
a=np.array([1,2,3])
b=a

b=a.copy()#b不在受a改变而改变
print(b)
a[2]=5
print(b)#两次结果一样
'''


#numpy的小练习
'''
import numpy as np
#随机生成五名学生的三门成绩，成绩范围为60-100
a=np.random.randint(60,101,(5,3))
print("查看五名学生各自三门成绩的内容：",a)
#计算学生成绩的总分
b=np.sum(a,axis=1)
#计算每门科目的平均分
c=np.mean(a,axis=0)
#找出最高分
d=np.max(a)
#找出哪名学生总分成绩最高
e=np.argmax(b)
print(b)
print(c)
print(d)
print(e)

import numpy as np
def covert_grade(score):
    if score>=90:
        return"A"
    elif score>=80:
        return"B"
    elif score>=70:
        return"C"
    elif score>=60:
        return"D"
    else:
        return"F"
grade=np.vectorize(covert_grade)#使其函数能处理整个数组
'''
#pandas基本介绍
'''
import pandas as pd
import numpy as np
#一维数据结构，创建一列数据
s=pd.Series([1,3,6,np.nan,41])


dates=pd.date_range('20160101',periods=6)#函数，生成日期范围

#创建随机六行四列数据，行是datas输出的，列是abcd
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])

#生成三行四列数据，二维数据结构
df1=pd.DataFrame(np.arange(12).reshape((3,4)))

df2=pd.DataFrame({'a':[1],'b':[2],'c':[3],'d':[4]})

print(df2.dtypes)#查看df2每一列的数据类型
print(df2.index)#输出行索引
print(df2.columns)#输出列的名字
print(df2.values)#获取数据值
print(df2.describe())#生成统计摘要（计数，均值，标准差，最值等）
print(df2.T)#行列颠倒
print(df2.sort_index(axis=1,ascending=False))#进行倒序排序
print(df2.sort_values(by='c'))#针对某一列进行排序
'''
#pandas的选择数据
'''
import numpy as np
import pandas as pd
dates=pd.date_range('20130101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['a','b','c','d'])

#print(df['a'],df.a)#两个功能一样，获取a列数据
#print(df[0:3],df['20130101':'20130103'])#前两个功能一样，获取前三行数据

#print(df.loc['20130102'])#输出这一行数据
#print(df.loc['20130102',['a','b']])#输出这一行啊a,b列数据

#print(df.iloc[3,1])#第三行第一位
#print(df.iloc[3:5,1:3])#第四行到第五行，第二列到第三列
#print(df.iloc[[1,3,5],1:3])#1,3,5具体到行

#print(df[df.a<8])#筛选出列a的值小于8的所有行
'''
#pandas设置值
'''
import numpy as np
import pandas as pd
dates=pd.date_range("20130101",periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['a','b','c','d'])
df.iloc[2,2]=1111#改变第三行第三列
df.loc['20130101','b']=222#改变这行这列
df[df.a>4]=0#a这一列中大于4这一行之前不变，大于的这一行全为0
df.a[df.a>4]=0#a这一列大于4的为0
df['f']=np.nan#增加f这一列，元素是nan

print(df)
'''
#pandas处理丢失数据
'''
import numpy as np
import pandas as pd
dates=pd.date_range("20130101",periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['a','b','c','d'])
df.iloc[0,1]=np.nan
df.iloc[1,2]=np.nan
print(df)
#print(df.dropna(axis=1,how='any'))#0：丢掉nan所在行 1：丢掉nan所在列
print(df.fillna(value=0))#给nan赋值0
print(df.isnull())#缺失数据处为true
print(np.any(df.isnull())==True)#丢失数据显示True
'''
#pandas导入导出
'''
import pandas as pd
date=pd.read_csv('data.csv')#读取csv文件
print(date)
date.to_pickle('data.pkl')#将date保存为pickle格式文件
'''
#pandas合并concat




#matplotlib基本用法已经figure用法
'''
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3,3,50)#横坐标-3到3,50个点
y1=2*x+1
y2=x**2

#可不写figure
plt.figure()#分别生成figure1和figure2
plt.plot(x,y1)

plt.figure(num=3,figsize=(10,5))#可以改成figure3，长宽为10,5
plt.plot(x,y2)#两条线在一个figure里
plt.plot(x,y1,color='red',linewidth=10.0,linestyle='--')#曲线为红色，宽度为10，样子为虚线

plt.show()
'''
#设置坐标轴
'''

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2



plt.figure()
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=10.0,linestyle='--')


plt.xlim((-1,2))#x坐标轴范围
plt.ylim((-2,3))#y
plt.xlabel('abc')#x坐标轴名字
plt.ylabel('efg')#y

new_ticks=np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)#x范围
plt.yticks([-2,-1.8,1],['s','n','m'])#y轴特定值所指字母

#设置坐标轴2
ax=plt.gca()
ax.spines['right'].set_color('none')#将右边框显示为透明，
ax.spines['top'].set_color('none')#上边框隐藏
ax.xaxis.set_ticks_position('bottom')#设置x轴刻度线位置在底部
ax.yaxis.set_ticks_position('left')#设置y轴刻度线位置在左侧
#将底部边框移动到y=0位置，
ax.spines['bottom'].set_position(('data',0))
#将左侧边框移动到x=0位置
ax.spines['left'].set_position(('data',0))
plt.show()
'''