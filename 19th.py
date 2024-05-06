# Find the largest word in a dictionary
# 18day

def long(list):
    for i in list:
        for j in list:
            if len(i)<len(j):
                i,j=j,i
    a=list[len(list)-1]
    return a

List=[]
n=int(input("enter number list item: "))
for i in range(n):
    List.append(input("enter list item: "))

print(f"longest : {long(List)}")