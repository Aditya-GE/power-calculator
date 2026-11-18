# ATM cash dispenser
print("===ATM cash dispenser===\n")
total_100 = total_50 = total_20 = total_10 = total_5 = total_1 = 0
customers_served = 0
total_dispensed = 0

serving = True                               #outer while--one customer per loop
while serving:
    name = input("Enter customer name: ")
    amount = int(input(f"Hello {name}! Enter withdrawal amount: "))
    if amount <= 0:
        print("Invalid amount. Please enter a positive number.")
        continue

    print(f"\nDispensing {amount} units for {name}...\n")
    remaining = amount
    idx = 1
    while idx <= 6:                          #inner while--breaks amount into notes
        if idx == 1: value = 100
        elif idx == 2: value = 50
        elif idx == 3: value = 20
        elif idx == 4: value = 10
        elif idx == 5: value = 5
        else: value = 1
        count = remaining // value
        if count > 0:
            print(f" {count} x {value}-unit note(s) = {count * value} ")
            remaining -= count * value
            if value == 100: total_100 += count
            elif value == 50: total_50 += count
            elif value == 20: total_20 += count
            elif value == 10: total_10 += count
            elif value == 5: total_5 += count
            else: total_1 += count
        idx += 1


    customers_served += 1
    total_dispensed += amount
    print(f"transaction complete {name},\n")
    again = input("next customer (yes/no): ").strip().lower()
    if again != "yes":
        serving = False

print(f"\n=== Daily denomination report===")
for slot in range(1, 7):
    if slot == 1: value = 100; count = total_100
    elif slot == 2: value = 50; count = total_50
    elif slot == 3: value = 20; count = total_20
    elif slot == 4: value = 10; count = total_10
    elif slot == 5: value = 5; count = total_5
    else: value, total = 1 , total_1
    if total > 0:
        print(f" {value}-unit notes dispensed: {total}", end=" ")
        for note in range(total):
            print("=", end="")
        