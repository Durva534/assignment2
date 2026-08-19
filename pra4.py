month=input("Enter month name:")
if(month=="february"):
    print("28 or 29 days in a momth")
elif(month in[april,june,september,november]):
    print("30 days in a month")
elif(month in [january,march,may,july,august,octobar,december]):
    print("31 days in a month")
else:
    print("Invalid output")
