i = 1
while i <= 10:
    print(i,end = ",")
    i+= 1

i = 10
while i > 0:
    print(i,end = "-")
    i-= 1


total_chores = 4
original_count = total_chores
print(f"You have {original_count} chores to finish today!\n")

completed_count = 0
chore_num = 1



while chore_num <= total_chores:


    if chore_num == 1: next_chore = "make your bed"   
    elif chore_num == 2: next_chore = "feed the pet" 
    elif chore_num == 3: next_chore = "do the dishes"
    elif chore_num == 4: next_chore = "take out the trash"
    else: next_chore = "wash the dishes"


    answer = input(f"Have you finished: {next_chore}? (yes/no): ")         


    if answer == "yes":
        completed_count += 1
        chore_num += 1
        print("great job! chore completed")
    else:
        print("okay,finish and check again!")                                  
