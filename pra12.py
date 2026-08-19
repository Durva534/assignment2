Basic_salary = int(input("enter the employee's basic salary"))
if (basic_salary <=10000):
    HRA =(basic salary*100)/20
    DA = (basic salary*100)/80
    print("\n gross salary:" , basic salary + HRA + DA)
elif (basic_salary <=20000):
    HRA =(basic salary*100)/25 
    DA =(basic salary*100)/90
     print("\n gross salary:" , basic salary + HRA + DA)
elif (basic_salary >20000):
    HRA =(basic salary*100)/30
    DA =(basic salary*100)/95 
     print("\n gross salary:" , basic salary + HRA + DA)
    
    
    
    
