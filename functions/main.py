def sum(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
def floor(a, b):
    return a // b
def mod(a, b):
    return a % b
print (sum (2, 3))
print (sub (60, 51))
print (mul (5, 2))
print (div (5, 2))
print (floor (5, 2))
print (mod (5, 2))


# part 1: define a function with no arguements to greet the customer
def greet_customer():
    print("Hello! Welcome to the lemonade stand.")
    print("fresh lemonsade , made just for you.")


#part2:call the greet_customer function 
greet_customer()

#part3: Ask for the price per cup and the number of cup sold
price_per_cup = float(input("Enter the price per cup in dollars: "))
cups_sold = int(input("Enter the number of cups sold: "))

#part4: Define a function that takes arguements and returns the total cost
def calculate_total(price, cups):
    total = price * cups
    return total

#part5: Call the calculate_total and store the value it returns
total_cost = calculate_total(price_per_cup, cups_sold)

#part6: Use a built-in function to round the total , then print it
rounded_total = round(total_cost, 2)
print("total cost:",rounded_total)

#part7: Ask how much money the customer paid
amount_paid = float(input("Enter the amount paid by the customer: "))

#part8: Define a function that takes arguements and returns the change due
def calculate_change(paid, total):
    change = paid - total
    return change

#part9: Call the calculate_change function and store the value it returns
change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)

#part10: define a function that returns a thank you message based on cups sold
def thank_you_message(cups):
    if cups > 5:
        return "WOW,big order! thanks so much for your support "
    else:
        return "Thank you for buying a cup of lemonade!"