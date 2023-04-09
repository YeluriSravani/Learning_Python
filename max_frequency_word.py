#Write a python program that accepts a text and displays a string which contains the word with the largest frequency in the text and the frequency itself separated by a space.

#Rules:

#The word should have the largest frequency.

#In case multiple words have the same frequency, then choose the word that has the maximum length.

#Assumptions:

#The text has no special characters other than space.

#The text would begin with a word and there will be only a single space between the words.

#Perform case insensitive string comparisons wherever necessary.


def max_frequency_word_counter(data):
    word=""
    frequency=0

    #start writing your code here
    check=''
    list=[]
    check=data.lower()
    list=check.split()
    unique=set(list)
    dict={}
    for i in unique:
        freq=0
        freq=(check.count(i+' '))+(check.count(' '+i))-(check.count(' '+i+' '))
        dict.update({i:freq})
        
    temp_key=''
    temp_key=max(dict, key=dict.get)
    frequency=dict.get(temp_key)
    list1=[k for k, v in dict.items() if v == frequency]
    word=max(list1, key=len)
    #Populate the variables: word and frequency

    print(word,frequency)
    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    #print(word,frequency)
    

#Provide different values for data and test your program.
data="data-Listen to the big clock Tick tock tick"
max_frequency_word_counter(data)
