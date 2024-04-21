# Longest Subarry Without Repeating Characters

arr=[]
n=int(input("Enter how many data: "))
for i in range(n):
    arr.insert(i,int(input(f"enter {i+1} ele: ")))

print(arr)

subarr=[]
for ele in range(n):
    if arr[ele] not in subarr:
        subarr.insert(ele,arr[ele])
    else:
        continue

print(subarr)
        
