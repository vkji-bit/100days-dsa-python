#finding the maximun value in array
#day 8
arr=[1,2,5,6,12,25,10,11]
value=0
for i in arr:
    if value>i:
        continue
    else:
        value=i
print("maximun value: ",value)