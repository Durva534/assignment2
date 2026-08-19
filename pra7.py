num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
num3 = int(input("enter third number"))
if(num1>num2>num3):
    print("the largest number among the three is:",num1)
elif (num1<num2<num3):
    print("the largest number among the three is:",num3)
elif (num1==num2==num3):
    print("there is no largest number among three numbers")
else:
    print("invaild input,plese check")
