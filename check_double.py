'''
Write a python function, check_double(number) which accepts a whole number and returns True if it satisfies the given conditions.

The number and its double should have exactly the same number of digits.

Both the numbers should have the same digits ,but in different order.
'''

def check_double(number):
    double=0
    double=2*number
    if len((str)(double))!=len((str)(double)):
       return(False)
    
    num=number
    list1=[]
    while(num>0):
       list1.append(num%10)
       num=(int)(num/10)
       
    num=double      
    list2=[]
    while(num>0):
       list2.append(num%10)
       num=(int)(num/10)
    
    list1.sort()
    list2.sort()
    if list1==list2:
       return(True)
    else:
       return(False)

#Provide different values for number and test your program
print(check_double(125874))
