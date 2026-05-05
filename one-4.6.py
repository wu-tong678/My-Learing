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
#lengend图例
'''
l1,=plt.plot(x,y2,label='up')#绘制两条曲线，标签为up
l2,=plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--',label='down')#绘制两条曲线，标签为down
#handles指定要用的线条对象，labels覆盖原有标签名，最后一个选择最佳位置
plt.legend(handles=[l1,l2],labels=['up','down'],loc='best')
plt.show()
'''
#annotation标注
'''
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-3,3,50)
y=2*x+1
plt.figure(num=1,figsize=(8,5),)
plt.plot(x,y,)

ax=plt.gca()
ax.spines['right'].set_color('none')#将右边框显示为透明，
ax.spines['top'].set_color('none')#上边框隐藏
ax.xaxis.set_ticks_position('bottom')#设置x轴刻度线位置在底部
ax.yaxis.set_ticks_position('left')#设置y轴刻度线位置在左侧
#将底部边框移动到y=0位置，
ax.spines['bottom'].set_position(('data',0))
#将左侧边框移动到x=0位置
ax.spines['left'].set_position(('data',0))




x0=1
y0=2*x0+1
plt.scatter(x0,y0,s=50,color='b')
plt.plot([x0,x0],[y0,y0],'k-',lw=2.5)

plt.annotate(r'$2x+1=%s$'%y0,xy=(x0,y0),xycoords='data',xytext=(+30,-30),textcoords='dffset poins',
             fontsize=16,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))


plt.show()
'''

#tick能见度
'''
for label in ax.get_xticklabels()+ax.get_yticklabels():#获取x轴和y轴的所有刻度标签
    label.set_fontsize(12)#将标签字体设置为12号
    label.set_bbox(dict(facecolor='white',edgecolor='none',alpha=0.7))#为标题添加一个背景框，背景色为白，无边框，透明度70%
plt.show()
'''

#scatter散点图
'''
import matplotlib.pyplot as plt
import numpy as np

x=1024                         #点的数量
X=np.random.normal(0,1,x)#生成1024个x个坐标，均值为0，标准差为1
Y=np.random.normal(0,1,x)
T=np.arctan2(X,Y)#计算每个点的方位角，用作颜色值

plt.scatter(X,Y,s=75,c=T,alpha=0.5)#s点的大小，c颜色映射到角度值，0.5半透明效果

plt.xlim((-1.5,1.5))#x轴范围
plt.ylim((-1.5,1.5))

plt.show()
'''

#bar柱状图
'''
import matplotlib.pyplot as plt
import numpy as np

n=12
X=np.arange(n)
#生成12个0.5到1.0之间的随机数
Y1=(1-X/float(n))*np.random.uniform(0.5,1.0,n)
Y2=(1-X/float(n))*np.random.uniform(0.5,1.0,n)
#.bar绘制柱状图，x,y位置，颜色和边框
plt.bar(X,+Y1,facecolor='r',edgecolor='none')
plt.bar(X,-Y2,facecolor='b',edgecolor='none')
#将位置与数值一一对应
for x,y in zip(X,Y1):
    #柱子上写数字，距离自己定，保留两位小数，居中，垂直底部对齐
    plt.text(x+0.4,y+0.05,'%.2f'%y,ha='center',va='bottom')
for x,y in zip(X,Y2):
    #垂直顶部对齐
    plt.text(x+0.4,-y-0.05,'-%.2f'%y,ha='center',va='top')

plt.xlim(-0.5,n)
plt.xticks(())
plt.ylim(-1.25,1.25)
plt.yticks(())

plt.show()
'''

#contours等高线图
'''
import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
    
n=256
x=np.linspace(-3,3,n)
y=np.linspace(-3,3,n)

#生成二维网格矩阵x和y，计算函数值
X,Y=np.meshgrid(x,y)

#绘制填充等高线，8：等高线层级数，0.75：透明度，使用热色调
plt.contourf(X,Y,f(X,Y),8,alpha=0.75,cmap=plt.cm.hot)


#绘制黑色等高线，线宽0.5，
C=plt.contour(X,Y,f(X,Y),8,colors='black',linewidths=.5)

#在等高线C上添加数值标签，标签嵌入线中，字号10
plt.clabel(C,inline=True,fontsize=10)

plt.xticks(())
plt.yticks(())
plt.show()
'''
#image图像
'''
import matplotlib.pyplot as plt
import numpy as np

#定义一个长度为9的一维数据，转成三行三列
a=np.array([1,2,3,
            4,5,6,
            7,8,9]).reshape(3,3)

#imshow将数组a显示为图像，色块样式，bone颜色映射（蓝黑白），图像原点位于左上
plt.imshow(a,interpolation='nearest',cmap='bone',origin='upper')

#添加颜色条，0.9颜色条高度缩短为0.9
plt.colorbar(shrink=0.9)

plt.xticks(())
plt.yticks(())
plt.show()
'''
#3D数据
'''
import numpy as np
import matplotlib.pyplot as plt


fig=plt.figure()#创建图形窗口，函数

#fig（figure类的方法）
ax=fig.add_subplot(111,projection='3d')#在这个图形上添加一个3D坐标轴，

X=np.arange(-4,4,0.25)#x轴范围-4到4，步长0.25,函数
Y=np.arange(-4,4,0.25)
X,Y=np.meshgrid(X,Y)#生成二维网格，函数

R=np.sqrt(X**2+Y**2)#计算平方跟，函数
Z=np.sin(R)#计算正弦值，函数

#plt.get_cmap:函数，获取颜色映射表，ax.plot_surface():Axes3D类方法
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))

#Axes3D类方法
ax.contourf(X,Y,Z,zdir='z',offset=-2,cmap='rainbow')
#Axes3D类方法
ax.set_zlim(-2,2)
plt.show()
'''
#subplot多合显示
'''
import matplotlib.pyplot as plt

plt.figure()

plt.subplot(2,1,1)#创建坐标轴，位置二行一列第一个位置
plt.plot([0,1],[0,1])#将点连成线

plt.subplot(2,3,4)#二行三列第四个位置
plt.plot([0,1],[0,2])

plt.subplot(235)#简化版二行三列第五个位置
plt.plot([0,1],[0,3])

plt.subplot(236)
plt.plot([0,1],[0,4])

plt.show()
'''
#subplot分格显示
'''
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.figure()
#3*3虚拟网格，位置是0行0列，横向跨三列，纵向占一行
ax1=plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=1)
#在ax1上面画条线，x:1,2 y:1,2
ax1.plot([1,2],[1,2])
#ax1设置标题
ax1.set_title('ax1')

plt.show()

'''
#图中图
'''
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

#figure函数返回一个fig实例对象
fig=plt.figure()
x=[1,2,3,4,5,6,7]
y=[1,2,3,4,5,6,7]

left,bottom,width,height=0.1,0.1,0.8,0.8#左下宽高
#fig的一个子类对象
ax1=fig.add_axes([left,bottom,width,height])

ax1.plot(x,y,'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('ax1')

left,bottom,width,height=0.2,0.6,0.25,0.25
ax2=fig.add_axes([left,bottom,width,height])
ax2.plot(x,y,'r')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('ax1')

plt.axes([0.6,0.2,0.25,0.25])
plt.plot(y,x,'g')
plt.xlabel('x')
plt.ylabel('y')
plt.title('ax2')

plt.show()

'''
#次坐标轴
'''
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,10,0.1)
y1=0.05*x**2
y2=-1*y1

fig,ax1=plt.subplots()#返回一个画布，包含子图
ax2=ax1.twinx()#还是figure的实例对象，另一子图，与ax1平级，twinx共享x轴
ax1.plot(x,y1,'g-')
ax2.plot(x,y2,'b--')

ax1.set_xlabel('x')
ax1.set_ylabel('y1')
ax2.set_ylabel('y2')

plt.show()
'''

