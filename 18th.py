#Creating non duplicate set
#day 18th
def duplicate(string):
    final=[]
    for i in range(0,len(string)):
        store=string[i]
        count=len(store)
        for j in range(0,len(string)):
            store1=string[j]
            if string[i]==string[j]:
                continue
            else:
                for k in range(len(store1)):
                    if k+count>len(store1):
                        continue
                    else:
                        if store==None or store1==None:
                            continue
                        else:
                            if store==store1[k:k+count] :
                                # final.remove(string[i])
                                final.append(store)
    final=set(final)

    seting=[]
    for value in string:
        if value in final:
            continue
        else:
            seting.append(value)
                    
    return seting



Input=[]
num=int(input("Enter number of elements: "))
for i in range(num):
    Input.append(input("Enter strings: "))
print(Input," has been corrected",duplicate(Input))
