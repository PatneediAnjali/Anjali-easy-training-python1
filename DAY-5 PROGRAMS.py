import random as r
x="i love sweets"
print(r.sample(x,2))

#EVERYTIME IT GIVESDIFF OUTPUT
a=[1,2,3,4,5,6]
r.shuffle(a)
print(a)

''' a=[1,2,3,4,5,6]
print(r.choice(a))

b="welcome back"
print(r.choice(b))

a=r.random()
print(r.choices(b))

a=r.random()
print(a)
#will return random numbers between 0.0 to 1.0
#0.0 includes 1.0 excludes
print(r.randint(20,30))
a=[10,20,30,40,50]
print(r.choices(a,k=10)) #try with big number and other than k

s="hello good day"
print(r.choices(s,k=3))

print(r.uniform(5,10))
#returns any random number
#between the range includes the
#range values
#float values

#to find all the functions available in particular modulekxz
z=dir(r)
print(z)  '''

'''#DISPLAY WHOLE YEAR CALENDAR
import calendar
print("Full calendar")
print(calendar.calendar(2022))

print("particukar month ")
print(calendar.month(2021,3))
import calendar
print("set first day of the week ")
calendar.setfirstweekday(calendar.FRIDAY)
print(calendar.month(2022,12))'''

'''#prg - display date time

import datetime
a=datetime.datetime.now()
print(a)
sv=a.strftime("%y") #lower case
fv=a.strftime("%Y") #upper case
print("year short version",sv)
print("year full vesion",fv)  '''


'''def sample(): #def or des
    print("great day")
    print("happy time")

sample() #call
print("today")
sample()  '''

''' #multiplication using functions
def multi():
    n1=int(input("number"))#without arg without return value
    n2=int(input("number"))
    n3=int(input("number"))
    prod=n1*n2*n3
    print(prod)
multi()

#multiplication using functions
def multi():
    n1=int(input("number"))#without arg with return value
    n2=int(input("number"))
    n3=int(input("number"))
    prod=n1*n2*n3
    return prod
res=multi()
print(res)

#multiplication using functions
def multi():
    prod=n1*n2*n3       #with arg without return value 
    print(prod)         #static input
multi(3,4,5)

def multi(a,b,c):
    prod=a*b*c
    print(prod)
n1=int(input("number"))    #with arg without return value
n2=int(input("number"))    #dynamic input
n3=int(input("number"))
multi(n1,n2,n3)

#with argument with return value
#static input
def multi():
    prod=n1*n2*n3       
    print(prod)
res=multi(3,4,5)
print(res)

#user input
def multi(a,b,c):
    prod=a*b*c
    return prod
n1=int(input("number"))    
n2=int(input("number"))    
n3=int(input("number"))
res1=multi1(n1,n2,n3)
print(res1)  '''

#1lemons program using functions type1
#2find factors of the given number using functions type2
#3print multiplication table of the given number using functions type3
#4find out sum of digits of the given number using functions type4

'''n=int(input("enter "))
def factor():             #2 not correct
    for i in range(100):
        if(n%i==0):
            return i
res=factor()
print(res)'''

'''#3 multiplication
for i in range(1,11):   
    print(n,"X",i,"=",i*n)
#3 multiplication        
def multi_table(n):                     
for i in range(1,11):   
    print(n,"X",i,"=",i*n)
n=int(input("which table?")
      multi_table(n) '''

'''#2factors of given number
n=int(input("number?"))
for i in range(1,n+1):
      if(n%i==0):
         print(i) '''
        
'''#sum of digits
def digits(n):                       #n=321
      sum=0                          rem=321%10-----------1
      while n!=0:                     0+1----sum ----1
            rem=n%10                  n=321//10 -------32
            sum=sum+rem               rem=32%10 -----------2
            n=n//10
      return sum
n=int(input("enter the number"))
res=digits(n)
print(res) '''

#Recursion
def display():
       n=int(input("enter a number"))
       if(n==1):
             display()
       else:
             print("over")
display()


#recrsive function
def fact(n):
      if n==0:                  # 4!
            return 1            #4*fact(3)
      return n*fact(n-1)        #4*3 i.e 12*fact(2)
result=fact(5)                  #4*3*2 i.e 24*fact(1)
print(result)                   #4*3*2*1*fact(0) ------24


#fibinocci series
n=int(input"enter number"))        57
a=0
b=1
sum=0
count=1
while(count<=n):
      print(sum,end=" ")
      count+=1
      a=b
      b=sum
      sum=a+b
      
#Function returns more values
#addition and subtraction of two numbers in one function
def add_sub(x,y):
       sub=x-y
       add=x+y
       return sub,add
res1,res2=add_sub(20,10)
print(res1)
print(res2)

#varaiable length method
def summ(*a):
       c=0
       for i in a:
              c=c+i
              print(c)
       summ(10,2,3,1,2)




















      
      
