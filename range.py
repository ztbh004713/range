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
print(type(i))
#搭配使用字串及 , ：明确印下，使用次数及当下产生的随机数字。