# Count the number of time string is repeating
#day 13

def Count(string):
    str1=[]
    for i in string:
        if i not in str1:
            str1.append(i)
    

    for i in range(len(str1)):
        count=0
        for j in string:
            if str1[i]==j:
                count+=1
            else:
                continue
        print(f"{str1[i]} count : {count}")

string=input("Enter the string: ")
Count(string)