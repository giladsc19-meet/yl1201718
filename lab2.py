import turtle
# lis = [1,2,3,4,5]
# def newlis ():
# 	newlis = [lis[0],lis[-1]]
# 	print (newlis)
# newlis()
a = [1,1,2,3,5,8,13,21,34,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12]
c = []
def less5 (a):
	for i in a:
		if (i==5):
			c.append(i)			
less5(a)
print (c)
