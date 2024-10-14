# 6 Reverse a number using while loop

number = int(input(" Enter the Number :"))

reversed_number = 0

while number > 0:
    digit = number%10
    reversed_number = reversed_number*10 + digit
    number = number//10

print("Reversed number is ", reversed_number)
