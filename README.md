# Conditional-and-Looping-Statements
# 1 Name your file: Write a program that reads an integer value between 1 and 12 from the user and prints
    # output the corresponding month of the year. An example run of the program

month = ( "January","February","March","April","May","June",
           "July","August","September","October","November","December")

month_Number = int(input("Enter the month :"))

if 1<= month_Number<=12:
    print(f"Month {month_Number} is {month[month_Number-1]}")
else:
    print("Invalid month. Please enter a number between 1 and 12.")

#  2 A certain cinema currently sells tickets for a full price of 6 pounds,
    #  but always sells tickets for half price to people who are less than 16 years old,
    #  and for a third of the price for people who are 60 years old or more.

full_price = 6.00

age = int(input("Enter your age :"))

if age<16:
    ticket_price = full_price/2
elif age>60:
    ticket_price = full_price/3
else:
    ticket_price = full_price

print(f"Your ticket costs £{ticket_price}")

#3 Write a program to calculate your BMI and give weight status. Body Mass Index (BMI) is an internationally used measurement
 # to check if you are a healthy weight for your height.The metric BMI formula accepts weight in kilograms and height in meters:
 # BMI= weight(kg)/height2(m2) BMI Weight Status Categories table BMI range - kg/m2 Category
 # Below 18.5 Underweight 18.5 -24.9 Normal 25 - 29.9 Overweight 30 & Above Obese

weight = float(input("Enter your weight in (kg): "))
height = float(input("Enter your height in (m): "))

bmi = weight / ( height * height )

if bmi < 18.5:
    category ="Underweight"
elif 18.5 < bmi <24.9:
    category = "Normal"
elif 25 < bmi < 29.9:
    category = "Overweight"
else:
    category = "Obese"

print(" Your bmi is :", round(bmi,2))
print("You are in the ",category," range")

# 4.Write a Python program to receive 3 numbers from the user and print the greatest among them.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the first number: "))

if num1 >= num2 and num1 >= num3:
    greatest = num1
elif num2 >= num1 and num2 >= num3:
    greatest = num2
else:
    greatest = num3

print("The greatest number is :",greatest)

# 5 Find the factorial of a given number using loops(note the number is received from the user)

number = int(input("Enter the number :"))

factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print(f"The factorial of the number {number} is {factorial}. ")

# 6 Reverse a number using while loop

number = int(input(" Enter the Number :"))

reversed_number = 0

while number > 0:
    digit = number%10
    reversed_number = reversed_number*10 + digit
    number = number//10

print("Reversed number is ", reversed_number)

# 7 Finding the multiples of a number using loop

number = int(input("Enter the number : "))
count = int(input("Multiples required : "))

i=1

print(f"The first {count} multiples of the {number} are :")

while i<=count:
    multiple = number*i
    print(multiple)
    i += 1

# 8 Write a program to print the inputted value as it is and break the loop if the value is 'done'.

while True:
    input_Value =input(":")
    if input_Value == "done":
        print("Done")
        break
    print(input_Value)

# 9 Write a program that prints the numbers from 1 to 10.
    # But for multiples of three print "Fizz" instead of the number and for the multiple of five print "Buzz".
    # For numbers which are multiples of both three and five print "FizzBuzz"

for num in range(1,11):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 ==0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# 10.Write a program to print the following pattern:
    # 5 4 3 2 1
    # 4 3 2 1
    # 3 2 1
    # 2 1
    # 1

for i in range(5,0,-1):
    for j in range (i,0,-1):
        print(j,end = "")
    print()
