# ================================
# GROCERY BILLING QUEUE
# ================================
print("=== Grocery Billing Queue ===\n")

# ---------- PART 1: the five counters ----------
low_price_items = 0
medium_price_items = 0
high_price_items = 0

customers_served = 0
total_sales = 0

billing = True

# ---------- PART 2: the OUTER while loop — one customer per repeat ----------
while billing:
    customer_name = input("Enter customer's name: ")
    item_count = int(input("How many items are they buying? "))

    # ---------- PART 3: continue on a bad item count ----------
    if item_count <= 0:
        print("Invalid item count. Please enter a number greater than 0.\n")
        continue

    # ---------- PART 4: the INNER while loop — one item per repeat ----------
    customer_total = 0
    item_number = 1

    while item_number <= item_count:
        print(f"\nItem {item_number}:")
        item_name = input("  Item name: ")
        price = int(input("  Price: "))
        quantity = int(input("  Quantity: "))

        # ---------- PART 5: item total and price band ----------
        if price <= 0 or quantity <= 0:
            print("  Price and quantity must be greater than 0. Try this item again.")
            continue

        item_total = price * quantity
        print(f"  {item_name}: {quantity} x {price} = {item_total}")
        customer_total += item_total

        if price < 50:
            low_price_items += quantity
        elif price <= 100:
            medium_price_items += quantity
        else:
            high_price_items += quantity

        item_number += 1

    # ---------- PART 6: finish the customer, ask about the next ----------
    customers_served += 1
    total_sales += customer_total
    print(f"\nTotal for {customer_name}: {customer_total}")

    next_customer = input("Next customer? (yes/no): ").strip().lower()
    if next_customer != "yes":
        billing = False
    print()

# ---------- PART 7: the NESTED for report ----------
print("=== Daily Summary Report ===")
bands = [
    ("Low (< 50)", low_price_items),
    ("Medium (50-100)", medium_price_items),
    ("High (> 100)", high_price_items)
]

for band_name, count in bands:
    print(f"{band_name}: ", end="")
    for _ in range(count):
        print("*", end="")
    print()

print(f"\nCustomers served: {customers_served}")
print(f"Total sales: {total_sales}")
