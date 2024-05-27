# -------------------EASY QUESTIONS--------------------

#Q1- Variable: Create a variable x and assign the value 10 to it. Then create another variable y and assign it the value 5. Print the sum of x and y.
# x =10
# y=5
# print(x+y)

#Q2- Condition: Write a Python program that checks if a number stored in the variable num is positive, negative, or zero. Print "Positive", "Negative", or "Zero" based on the value of num.

# number=1
# if(number>0):
# 	print("Positive")
# elif(number<0):
# 	print("Negative")
# else:
# 	print("Zero")

# Q3- List: Create a list numbers with the values [1, 2, 3, 4, 5]. Print the third element in the list.

# numbers = [1,2,3,4,5]
# print(numbers[2])

# Q4- String: Write a Python program that takes a string text and prints it in uppercase.

# str = input("Write something and ill convert it into upper case")
# print(str.upper())

#Q5- Loop: Write a Python program that prints all the numbers from 1 to 10 using a for loop.

# for i in range(1,11):
# 	print(i)

# i = 1
# while i<11:
# 	print(i)
# 	i += 1


# --------------INTERMEDIATE QUESTIONS-----------------

# Q1- Logical Operator: Write a Python program that checks if a number n is between 10 and 20 (inclusive). Print "Yes" if it is, otherwise print "No".

# number = int(input("White a number "))
#
# if(number>=10 and number<=20):
# 	print("Yes")
# else:
# 	print("No")


# Q2- Math: Write a Python program that calculates the factorial of a number n using a for loop. The factorial of n (n!) is the product of all positive integers less than or equal to n.

# num = int(input("Write a number to find a factorial : "))
# fact = 1
# if (num==0 or num<0):
# 	print("Enter a positive number")
# else:
# 	while num > 1:
# 		fact = num * fact
# 		num -= 1
# 	print(fact)


# Q3- List: Write a Python program that takes a list of numbers nums and prints only the even numbers from the list.

# count = int(input("How many numbers u want to enter in list"))
# list = []
#
# for i in range(0,count):
# 	value = int(input())
# 	list.append(value)
#
# for i in range(0,count):
# 	if(list[i]%2==0):
# 		print(list[i])
#


# Q4 - String: Write a Python program that counts the number of vowels in a given string text.

# str =  input('Write any text to find how many vowels are there in it : ')
# count = 0
# for i in str:
# 	if(i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U' or i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
# 		count += 1
# print(count)

# Q5- Loop: Write a Python program that prints the Fibonacci sequence up to n terms, where n is a positive integer input by the user. The Fibonacci sequence is defined as:
#
# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2) for n > 1

# 0 1 1 2 3 5 8 13
#
# num = int(input('Give me number till you want to print fabbonaci series : '))
# prev,curr = 0,1
#
# for i in range(0,num):
# 	if(curr>num):
# 		print(prev)
# 		break
# 	else:
# 		print(prev)
# 		temp = curr + prev
# 		prev = curr
# 		curr= temp


# -------------------HARD QUESTIONS--------------------





