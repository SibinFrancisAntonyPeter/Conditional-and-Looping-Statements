# 8 Write a program to print the inputted value as it is and break the loop if the value is 'done'.

while True:
    input_Value =input(":")
    if input_Value == "done":
        print("Done")
        break
    print(input_Value)

