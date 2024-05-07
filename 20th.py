# Reduce the string by removing K consecutive identical characters
# Input: K = 2, str = “geeksforgeeks” 
# Output: gksforgks 
# Input: K = 2, str = “aaabbcddd” 
# Output: acd

def remove(k,string):
    string_convert=list(string)
    dupli=[]
    for i in range(len(string_convert)):
        if string_convert[i] not in dupli:
            dupli.append(string_convert[i])


    for i in range(len(dupli)):
        count=0
        for j in range(len(string_convert)):
            if dupli[i]==string_convert[j]:
                count+=1
                if count==k:
                    string_convert[j]=''
                    string_convert[j-1]=''
   

    for x in range(len(string_convert)):
        print(string_convert[x],end="")

af="aaabbcddd"

remove(2,af)