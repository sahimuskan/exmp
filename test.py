f=open("python1.txt",'w')
import random
n=10
y=10*n
z=""
x1 = random.randint(n,y)
z=z+str(x1)+"#"
f.write(z)
#f.close()
f=open("python1.txt",'r')
data1=f.read()
print(data1)
f.close()