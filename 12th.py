# Count ways to increase LCS length of two strings by one
# two string will be pass if the string2 have elements in string1 the result will be the common element

def substring(string1,string2):
    str1=''
    for i in string1:
        for j in string2:
            if j==i:
                str1=str1+j
    return str1

string1=input("String 1: ")
string2=input("String 2: ")

print("result",len(substring(string1,string2)))