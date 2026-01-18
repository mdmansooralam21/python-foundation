#Write a python program to check whether the given year is a leap year or not 

year=int(input("Enter the year to check if it is a leap year or not: "))

if (year%4==0 and year%100!=0) or (year%400==0 and year%100==0):
    print("Leap Year")

else:
    print("Not a Leap Year")

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

#Write a Python Function factorial(num) which return the factorial of a given number 

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

#Write a Python Function is_palindrome(num) that accepts an integer num as argument and returns True if the num is palindrome 
#else returns false. Invoke the function and based on return value, print the output. 

def is_palindrome(num):
    rev_num=0
    temp_num=num
    while temp_num>0:
        rem=temp_num%10
        rev_num=(rev_num*10)+rem
        temp_num=temp_num//10
    
    if rev_num==num:
        return True

    else:
        return False

num=int(input("Enter the number to check if the integer is a palindrome or not: "))

if is_palindrome(num):
    print("Palindrome Number")

else:
    print("Not a Palindrome Number")

#Write a Python function check_amicable_numbers(num1, num2) that accepts two numbers num1 and num2 as arguments and returns True if the given pair of 
#numbers are amicable numbers else return false. Invoke the function and based on return value, print the numbers are amicable numbers or not. 

#num1 and num2 are said to tbe amicable numbers if sum of all the proper divisors (except num1 itself) of num1 is equal to num and sum of all the proper
#divisors of num2 (except num2 itself) is equal to num1. 

def check_amicable_numbers(num1, num2):
    sum1=0
    sum2=0

    if num1>0 and num2>0: 
        for div1 in range (1, num1):
            if num1%div1==0:
                sum1+=div1
        
        for div2 in range (1, num2):
            if num2%div2==0:
                sum2+=div2
            
        if (sum1==num2) and (sum2==num1):
            return True
        
        else:
            return False

print("Enter the two numbers to check if the numbers are Amicable Numbers or not\n")
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

if check_amicable_numbers(num1, num2):
    print("Amicable Numbers")

else:
    print("Not Amicable Numbers")

#Write a Python function check_strong_number(num) that accepts a positive integer as argument and return True if the number is strong number
#else false. Invoke the function and based on return value, print the number is strong number or not. 

def check_strong_number(num):
    if num>0:      
        sum=0
        temp_num=num

        while temp_num%10>0:
            remainder=temp_num%10
            product=1

            for i in range (1, remainder+1):
             product*=i
             
            temp_num=temp_num//10     
            sum+=product 
        
        if sum==num:
           return True
        
        else:
           return False
    else:
       print("Invalid Value!! Please enter a postive number")
    
num=int(input("Enter a number to check if it's a Strong Number or not: "))

if check_strong_number(num):
   print("Strong Number")

else:
   print("Not a Strong Number")

#Write a Python function right_shift(num, n) that takes two numbers num and n as arguments and returns value of the integer num 
#rotated to the right by n positions. Assume both the numbers are unsigned. Invoke the function and print the return value. 

#Hint: Use >> binary operators to shift the bits
#Example - num=60, n=2, output=15

INT_BITS=32
def right_shift(num, n):
    return (num >> n)

num = int(input("Enter a number: "))
n = int(input("Enter the number of positions to rotate: "))

result = right_shift(num, n)
print("The result of the rotation is:", result)


#Write a Python Function proper_divisors(num) which returns a list of all the proper divisors of given number. 

def proper_divisors(num):
    if num>0:
        divisor_list=[]
        for i in range (1, num):
            if num%i==0:
                divisor_list.append(i)
            
            else:
                continue

        return divisor_list

num=int(input("Enter the number to get a list of all proper divisior: "))
print(f"The below is the list of all proper divisors of {num}")
print(proper_divisors(num))

#Write a Python Function generate_fibonacci(n) to return a list of first n Fibonacci numbers. 

def generate_fibonacci(n):
    num1=0
    num2=1
    fibonacci_list=[]

    if n<=0:
        print("Invalid number entered!! Please enter a valid number i.e. A Natural Number")
    
    if n==1:
        fibonacci_list.append(num1)
    
    if n==2:
        fibonacci_list.append(num1)
        fibonacci_list.append(num2)

    if n>2:
        fibonacci_list.append(num1)
        fibonacci_list.append(num2)

        for i in range (1, n-1):
            num3=num1+num2
            fibonacci_list.append(num3)
            num1=num2
            num2=num3

    return fibonacci_list

n=int(input("Enter the number of Fibonacci Numbers to be generated: "))
print(f"The below is the list of {n} Fibonacci Numbers")
print(generate_fibonacci(n))

#Write a Python program to generate the next 15 leap years starting from a given year. Populate the leap years into a list and display the list. 

def generate_leap_year(year):
    year_list=[]

    while len(year_list) < 16:
        if (year%4==0 and year%100!=0) or (year%100==0 and year%400==0):
            year_list.append(year)  

        year+=1
          
    return year_list
    
year=int(input("Enter the year to generate next 15 years: "))
print(f"The below is the list of 15 leap years starting from {year}")
print(generate_leap_year(year))

#Given a list of integer values, write a Pyhton program to check whether the list contains the same number in adjacent poitions. 
#Display the count of such adjacent occurrences. 
#[1,1,5.100,-20,-20,6,0,0]
#[10,20,30,40,30,20]
#[1,2,2,3,4,4,4,10]

given_list=[1,2,2,3,4,4,4,10]

def adjacent_occurences(given_list):
    count=0
    for i in range (1, len(given_list)):
        if given_list[i]==given_list[i-1]:
            count+=1

    return count
    
print(f"The number of occurences is {adjacent_occurences(given_list)}")

#Write a Python program to generate the ticket numbers for specified number of passengers traveling in a flight as per the details mentioned below:
#The ticket number should be generated as airline:src:dest:number where
#AL1 --> airline, src and dest should be the first three characters of the source and destination cities. number should be auto generated starting from 101. 
#The program should return the list of ticket numbers of last five passengers. If passenger count is less than 5, return the list of all generated ticket numbers. 

import random

airline="AL1"
src=(input("Enter the source city: ").upper())[0:3]
dest=(input("Enter the destination city: ").upper())[0:3]

def generate_ticket(num_of_passenger):
    generated_ticket=[]
    
    for i in range (1, num_of_passenger+1):
        inital_ticket=airline + ":" + src + ":" + dest + ":"
        number=str(random.randint(101, 999))
        final_ticket=inital_ticket + number
        generated_ticket.append(final_ticket)
    
    return generated_ticket

num_of_passenger=int(input("Enter the number of passengers to generate ticket: "))
generated_ticket=generate_ticket(num_of_passenger)

if num_of_passenger<0:
    print("Invalid value entered!!")

if (num_of_passenger>=0) and  (num_of_passenger<=5):
    final_list='\n'.join(generated_ticket)
    print("Below is the list of generated ticke: \n")
    print(final_list)
    print("\n")

if num_of_passenger>5:
    final_list='\n'.join(generated_ticket[-5:])
    print("Below is the list of generated ticke: \n")
    print(final_list)
    print("\n")
    
    

