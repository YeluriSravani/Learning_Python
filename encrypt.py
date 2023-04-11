#Write a python function, encrypt_sentence() which accepts a message and encrypts it based on rules given below and returns the encrypted message.
#Words at odd position -> Reverse It
#Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change
#lex_auth_01269444195664691284
def encrypt_sentence(sentence):
    #start writing your code here
    list=[]
    flag='n'
    encrypt=''
    vowel=''
    word1=''
    list=sentence.split(' ')
    for word in list:
        if flag=='y':
           encrypt+=' '
        if (list.index(word)+1)%2==0:
           word1=''
           vowel=''
           for i in range(0,len(word)):
               if word[i] in ['a','e','i','o','u']:
                  vowel+=word[i]
               else:
                  word1+=word[i]
           
           encrypt+=word1+vowel
        else:
           encrypt+=word[::-1]
        
        flag='y'
    return encrypt 

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
