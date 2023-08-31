# Session 3 Exercises

## Section A
# 1. Ask for the user's name, if they are called "Bob", print "Welcome Bob!".

#name=input("WHat is you name? ")

# if name == "Bob":
#   print("Welcome Bob")

# 2. Ask for the user's name, if they are not called "Alice", print "You're not Alice!".

# if name != "Alice":
#   print ("You are not Alice")

# 3. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
#   If they get it wrong, print "Password failure".
# pw = input("Enter your password ")

# if(pw == "qwerty123"):
#   print("You are now logged in")
# else:
#   print ("Password failure")

# 4. Ask the user to enter a number, if the number is even, print "Even", otherwise print "Odd".

# x= int(input("Enter a number: "))
# y=x%2
# if y == 0:
#   print("even")
# elif y!=0:
#   print("odd");


# 5. Ask the user for 2 different numbers, if the total of the two numbers is over 21, print "Bust" otherwise print "Safe"



# 6. Ask the user to enter the length and width of a shape and check if it is a square or not.
# l= int(input("Enter Length: "))
# b= int(input("Enter breadth: "))
# if l==b:
#   print("Its a square \n")



# 7. You have had a great year and are going to offer a bonus of 10% to any employee who has a service of over 3 years.




#   Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.



# 8. Take a whole number input, if it's positive, print out the number cubed, if it is a negative, print out half its value.

# x= int(input("Enter a number \t"))
# if x>0:
#   print(x*x*x)

# elif x<0:
#   print(x/2)

# elif x == 0:
#   print ("its a zero")

# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask for the user's name, if they are called "Alice" print "Hello, Alice", if they are called "Bob", 
#   print "You're not Bob! I'm Bob", else print "You must be Charlie".



# 2. Ask the user to enter their age:
#     1. If they are younger than 11, print "You're too young to go to this school"
#     2. If they are between 11 and 16, print "You can can come to this school"
#     3. If they are over 16, print 'You're too old for school"
#     4. If they are 0, print "You're not born yet!"

# age = int(input("Enter your age: "))

# if(age ==0):
#   print("You aren't born yet! ")
# elif(age < 11):
#   print("You're too young to go to this school")
# elif(age <= 16 and age >=11):
#   print("You can can come to this school")
# elif(age > 16):
#   print("You're too old for school")

# else:
#   print("Enter correct age.") 



# 3. Ask the user to enter the name of a month. If the user enters March/April/May: print "<month> is in Spring", otherwise print "I don't know".
#     1. Expand for the rest of the year, given that summer is June/July/August. Autumn is September/October/November. Winter is December/January/February.
#     2. Ensure that when an unknown month is given it prints "I don't know".



# 4. Ask the user for two different numbers, if both numbers are even, print "Even", if both numbers are odd, print "Odd", else print the product of the two numbers.



# 5. Ask the user to input two numbers. Decide which is the number of highest value and print this out.



# 6. You have had a fantastic year and are now going to offer a bonus of 20% to any employee who has a service of over 7 years, 
#   a bonus of 15% to any employee who has a service of over 5 years and a bonus of 10% to any employee who has a service of 3 - 5 years. 
#    Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.

# salary=float(input("input your salary: "))
# tenure = int (input("enter your service "))

# if (tenure >=7):
#   print("Your bonus is: " + str(0.2 * salary))

# elif(tenure>=5 and tenure<7):
#   print("Your bonus is: " + str(0.15 *salary))

# elif(tenure>=3 and tenure<5):
#   print("Your bonus is: " + str(0.10*salary))

# else:
#   print("No Bonus!")
  

# 7. Take the age and name of three people and determine who is the oldest and youngest and print out the name and age of the oldest and youngest. 
#   If all three ages are the same, print that.
# name_1=input("Enter first Name: ")
# age_1=int(input("Enter age for " + name_1 + ":"))
# name_2=input("Enter second Name: ")
# age_2=int(input("Enter age for " + name_2 + ":"))
# name_3=input("Enter third Name: ")
# age_3=int(input("Enter age for " + name_3 + ":"))

# #Finding Oldest
# if(age_1>age_2 and age_1>age_3):
#   print(name_1 + "is the oldest. " +"age is " + str(age_1))

# elif(age_1> age_2 and age_1<age_3):
#   print(name_3 + "is the oldest. " +"age is " + str(age_3))

# elif(age_1> age_3 and age_1<age_2):
#   print(name_2 + "is the oldest. " +"age is " + str(age_2))

# #Finding Youngest
# if(age_1<age_2 and age_1<age_3):
#   print(name_1 + "is the Youngest. " +"age is " + str(age_1))

# elif(age_1< age_2 and age_1>age_3):
#   print(name_3 + "is the youngest. " +"age is " + str(age_3))

# elif(age_1< age_3 and age_1>age_2):
#   print(name_2 + "is the youngest. " +"age is " + str(age_2))

# else:
#   (print("Age is same"))

# print("good bye!")

# 8. A school has following rules for their grading system:
#     a.	Above 80 – A
#     b.	60 to 80 – B
#     c.	50 to 60 – C
#     d.	45 to 50 – D
#     e.	25 to 45 – E
#     f.	Below 25 - F
#   Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.
# lesson_1=input("Enter name of lesson: ")
# marks_1= int(input("Enter Marks for " + lesson_1 +":"))
# if (marks_1 >= 80):
#   Print("Grade obtained - A")

# elif(marks_1>=60 and marks_1<80):
#   print("Grade obtained - B")

# elif(marks_1>=50 and marks_1<60):
#   print("Grade obtained - C")

# elif(marks_1>=45 and marks_1<50):
#   print("Grade obtained - D")

# elif(marks_1>=25 and marks_1<45):
#   print("Grade obtained - E")
# elif(marks_1 < 25):
#   print("Grade obtained - F")

# #Lesson -2 
# lesson_2=input("Enter name of lesson: ")
# marks_2= int(input("Enter Marks for " + lesson_2 +":"))

# if (marks_2 >= 80):
#   Print("Grade obtained - A")

# elif(marks_2>=60 and marks_2<80):
#   print("Grade obtained - B")

# elif(marks_2>=50 and marks_2<60):
#   print("Grade obtained - C")

# elif(marks_2>=45 and marks_2<50):
#   print("Grade obtained - D")

# elif(marks_2>=25 and marks_2<45):
#   print("Grade obtained - E")
# elif(marks_2 < 25):
#   print("Grade obtained - F")

# #Lesson 03

# lesson_3=input("Enter name of lesson: ")
# marks_3= int(input("Enter Marks for " + lesson_3 +":"))

# # Assigning grades

# if (marks_3 >= 80):
#   print("Grade obtained - A")

# elif(marks_3>=60 and marks_3<80):
#   print("Grade obtained - B")

# elif(marks_3>=50 and marks_3<60):
#   print("Grade obtained - C")

# elif(marks_3>=45 and marks_3<50):
#   print("Grade obtained - D")

# elif(marks_3>=25 and marks_3<45):
#   print("Grade obtained - E")
# elif(marks_3 < 25):
#   print("Grade obtained - F")



