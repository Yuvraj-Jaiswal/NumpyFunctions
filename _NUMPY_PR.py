import numpy as np

#common function of numpy
y = np.arange(0,10)#act like range function
y = np.zeros(10)#return matrix or array of 0s
y = np.zeros((4,4) ,dtype=int)#you can also pass shape in tupple
y = np.ones((4,4))#return matrix of ones
y = np.linspace(0,10,5)#return linearly spaced "n" points between range
y = np.eye(5)#return matrix which have 1s in diagonal or eyedentiy matrix


#Random data generation function of numpy
y = np.random.rand(20)#return number of random number between 0-1
y = np.random.rand(2,5)#you can also pass shape (it will return uniform distribution of no.)
y = np.random.randn(3,4)#return no. which are centered on 0 of variance 1
y = np.random.randint(0,10,10)#take low and high value and return n number of value b/w low and high
y = np.random.randint(0,100,(3,4))#size is optional and we can pass shape in size for matrix
np.random.seed(42)#generate same random no if seed is same # diffrent seed give diffrent value
y = np.random.randint(0,100,(3,4))#testing seed value and it worked #same seed return same random value

#Dot Functions
y = np.random.rand(10)#Test Dot function
y.shape#return shape(row,coloumn) value of y
y = y.reshape(5,2)#reshape np array in given row , colomn manner  -- row*colomn should be == array len
# print(y)#printing reshaped value
y = np.random.rand(10)

#------#
y.max()#Return maximum 'VALUE' in array
y.argmax()#Return 'INDEX' of maximum value in array
#------#
y.min()#Return minimum 'VALUE' in array
y.argmin()#Return 'INDEX' of minimum value in array

#$$$$$#
y.dtype#Retun datatpe of array "int" - "str" or other
#$$$$$#