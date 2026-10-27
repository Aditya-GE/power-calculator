# ================================
# POWER CALCULATOR
# ================================

print("=== Power Calculator ===")

# ---------- PART 1: ask the two questions ----------
# YOUR CODE HERE
base = int(input("Enter the base number: "))
exponent = int(input("Enter the power: "))

# ---------- PART 2: the running total ----------
result = 1
# Create a variable called  result  and start it at 1.
# Think about why 1 and not 0 before you write it. The hint below explains.


# ---------- PART 3 + 4: the loop that multiplies ----------
for i in range(1, exponent + 1):
    result *= base
    print(f"Step {i}: result is now {result}") 
# for i in range(1, exponent + 1):
#     multiply result by base and store it back in result
#     print which step you are on and what result is now


# ---------- PART 5: the answer ----------

# After the loop, print the base, the exponent, and the result
print(f"{base} to the power of {exponent} is {result}")