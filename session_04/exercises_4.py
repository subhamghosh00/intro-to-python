import numpy as np

# Session 4 Exercises
# a=np.array([1,2,3,4,5])
# print(a)
## Section A
# 1. Create the following list of items: Apples, Cherries, Pears, Pineapple, Peaches, Mango. Then print the list.
fruits =["Apples", "Cherries", "Pears", "Pineapple", "Peaches", "Mango"]
# print(fruits)

# for index in range(4):
#   print(fruits[index])


# # # 2. Add "Grapes" to the list and print the list.
# fruits.append("Grapes")
# # print(fruits)

# # # 3. Change "Pears" to "Strawberries" and print the list.
# fruits[2]= "Strawberries"
# # print(fruits)

# # 4. Remove "Apples" from the list and print the list.

# del(fruits[0])
# print(fruits)
# # 5. Print out the current length of the list.

# print(len(fruits))

# # 6. Order the list alphabetically.
# fruits.sort()
# print(fruits)


# # 7. Print out the list again.
# print(fruits)



# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Loop through the list you created in section A and print each item out.

# for fruit in fruits:
#   print(fruit)


# 2. Print the numbers 1 to 100 (including the number 100).
# for i in range(0,101):
#   print(i)
  


# 3. Print all odd numbers from 1 to 100.
# for i in range(1,100,2):
#   print(i)


# 4. The modern olympics started in 1896, print the years they have been held (bonus points to skip the years it has not been held 1916, 1940, 1944, 2020).

# years_nh = [1916,1940,1944,2020]
# years = range(1896,2022,4)
# for i in years:
#   if i not in years_nh:
#       print(i)
  


  

# 5. Create a list of ten random numbers. Loop through your list and count the number of even numbers and the number of odd numbers.

numbers =[1,44,3003,90,84,77,982,9575,839,875,739,534,5856]
odd_count=0
even_count=0

for i in numbers:
  if i%2 ==0:
    odd_count=odd_count+1
    if 

# 6. Create a list of five names. Write a loop that will print "Hello" plus each name in the list.



# 7. Create a loop to go through each letter of the word "supercalifragilisticexpialidocious".



# 8. Create a list of 5 numbers. Write a for loop which appends the square of each number to the new list.



# 9. Create a list with five names in. Write a for loop which appends  Dr. to each name in the new list.



# 10. FizzBuzz – Write a program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number and for multiples of five, print "Buzz". 
#    For numbers which are multiples of both three and five, print "FizzBuzz".

#     ```
#     1
#     2
#     Fizz
#     4
#     Buzz
#     Fizz
#     7
#     8
#     Fizz
#     Buzz
#     11
#     Fizz
#     13
#     14
#     FizzBuzz
#     ```
