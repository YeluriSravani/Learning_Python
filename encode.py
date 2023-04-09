#Write python function, sms_encoding() which accepts a sentence and converts it into an abbreviated sentence to be sent as SMS and returns the abbreviated sentence. 

#Rules are as follows: 
#a. Spaces are to be retained as is 
#b. Each word should be encoded separately

#If a word has only vowels then retain the word as is

#If a word has a consonant (at least 1) then retain only those consonants

def sms_encoding(data):
    #start writing your code here
    vowels = "AaEeIiOoUu"
    encode=''
    flag='n'
    list=data.split(' ')
    for word in list:
        if flag=='y':
           encode+=' '
        vow=[each for each in word if each in vowels]
        if len(vow)==len(word):
           encode+=word
        else:
           cons=[each for each in word if each not in vowels]
           for i in cons:
               encode+=i
        flag='y'       
    return encode
