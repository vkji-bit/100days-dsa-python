# Product of Array Except Self input= [1,2,3] output=[6,3,2]
# day 7 

def prod(arr):
    
    product=[]
    for i in arr:
        value=1
        for j in arr:
            if i==j:
                continue
            else:
                value=value*j
        product.append(value)

    print(product)
arr=[]
def Input_arr():
    
    n=int(input("Enter how many data: "))
    for i in range(n):
        arr.insert(i,int(input(f"enter {i+1} ele: ")))

    print(arr)

Input_arr()
prod(arr)