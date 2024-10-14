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

