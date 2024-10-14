# 1 Name your file: Write a program that reads an integer value between 1 and 12 from the user and prints
    # output the corresponding month of the year. An example run of the program

month = ( "January","February","March","April","May","June",
           "July","August","September","October","November","December")

month_Number = int(input("Enter the month :"))

if 1<= month_Number<=12:
    print(f"Month {month_Number} is {month[month_Number-1]}")
else:
    print("Invalid month. Please enter a number between 1 and 12.")



