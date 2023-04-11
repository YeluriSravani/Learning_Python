#Write a python program to display all the common characters between two strings. Return -1 if there are no matching characters.
#lex_auth_012693825794351104168
def find_common_characters(msg1,msg2):
    #pass #Remove pass and write your logic here
    common=''
    for i in msg1:
        for j in msg2:
            if i==j:
               if i not in common:
                  common+=i
               else:
                  continue
            else:
               continue
    
    if common=='':
       common=-1
    return common

#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
