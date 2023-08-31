# Session 2 Exercises

## Section A
# 1. Create two variables that hold the width and height of a rectangle, work out and store the area in a third variable. 
# Print out the string: `Rectangle of width <x> and height <y> has an area of <area>`.
#x=int(input("Enter Length of Rectangle "))
#y=int(input("Enter Breadth "))
#z=x*y
#print(z)

# 2. Write code that prints the length of the string, 'python'.
#x=input("Enter your string \t")
#y=len(x)
#print ("The length of your string is " +str(y))
# 3. Print out the first and third letter of the word 'python'.
word = "python"
#print(word[0],word[2])


# 4. Ask the user to enter their name, and print out `Hello, <name>`.
name=input("what is your name? ")
#print ("Hello " + name)


# 5. Ask the user to enter their age, tell them how old they will be in 15 years time.

#age=input("what is your age? ")
#y=int(age)+15
#print("in 15 years you'll be " + str(y))

# 6. Combine the two input statements above and print out the message `Hello, <name>, you are currently <age> years old. 
#   In 15 years time you will be <age_in_15_years_time>`.
#print("Hello "+ name +" You are now" +str(age) +"years old. ""In 15 years your age will be "+str(y))


# 7. Ask the user to enter their hometown, print it out in uppercase letters.
#ht=str(input("What is your hometown? "))
#print(ht.upper())


# 8. Ask the user to enter their favourite colour and find out the length of the colour they input.



# 9. Ask the user to enter the weather and the month. Print out the string, `It is <month> and it is <weather> today`.



# 10. Ask the user to enter 5 different temperatures and the month. Work out the average temperature and print out the string: 
#   `It is <month> and the average temperature is <average_temperature> degrees celsius`.
#month=input("what month is it? ")
#t1=float(input("Please enter temperature for Day 1 - "))
#t2=float(input("Please enter temperature for Day 2 - "))
#t3=float(input("Please enter temperature for Day 3 - "))
#t4=float(input("Please enter temperature for Day 4 - "))
#t5=float(input("Please enter temperature for Day 5 - "))

#t_average=(t1+t2+t3+t4+t5)/5
#print("It is " +month + "and the average temperature is " +str(t_average) +" degrees celsius" )

# 11. Print out the above sentence but make the month upper case.

#print("It is " +month.upper() + "and the average temperature is " +str(t_average) +" degrees celsius" )

# 12. Create a variable that holds your favourite animals and print it out. 
#    Make sure the animals are all on different lines and tabbed.

#animal_1 =input("Enter your favorite animal \t")
#animal_2 =input("Enter your favorite animal \t")
#animal_3 =input("Enter your favorite animal \t")
#print(" Your favorite animals are \n")
#print("\n" + animal_1 +"\t" +animal_2 +"\t" +animal_3)



# 13. Ask the user to enter their name as well as a number. 
#    Print out the uppercase character at that position in the string.
#i=int(input("Enter string position "))
#j=len(name)
#print(name[i].upper())

# 14. Slice the string with steps of 2, excluding the first and last characters of the string "WelcometoPython".
z="WelcometoPython"
print(z[1::2])
