# 5 Find the factorial of a given number using loops(note the number is received from the user)

number = int(input("Enter the number :"))

factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print(f"The factorial of the number {number} is {factorial}. ")