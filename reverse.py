# Question:You are given a string s. You need to reverse the string.

# Code: 
def reverseWord(str):
        
        return str[::-1]

def reverseWord(str):
        
        new_str = ''
        for i in range(len(str)-1,-1,-1):
            new_str+=str[i]
        return new_str
            

