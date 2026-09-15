p = int(input("enter principal amount:"))
r = int(input("enter rate of interest:"))
t = int(input("enter time:"))
ci = p*(1+r/100)**t-p
print("compund interest=",ci)
