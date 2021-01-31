#Problem 1 : creating payslip

#To promt the user to input their details and import date for the employee

import datetime
name= input("Enter your name:")
employeenum= input("Enter employee number:")
date= print("Enter week ending date-")
year = int(input('Enter a year:'))
month = int(input('Enter a month:'))
day = int(input('Enter a day:'))
date1 = datetime.date(year, month, day)
print("year-month-day:",date1)


number_hour=float(input("Hours worked:"))
Hour_rate=float(input("Hourly Rate:"))
Overtime_rate=float(input("overtime Rate:"))
standard_taxrate=float(input("Standard tax:"))
overtime_taxrate=float(input("Overtime tax:"))

#Calculation of overtime , Hours worked, Rate for over time, Tax rate , Calculation of amount after deductions , net amount payable.  

overtime_fairrate= (Hour_rate*1.5) #calculating the overtime
Total_hourly_amt=37.50*Hour_rate #the amount for hourly work would be the limit provided, i.e 37.50 multiplied by the rate
After_deduction_1=((Total_hourly_amt*20)/100) #calculating the tax amount
overtime_A=number_hour-37.50 #overtime hours
Total_hourly_rate_2=overtime_A*Hour_rate*Overtime_rate #calculating the hourly rate
After_deduction_2=Total_hourly_rate_2-((Total_hourly_rate_2*50)/100) #calculating the deduction for overtime
totalamount=Total_hourly_amt+Total_hourly_rate_2 #Final amount
print("total",totalamount)
Total_deduction=After_deduction_1+After_deduction_2
print("Total deduction",Total_deduction)
net_amt=Total_hourly_amt+Total_hourly_rate_2-Total_deduction #net amount is the final payment available to the person after  adding the total income and deducting the deductions
print("Net pay",net_amt)


#printing the payslip


print("\nP A Y S L I P")  
print("WEEK ENDING", date1)  
print("Employee", name)
print("Employee Number " ,employeenum)  
print("                                    Earnings                     Deductions      ")                 
print("                                    Hours     Rate   Total                             ")
print("                 Hours (normal)     37.50     "+   str(Hour_rate)+"    "+str(Total_hourly_amt)+          "      Tax @ "+str(standard_taxrate)+"%  "+   str(After_deduction_1))
print("                 Hours (overtime)   "+str(overtime_A)+"      "+str(overtime_fairrate)+"   "+ str(overtime_A*overtime_fairrate)+   "      Tax @ "+str(overtime_taxrate)+"% "+ str(After_deduction_2))

print("                                                                  Total pay",totalamount)
print("                                                                  Total deductions",Total_deduction)   
print("                                                                  Net pay",net_amt)

