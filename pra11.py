physics =int(input("enter marks for physics"))
chemistry =int(input("enter marks for chemistry"))
mathematics =int(input("enter marks for mathemaics"))
biology =int(input("enter marks for biology"))
computer =int(input("enter marks for computer"))
total_marks = physics + chemistry + mathematics + biology + computer
percentage=total_marks/3
if (percentage >= 90):
    grade = "A"
elif (percentage >= 80):
    grade = "B"
elif (percentage >= 70):
    grade = "C"
elif (percentage >= 60):
    grade = "60"
elif (percentage >= 40):
    grade = "E"
elif (percentage < 40):
    grade = "F"
else:
    print("you are fail")
print("\n Grade:",grade)
    
    
    
