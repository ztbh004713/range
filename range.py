#range 范围
#python内建功能：清单产生器

range(5) #[0, 1, 2, 3, 4] 
range(3) #[0, 1, 2]       

for c in range(3):        
	print(c)
#通常在使用rahge（）都是与for回圈搭配，『很少有单独写range（）的情况』
for i in range(5):  #通常只是为了拿来重复执行固定次数
	print("why")    #撰写的range(5) 则是[0 ,1 ,2 ,3 ,4] 在搭配print("内容自定义")，则会依照设立的条件印下多少次
import random                    #先前影片教学的载入 random模组
for i in range(50):              #for回圈中 range设定回圈次数
	c = random.randint(1, 5000)  #randint(1 , 5000) 产生随机数的范围 （起始值，结束值）在产生随机的过程中包含起始及结束值。 
	print("这是第" , i + 1 , "次产生的随机数字" , c ,".")

#range 最后的延伸
#ragne(结尾值)
#ragne(开始值，结尾值)
#ragne(开始值，结尾值，递增值) or ragne(开始值，结尾值，递减值)
range(2 , 8)   #[2,3,4,5,6,7] 在撰写时，开始值是有包含在其中，而结束值没有
range(11 , 16) #同理可证[11,12,13,14,15]
for n in range(11 , 16):
	print(n)
print("--------------------")
range(2, 10, 3) #[2, 5, 8]  range()中的第三个数，为递增值(step)，从开始值2依序+3往上增加，但不超过结束值
range(3, 20, 4) #[3,7,11,15,19]
for m in range(3, 20, 4):
	print(m)
print("--------------------")
range(10, 3, -2) #[10,8,6,4] 反向撰写时，开始值依序递减-2，递减后不得低于结束值。
for a in range(20, 4, -3):
	print(a)