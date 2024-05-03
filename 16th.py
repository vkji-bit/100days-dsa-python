# Longest Valid Parentheses
# day 16

def longest_parenthesis(str):
    string=[]
    for i in range(len(str)):
        if str[i]=='(':
            string.append(str[i])
            for j in range(i,len(str)):
                if str[j]==')':
                    string.append(str[j])
                    break
    count=int(len(string)/2)
    print(f"{count} : pairs of () ")




string="()(()))()))"
longest_parenthesis(string)