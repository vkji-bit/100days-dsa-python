# Distinct Palindromic Substrings
#day 17

def Palindrone(string):
    palindrone=set()
    for i in range(len(string)):
        for j in range(len(string)):
            substring=string[i:j+1]
            if substring==substring[::-1]:
                palindrone.add(substring)
    return palindrone

val=input("Enter palindrone: ")
print(Palindrone(val))