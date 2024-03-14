
Q1
"""

length=float(input("Enter the lenght of the rectangle"))
width=float(input("Enter the width of the rectangle"))
area=length*width
print("Area of the rectangle is ",area)

"""Q2"""

weight=float(input("Enter your weight in kg"))
height=int(input("Enter your height in cm"))

height_m=height/100
bmi=weight/(pow(height_m,2))
print("Your BMI is ",bmi)

"""Q3"""

student_details={}
n=int(input("Enter number of student"))
for i in range(0,n):
  name=input("Enter students name ")
  score=int(input("Enter score of the student"))
  student_details[name]=score
print(student_details)

"""Q4"""

age=int(input("Enter your age "))
if age<18:
  print("Minor")
elif age<50:
  print("Adult")
else:
  print("Senior")

"""Q5"""

for i in range(0,51):
  if i%2==0:
    print(i," ")

"""Q6"""

user_login={}
user_name=input("ENter your user name")
password=input("Enter your password")
user_login[user_name]=password

user_name2=input("ENter your username that you want to login with")
password2=input("Enter your password")
while password2 != user_login[user_name2]:
  password2=input("Enter your password")

print("Login Successful")

"""Q7"""

def average(list1,n):
  sum=0
  for i in list1:
    sum+=i
  a=float(sum/n)
  print("Average is ",a)


list1=[]
n=int(input("Enter number of elements"))
for i in range(0,n):
  x=int(input("ENter number"))
  list1.append(x)
average(list1,n)

"""Q8"""

str=input("Enter string")
count=0
for i in str:
  if i=='a'or i=='e' or i=='i' or i=='o' or i=='u' or i=='A'or i=='E' or i=='I' or i=='O' or i=='U':
    count+=1

print("Total vowels are= ", count)

"""Q9"""

from datetime import datetime as dt
print("Current date time is ",dt.now())

"""Q10"""

def addition(a,b):
  try:
    for i in a:
      if i == '0' or i == '1' or i == '2'or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
        continue
      else:
        raise Exception(print("Invalid argument"))
  except Exception as e:
    print("Error",e)
    return
  try:
    for i in b:
      if i == '0' or i == '1' or i == '2'or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
        continue
      else:
        raise Exception(print("Invalid argument"))
  except Exception as e:
    print("Error",print("Invalid argument"))
    return
  return "No error"
one=input("Enter number 1")
two=input("Enter number 2")
addition(one,two)

"""Q11"""

x=int(input("Enter number"))
try:
  if x>100:
    raise ValueError("Number cannot be greater than 100")
except ValueError as ve:
  print("Error",ve)

"""Q12"""

numerator=int(input("Enter Numerator"))
denominator=int(input("Enter denominator"))
try:
    result = numerator/denominator
    print(result)
except:
    print("Error: Denominator cannot be 0.")

"""Q13"""

f2=open("file1.txt",'w')
f2.write("Hello! python")

"""Q14"""

f3=open("file1.txt",'r')
f3.read()

"""Q15"""

f4=open("file1.txt",'a')
f4.write("Hello again")

f5=open("file1.txt",'r')
f5.read()