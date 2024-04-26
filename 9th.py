# Group Anagrams in arrays like list =[12,43,34,21]
# output =[[12,21],[43,34]]

def reverse(num,num2):
    if num==num2:
        return False
    elif num%10==int(num2/10):
        return True
    else:
        return False



arr=[11,34,32,56,63,49,20]
newarr=[]
for i in arr:
    for j in arr:
        if reverse(i,j):
            n=[i,j]
            newarr.append(n)
        else:
            continue

print(newarr)