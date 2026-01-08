"""

#Write a python program to check whether the given year is a leap year or not 

year=int(input("Enter the year to check if it is a leap year or not: "))

if (year%4==0 and year%100!=0) or (year%400==0 and year%100==0):
    print("Leap Year")

else:
    print("Not a Leap Year")

----------------------------------------------------------------------------------------------------

#Write a python program to find and display the maximum of three given numbers

first_number=int(input("Enter the first number: "))
second_number=int(input("Enter the second number: "))
third_number=int(input("Enter the third number: "))

if (first_number>=second_number) and (first_number>=third_number):
    print(f"The largest number is {first_number}")

elif (second_number>=first_number) and (second_number>=third_number):
    print(f"The lrgest number is {second_number}")

elif (first_number==second_number==third_number):
    print("All the three numbers are equal")

else:
    print(f"The leargest number is {third_number}")


--------------------------------------------------------------------------------------------------------

#Write a python program to print the first n Fibonacci Numbers

n1=0
n2=1

num=int(input("Enter the value of n to generate first n Fibonacci Numbers: "))

if num<=0:
    print("Invalid value! Enter a natural number")

elif num==1:
    print(n1)

elif num==2:
    print(n1, n2)

elif num>2:
    print(n1, n2, end=" ")
    for i in range (1, num-1):
        n3=n1+n2
        print(n3, end=" ")
        n1=n2
        n2=n3



--------------------------------------------------------------------------------------------------------------

'''

An organization has decided to provide salary hike to its employees based on their job level. Employees can be in job levels 3, 4 or 5. 
In case of invalid job level, consider hike percentage to be 0. Given the current salary and job level, write a python program to find 
and display the new salary of an employee. 

JL=3, Hike percentage=15
JL=4, Hike percentage=7
JL=5, Hike percentage=5

'''

job_levels=int(input("Please enter the Job Level of the employee"))

default_current_salary="NA"
current_salary_jl3=20000
current_salary_jl4=40000
current_salary_jl5=50000

if job_levels not in (3, 4, 5):
    print("Invalid Job Level; Please enter a valid Job Level")
    new_salary=default_current_salary
    print("Salary: ", new_salary)

elif job_levels==3:
    hike_percentage=15
    new_salary=((int(hike_percentage)/100)*current_salary_jl3) + current_salary_jl3
    print("The updated salary after hike is: ", new_salary)

elif job_levels==4:
    hike_percentage=7
    new_salary=((int(hike_percentage)/100)*current_salary_jl4) + current_salary_jl4
    print("The updated salary after hike is: ", new_salary)

else:
    hike_percentage=5
    new_salary=((int(hike_percentage)/100)*current_salary_jl5) + current_salary_jl5
    print("The updated salary after hike is: ", new_salary)

---------------------------------------------------------------------------------------------------

#Write a Python function factorial(num) which return the factorial of a given number 

def factorial(num):
    if num>=0:
        product=1
        for i in range (1, num+1):
            product*=i
        
        return product

num=int(input("Enter the number to find its factorial "))

if factorial(num):
    print(f"The factorial of {num} is {factorial(num)}") 

else:
    print("Invalid value entered!! Please enter a whole number")

"""