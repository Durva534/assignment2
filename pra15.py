amount = int(input("Enter amount:"))
notes = [500,200,100,50,20,10]
count = 0
for note in notes:
    count += amount//note
    amount = amount%note
print("Total number of notes=",count)
