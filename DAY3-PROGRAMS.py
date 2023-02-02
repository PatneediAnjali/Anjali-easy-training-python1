#list operations
L=[1,4,7.4,"sam"]
L
[1, 4, 7.4, 'sam']
L[3]
'sam'
L[2:3]
[7.4]
L[2:4]
[7.4, 'sam']
L[0:]
[1, 4, 7.4, 'sam']
L[:3]
[1, 4, 7.4]
L[-1]
'sam'
L[::-1]
['sam', 7.4, 4, 1]
L[::-2]
['sam', 4]
L[::3]
[1, 'sam']
l=[1,4,1,1,6,4,1,2]
len(l)
8
l.count(1)
4
l.append(400)
l
[1, 4, 1, 1, 6, 4, 1, 2, 400]
l.extend([100,200,300])
l
[1, 4, 1, 1, 6, 4, 1, 2, 400, 100, 200, 300]
l.remove(1)
l
[4, 1, 1, 6, 4, 1, 2, 400, 100, 200, 300]
l.pop(-2)
200
l.pop(9)
300
l.pop(8)
100
l
[4, 1, 1, 6, 4, 1, 2, 400]
l.sort()
l
[1, 1, 1, 2, 4, 4, 6, 400]
l.reverse()
l
[400, 6, 4, 4, 2, 1, 1, 1]
a=[1,2,3,4]



a=[1,2,3,4]
for k in range(len(a)):
    print(a[k]) 
 #using membership opertor
a=[1,2,3,4,5,6,7,8,9,10]
for  j in a:
    print(j)

#sum and avg of a list 
b=[1.3,3.4,3.4,3.5,5.6]
sum=0
for i in range(len(b)):
    sum=sum+b[i]
    avg=sum/len(b)
print(sum,avg) 

#append function
size=int(input("size:"))
L=[]
for i in range(size):
    ele=int(input("element"))
    L.append(ele)
print(L)

for i in L:
    if(i%2==0):
        print(i)

#comprehending a list    
numbers=[elements for elements in "Good Afternoon"]
print(numbers)

#can create list using existing list
L=["hyd","vizag","chennai","vijayawada"]
city=[]
for n in L:
    if "v" in n:
        city.append(n)
print(city)

L1=[2**x for x in range(2,10)]
print(L1)

L2=[for a in range(100,201,20)]
print(L2)

L3=[1,2,3,4,5,6]
L4=[i for i in L3 if(i<5)]
print(L4)

#print product of num in list if it is less than 750 or else print its sum
n=list(map(int,input("enter").split()))
print(n)
x=1
y=0
for i in n:
    x=x*i
    y=y+i
if(x<=750):
    print("product",x)
else:
    print("sum",y)


