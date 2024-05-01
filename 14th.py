# Find largest word in dictionary by deleting some characters of given string


def Largest_string(dict,string):
    count=[0]*len(dict)
    for i in range(len(dict)):
        for j in range(len(string)):
            if string[j] in dict[i]:
                count[i]+=1
    
    n=max(count)
    for i in range(len(count)):
        if count[i]==n:
            print(f"Longest: {n} \nstring: {dict[i]} ")

dict=['apple','ale','yellow','apllo']
string="apiple"
Largest_string(dict,string)