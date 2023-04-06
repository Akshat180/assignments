#que 1

num = int(input("enter a number "))
l=num%10
print(l)

#que 2

l={95,52,-410,57,55,10,-81,740,81}
for n in l:
    if(n%5==0):
        print(n )

#que 3

s = (input("enter str "))        
print(len(s))

#que 4

num = int(input("enter a number "))

if(num%2==0):
    print("even")
else:
    print("odd")    

#shortand notation 
'''
print('even')if num%2==0 else print('odd')

print('even')if int(input("enter a number"))%2==0 else print('odd')

#for shortand notation else is must 

'''

#que 5

str= input("enter a string ")
x=str[::-1]  # this is call reverse sclising
print(x)

# other way to do
'''
str=input('ent')
str1=""
for i str:
    str1= i + str1   #in this position of i matters

print(str1)

'''

#que 6

n=(input("number:"))

x=int(n[-3])
if(x%7==0):
    print("y")

else:
    print("n")    

#que 7
i=input(" enter ")    
x=i[::2]
print(x)

#other way to do
'''
str=input("enter")
  
for i in range(1,len(string),2):
print(string[i]),end = ""      end="" = \n it mean we have to start from new line

 

'''


#que 8

l=[28,45,12,978,254,28]
if l[0]==l[-1]:
     print("same")
else: print("not same")    

# to show indexing in list we can do 
# examole l=[12,555,4,6,5,8,4][-1]
#this will print -1 place 
#print(l)

#que 9

x= int(input("enter your salary "))
tax = 0

if x<250000:
     print("no tax ")
elif(x>250000 and x<500000):
     t=50000
     print(t)
elif(x>500000 and x < 1000000):
     t= 10000
     print(t)          

#que 10

s=input("string ")
x='aeiou'
if s[0].lower() in x :
    print("yes")
else :
    print("no")

#que 11
s=input("string ")

x='aeiou'

for i in s.lower():

        if i in x :
                print("all character are  vovwels")
                break

else:
     print("all character are not vovwels")       
#que 12
m=int(input("maths "))
sst=int(input("sst "))
sci=int(input("science "))
h=int(input("hindi "))
e=int(input("english "))

t=m+sst+sci+h+e
x=t/5
print(x)


#que 13
i='95.3'
print(float(i))

#que 14

num=(input("num "))
i=str(num)
count=i.count("0")
print(count)

#other way to do

'''
num = input("enter a number ")

count=0

for i in num:
    if i == "1":   # here we enter that value which we count of 
        count += 1

         
print(count)
    

'''

#que 15
h=int(input("hight "))
b=int(input("base "))

area= 0.5*b*h
print(float(area))
#que 16

day = { 1:'mon',2:'tue',3:'wed',4:'thr',5:'fri',6:'sat',7:'sun'}

x=int(input("enter a num "))

print(day[x])

#que 17

age=int(input("age "))

if age>=18:
    print("can vote")

elif age<18:
    print("can not vote ")

else:
    print("none")    
#que 18
n = int(input("Enter the number of values you want to add: ")) # this is for how many number you want that will add 
total = 0

for i in range(n):
    num = int(input("enter a number")) # this input is for number we want to add
    total += num

print("The sum of the numbers is:", total)

#que 19
s = int(input("enter a starting num "))
e = int(input(" enter the ending num "))


for s in range (s,e+1):
    if s%2==0:
        print(s**2)


# other way to do in list form 
'''
s = int(input("enter a starting num "))
e = int(input(" enter the ending num "))

l=[]
for i in range (s,e+1):
    if i%2==0:
        l.append(i**2)  

print(l)     

'''        


#que 20

n=int(input(" enter a number"))
sum=0
for i in range(1,n+1):
     sum = sum+i

print(sum)   
 