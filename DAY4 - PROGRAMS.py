#CALCULATING PRODUCT PRICE FOR 5 UNITS
old={'rice':60,'dhaal':120,'oil':150}
new={product:price*5 for (product,price)in old.items()}
print(new)

#WITH CHECKS
real={'sam':24,'angel':18,'kumar':35}
now={name:age for (name,age) in real.items()
     if age>20}
print(now)

#create a list with 8 customer names display a dictionary which has customers names along with discounts for them from a particular shop
import random
cust=['a','b','c','d','e','f','g','h']
cust_dict={names:random.randint(1,100) for names in cust}
print(cust_dict)

#how to take keys and values from diff iterables
import random
student_names=list(map(str,input("enter names:").split()))
marks=[]
for i in range(len(student_names)):
    a=(random.randint(300,500) / 500)*100
    marks.append(a)
my_dict={x:y for(x,y) in zip(student_names,marks)}
print(my_dict)



#STRINGS
s="anjali"
s.upper()
'ANJALI'
s.lower()
'anjali'
s.casefold()
'anjali'
s.capitalize()
'Anjali'
s.replace('h','a')
'anjali'
s.replace('a','h')
'hnjhli'
s.strip()
'anjali'
s="  anj  al i "
s.strip()
'anj  al i'
s.split()
['anj', 'al', 'i']
s="anjali"
s.split()
['anjali']
s.split('.')
['anjali']
s="an.,ja li"
s.split('.')
['an', ',ja li']

s.count('a')
2

#1.get one string as input along with a character find out and display whether that particular character is present or not
#2.check whether the given string is palindrome or not
#3. after getting one string as input check your string contains spaces or not if yes print number of spaces in it
#4.create a list with vowels get one string as input .count vowels from the string and print it 

#character prsent or not
s=input("enter")
ch=input("enter")
if ch in s:
    print("present")
else:
    print("not present")
#character present or not using iteration logic
s=input("enter")
ch=input()
for i in s:
    if i==ch:
        flag=1
        break
    else:
        flag=0
if flag==1:
    print("present")
else:
    print("Not present")
#character present or not 
st=input("enter the string:")
char=input("enter req char:")
a="yes" if char in st else no
print(a)

#spaces in list
s=input("enter")
n=0
for i in s:
    if i==" ":
        n=n+1
print(n)
if(n>0):
    print(n)
else:
    print("no spaces") 

#spaces in string method2
L=['a','e','i','o','u']
st=input("enter a string")
count=0
for i in st:
    if i in L:
        count=count+1
print(count) 

#MATH MODULE
import math
print( "CEIL 12.5:", math.ceil(12.5))
print(" FLOOR 12.5:",math.floor(12.5))
print("SQRT 345 :",math.sqrt(345))
print("FACTORIAL 3:",math.factorial(3))
print("power 2,3 :",math.pow(2,3))
print("REMINDER 10,3:",math.fmod(10,3))

a,b=divmod(10,3)
print(a,b)




