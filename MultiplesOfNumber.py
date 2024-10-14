# 7 Finding the multiples of a number using loop

number = int(input("Enter the number : "))
count = int(input("Multiples required : "))

i=1

print(f"The first {count} multiples of the {number} are :")

while i<=count:
    multiple = number*i
    print(multiple)
    i += 1