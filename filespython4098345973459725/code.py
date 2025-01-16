from random import randint

with open("students.txt", "r") as students:
    for line in students:
        print(line.strip())
 
with open("students.txt", "r") as students:
    for line in students:
        if len(line) > 2:
            print(line[2])

with open("students.txt", "r") as students:
    for line in students:
        if len(line) > 6:
            print(line.strip())

with open("students.txt", "r+") as students:
    for line in students:
        students.write("," + str(randint(0,100)))

userinp = input("Insert your own name into file: ")

with open("students.txt", "a") as students:
    students.write(userinp + "\n")
    print("Done")
    
#I didnt get to finish extensions because i was helping the other glorbs and schneebs
