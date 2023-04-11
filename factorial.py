#Write a Python function to find all the Strong numbers in a given list of numbers.
#Write another function to find and return the factorial of a number. Use it to solve the problem.

#Example:
#A number is considered to be a Strong number if sum of the factorial of its digits is equal to the number itself. 
#145 is a Strong number as 1! + 4! + 5! = 145. 


import math

def factorial(number):
    #pass #remove pass and write your logic to find and return the factorial of given number
    if number==0:
       return 1
    
    i=0
    fact=0
    while(number>0):
       i=number%10
       fact+=math.factorial(i)
       number=(int)(number/10)
       
    return(fact)
    


def find_strong_numbers(num_list):
    #pass #remove pass and write your logic to find and return the list of strong numbers from the given list
    strong_list=[]
    for i in num_list:
        if i==factorial(i):
           strong_list.append(i)
    
    return strong_list


num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
