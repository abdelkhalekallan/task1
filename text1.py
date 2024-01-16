################################1
print("hallo\n" *5)
################################2
#For Loop 
fruits = ["orange","lemon", "watermelon"]
x = 0 
for fruits in fruits:
    x +=1
    print(fruits)
print(fruits + " has " + str(x) +" letters")
###############################3
name = input("what is your name ?")
x = 0 
for letter in name:
    x += 1
print(name + " has "+str(x)+" letters")
#################################4
x = 0
print(x)
x += 1
print(x)
###################################5
for x in range(0,10,2): 
    print("hallo "+str(x))
name = "mohammad"
for x in name: # or letter
    print(x)
####################################6
fruits = ["orange","apple","lemon"]
for fruits in fruits:
    print(fruits)
####################################7
fname = "Abdelkhalek"
lname = "Allan"
print("My name is "+fname +" Nael "+lname)
name = input("What is your name ? ")
print(name+" Nael Ahmad Allan")
#####################################Q8
name = "Abdelkhalek"
age = 20
score = 24.5
IT = False
print("My name is " +name+ " I age"+str(age))
#####################################Q9
num1 = 3
num2 = 5
print(num1 +num2)
#####################################Q10
print("Don\'t")
#Q10
print("""Abdelkhalekate the apple
       mohammad play foatboll""")
#####################################Q12
#Bulit-in functions
print()
int()
str()
print(len("mohammad")) 
print(type(3.5))
print(type("Mohammd"))
print(type(3))
print(type(False))
#string methods 
print("Abdelkhalek".find("A"))
######################################Q13
massage =  "s7ee7 love python"
name = massage[0:5]
world = massage[6:10]
print(name)
print(world)
####################################Q14
name = "Abdelkhalek Allan"
first_name = name[0:11]
last_name =name[12:]
print(first_name)
print(last_name)
##################################Q15
number = -3
number12 = 3.52
print(abs(number))
print(round(number12))
print(sum([3,4,523,23]))
print(min([42,52,653,2]))
print(max([23,5,2,523,235,52352]))
##################################Q16
# incrementation
number2 = 3
number3 = 4 + number2 
print(max(number2,number3))
print(number3)
number23 = 3
number12 += 43
print(number12)
####################################Q17
#Nested  For loops :لوب داخل لوب 
cars = ["ferrari","aston martin","bmw"]
adjectives = ["fast", "expensive"]
for car in cars:
    print(car +":")
    for adj in adjectives:
        print("-"+adj)
    print("\n")
for x in range(5):
    print("hi")
######################################Q18
age = input("What is your age?\n")
age = int(age)
if age > 17 :
    print("you are elgibe to take driver test")
else:
    print("you are not elgible to take the driver test")
    exit()
driver_test = input("Have you passed the driver test : ")
if driver_test.lower() == "yes":
    print("Congrats,now you can have a driver license")
elif driver_test.lower() =="no":
    print("Sorry, you need to take the test again to pass")
else:
    print("you did't answer correctly")
####################################Q19
name = "Abdelkhalek Allan"
y = 0
for x in name :
    y +=1
    print(x +" "+str(y))
print(str(y))
print(len("Abdelkhalek Nael Ahmad Allan"))
####################################Q20
name = input("what is your name ? ")
y = 0
for x in name: # or letter
    y +=1
    print(x+" "+str(y))
    print(len(name))
####################################Q21
for x in range(1, 15 , 3):
    print("Hello " + str(x))
####################################Q22
name ="Mahmoud"
for x in name:
    print(x)
#####################################Q23
name = input("what is your name ? ")
x = 0
for letter in name:
    x +=1
print(name+" has "+ str(x) +" letters")
####################################Q24
name = "Abdelkhalek Allan"
x = 0
for y in  range(1,10):
    x +=1 
    print("Abdelkhalke ALlan "+str(y))
print(str(y))
###################################Q25
for x in range(5):
    print("Abdelkhalek Allan"*2)
###################################Q26
#comment
#1 >= 3 # False - no loop
#1 < 3 #True - loop
"""
print("fasdfasdf")
"""
####################################Q27
x =0
while x<3:
    x +=1
    print("Hello")
####################################Q28
x = 0
x = 1
while x :
    print("A")
###################################Q29
"""
==
!=
>
<
>=
<=
"""
print(18==18)
print(16<=18)
print(17>=18)
if 8 ==18:
    print("These are Identical")
else:
    print("These Numbers are Not Identical")
###################################Q30
Name = input("what is your name? ")
if Name.lower() =="mohammed":
    print("Take the ball")
else:
    print("No ball for you")
   #################################Q31
while True:
  Name = input("what is your name ? ")
  if Name :
     print("Nice to meet you"+Name)
     break
  else:
    print("Plese enter your name")
print("Hi")
#################################Q32
number = input("choose a number : ")
number = int(number)
x = 0
while x < 10:
      x +=1
      if x == number:
            continue
      print(x)
################################Q33
# not 
# and 
# or
if not 4 == 3 :
    print("thats true")
#########################Q34
students = [" Mohammed"," khaled"," Ali"]
x = 1
for student in students :
    print("student : " +str(x)+" "+student)
    x +=1
###############################Q35
students = ["Mohammed","Khaled","ali"]
print(students.index("Mohammed"))
################################Q36
students = ["Mohammed","Khaled","ali"]
print(students.index("Mohammed"))
###3:19 PM 1/6/2024
students = ["Mohammed","Khaled","ali"]
print(students.pop())
print(students)
#####################################37
student_age = { "Ahmad":21
               ,"Abdelkhalek":20
               ,"khaled":19
}
print(student_age.get("Abdelkhalek"))
months = { 1: "january",
           2: "feburary",
           3:"march",
           4:"april",
           5:"may",
           6:"june",
           7:"july"}
print(months.get(5))
####################################38
months ={1:"january",
         2:"February",
         3:"March",
         4:"April",
         4:"May",
         6:"june",
         7:"july",
         8:"August",
         9:"September",
         10:"October",
         11:"November",
         12:"December"}
for month in months:
    print(str(month)+"- "+months.get(month))
########################################39
months ={1:"january",
         2:"February",
         3:"March",
         4:"April",
         4:"May",
         6:"june",
         7:"july",
         8:"August",
         9:"September",
         10:"October",
         11:"November",
         12:"December"}
for keys,values in months.items():
    print(str(keys)+" "+values)
########################################40
months ={1:"january",
         2:"February",
         3:"March",
         4:"April",
         4:"May",
         6:"june",
         7:"july",
         8:"August",
         9:"September",
         10:"October",
         11:"November",
         12:"December"}
for keys,values in months.items():
    print(str(keys)+" "+values.upper())
########################################41
coordinates =(33,44)
#print(coordinates[1])
for coordinate in coordinates:
    print(coordinate)
##########################################42
#Functions
def print5times():
    for x in range(5):
        print(" hi")
print5times()
########################################43
def additioon(num1,num2):
    print(num1+num2)
additioon(3,5)
print(additioon)
##################################44
def subtration (num1,num2):
    print(num1-num2)
    
subtration(4,2)
###################################45
#Functions
def print5times(text,times):
    for x in range(times):
        print(text)
print5times("hallo",12)
#########################################46
def print5times():
    for x in range(10):
        print(str(x)+" hi")
print5times()
#############################################47
def addition(num1,num2=2):
    print(num1+num2)
addition(4)
##########################################48
def addition(num1=2,num2=2):
    print(num1+num2)
addition(4)
#########################################49
#email
#password
#username
def registration(username=False,email=False,password=False):
    if username and email and password:
        print("Registation Successful")
    else:
        print("Registration Unsucessful")
registration("Abdelkhalek","abdelkhalek.allan1@gmail.com",324232)
################################################50
#  flexible arguments
def registration(username=False,email=False,password=False):
    if username and email and password:
        print("Registation Successful")
    else:
        print("Registration Unsucessful")
registration(email="abdelkhalek.allan1@gmail.com",username="Abdelkhalek Allan", password=23423423)
################################################51
#Function - Return
count = len("Abdelkhalek Allan")
print(count)
######################################52
def registration(username=False,email=False,password=False):
    if username and email and password:
        return "Registation Successful"
    else:
       return "Registration Unsucessful"
student1 = registration('Abdelkahelk',"abdelkhalek.allan1@gmail.com",12423423)
print(student1)
#########################################53
def registration(username=False,email=False,password=False):
    if username and email and password:
        return [username,email,password]
    else:
       return "Registration Unsucessful"
student1 = registration('Abdelkahelk',"abdelkhalek.allan1@gmail.com",12423423)
student2 = registration("Nael Ahmad Allan","naelallan1@gmail.com",2342342)
print(student2)
#################################################54
def registration(username=False,email=False,password=False):
    if username and email and password:
        print( [username,email,password])
    else:
      print("Registration Unsucessful")
student1 = registration('Abdelkahelk',"abdelkhalek.allan1@gmail.com",12423423)
student2 = registration("Nael Ahmad Allan","naelallan1@gmail.com",2342342)
print(student2)
#هذا الكود غلط ما بزبط بس عشان تتأكد من صحت حله 
###################################################55
#Function -scope
#local
#global
def greet():
    name = "osama"
    return "hi " +name #local
print(greet())
######################################56
#Function -scope
name = "osama"
age = 21
def greet():
    global age
    global name #global
    name += " Ahamd"
    return "hi " +name
print(greet())
print(name)
print(age)
#######################################57
#local
def greet():
    age =18
    return age
age =greet()
age +=1
print(age)
##################################58
#global
age =19
def greet():
    global age
    return age 
print(greet())
############################################59
#أنواع ال error  :
#comment python errors
"""

#syntax errors
def greet:
    return "hi"
#NameError
major ="software"
mayor +="enginner"
#zeroDivisionError
num1 =5
num2 = 0
total = num1 / num2
#IndexError
fruits =["Orange","apple","lemon"]
print(fruits[3])
#KeyError
person ={"name":"joe","employee":True}
print(person[3])
#ValueError
hubby = "basketball"
int(hubby)
#TypeError
print("Hi my naem is hussam and my age is "+33)
#Indentation Error
   print("Hallo")
   """
#######################################60
#هذا حل ال error :
#comment python errors

#syntax errors
def greet():
    return "hi"
#NameError
major ="software"
major +="enginner"
#zeroDivisionError
num1 =5
num2 = 1
total = num1 / num2
#IndexError
fruits =["Orange","apple","lemon"]
print(fruits[2])
#KeyError
person ={"name":"joe","employee":True}
print(person["name"])
#ValueError
hubby = "23"
int(hubby)
#TypeError
print("Hi my naem is hussam and my age is "+str(33))
#Indentation Error
print("Hallo")
#Indentation Error
if 1 == 1:
    print("Hello")
#######################################61
#Raising Errors
def chooseNumber():
    number = input("choose a number from 1 to 10\n")
    number =int(number)

    if number < 1 or number >10:
        raise ValueError("plese insert from 1 to 10")
    else:
        print("Your number is "+str(number))
chooseNumber()
########################################62
#Modules
import random
import turtle
random_number = random.randint(0,100)
print(random_number)
for x in range(50):
    turtle.forward(90)
    turtle.right(1000)
##################################################63
import random as rand
import turtle as snake
random_number = rand.randint(0,100)
print(random_number)
for x in range(50):
    snake.forward(90)
    snake.right(1000)
##################################################64
from random import randint
import turtle as snake
random_number = randint(0,100)
print(random_number)
for x in range(50):
    snake.forward(90)
    snake.right(1000)
    
##########################################65
#creating Modules 
#example :
#new file hallo.py
import pro

print(pro.name)
print(pro.addition(4,32))
#and new file pro.py
name ="osama"
def addition(num1,num2):
    return num1+num2
########################################66
#go to cmd wirte :pip install termcolor
#go to vs code write :
import  termcolor
termcolor.cprint("hello","blue")
########################################################67
#Python Object-Oriented Programming
age = 18
def greet():
    print("hello")

print(type(greet))
####################################################68
name ="Mohammed"
print(type(name))
print(name.upper()) #upper : method : لأنها حولة الكلمة لحروف كبيره ولاكن داخل str
################################################
price = 3.5
print(price.is_integer())#.is_integer :method أحد داخل float
#########################################
class Cat: #allwoas CAPITAL NO SMOL
    def meow(self):
        print("meow meow meow")
    

cat1  = Cat() #veriable cat1
print(cat1.meow())
print(type(cat1))
###############################################
class Dog:
    def bark(self): # bark :ينبح 
        print("ho ho ho")

dog1 = Dog()
print(dog1.bark())
print(type(dog1))
#########################################
class Dog:
    def add(self,num1,num2):
        return num1 +num2

    def color(self):
        return"BLACK"

dog1 = Dog()
print(dog1.add(2,3))
print(dog1.color())
##########################################
class Humman:
    def __init__(self,name,age,food): # __init__ method # self : عباره عن داله
        #init :initialize 
        self.name = name #self.name :Attribute#
        self.age = age
        self.food = food
        self.email =self.name +"@"+"gamil.com"

    def display_food(self):
        return self.food
    
    def color(self):
        print(self.name+" i love Black")

humman1 = Humman("abdelkhalek",20,"shaworma")
humman2 =Humman("aos",8,"burgar")
print(humman1.email)
###################################
