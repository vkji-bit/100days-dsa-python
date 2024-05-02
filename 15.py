# Input: words[] = {“baa”, “abcd”, “abca”, “cab”, “cad”}
# Output: Order of characters is ‘b’, ‘d’, ‘a’, ‘c’
#day 15 
# Given a sorted dictionary of an alien language, find the order of characters

def alien_ditect(word):
    string=[]
    detect=[]
    for i in range(len(word)):
        string=word[i]
        for j in range(len(string)):
            if string[j] not in detect:
                detect.append(string[j])
            else:
                continue
    print(detect)
            
words = ["baa", "abcd", "abca", "cab", "cad"]
alien_ditect(words)