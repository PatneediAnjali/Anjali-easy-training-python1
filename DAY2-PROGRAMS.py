#get a number as input and find out whether it is 500 or not
n=int(input("enter a number"))
if n==500:
    print("the number is 500")
else:
    print("the number is not 500")

#check given number is "even-positive" or "odd negative" or "Even-negative" or "odd positive"
n=int(input("enter"))
if(n%2==0 and n>0):
    print("the given number is Even-positive")
elif(n%2!=0 and n>0):
    print("the given number is Odd-positive")
elif(n%2==0 and n<0):
    print("the given number is Even-Negative")
elif(n%2!=0 and n<0):
    print("the given number is Odd-negative")
    
#get two numbers as inout and find out biggest number
a,b=int(input("enter first number")),int(input("enter second number"))
if(a>b):
    print(a,"is the biggest number ")
else:
    print(b," is the biggest number ")

#check given number is float or integer
n=10.0
res=n-int(n)
if res>0 or res!=0:
    print("number is float")
else:
    print("number is integer")

#get three numbers as input and print the greatest number
a,b,c=int(input("enter num1")),int(input("enter num2")),int(input("enter num3"))
if(a>b and a>c):
    print("the greatest number is",a)
elif(b>a and b>c):
    print("the biggest number is",b)
else:
    print("the biggest number is",c)


#check given number is divisible by 11 or not
a=int(input("enter"))
if(a%11==0):
    print("the given number is divisible by 11")
else:
    print("the given number is not divisible by 11")

#print all even numbers between 2 to 20
i=2
while i<=20:
    if(i%2==0):
        print(i)
    i=i+1

#number guessing game
import random
n=random.randrange(1,50)
guess = int (input("enter any number:"))
while n!= guess:
    if guess<n:
        print("too low")
        guess=int(input("enter number again:"))
    elif guess > n:
        print("too high")
        guess=int(input("enter number again:"))
    else:
        break
print("you guessed it right")
                  
#weather naming using temparatures
t=int(input("enter"))
if t>45:
    print("Hottest")
elif t>=40 and t<=45:
    print("hot")
elif t>=25 and t<=40:
    print("moderate")
elif t>=10 and t<=25:
    print("cold")
elif t<10:
    print("chill")


   
    


          
