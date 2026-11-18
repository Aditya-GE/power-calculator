n = int(input("Enter how many rows"))
for r in range(0, n):
    for c in range(0, r + 1):
        print("*", end="")
    print()




n = int(input("Enter how many rows"))
k = 1
for r in range(0,n):
    for c in range(0,r+1):
        print(f"{k} ", end="")
        k+= 1
    print()


n = int(input("Enter how many rows"))
for r in range(0,n):
    for c in range(0,r+1):
        print(f"{r+1} ", end="")
    print()