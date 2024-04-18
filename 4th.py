#Container With Most Water Day 4

# Keep two index, first = 0 and last = n-1 and a value max_area that stores the maximum area.
# Run a loop until first is less than the last.
# Update the max_area with maximum of max_area and min(array[first] , array[last])*(last-first)
# if the value at array[first] is greater the array[last] then update last as last – 1 else update first as first + 1
# Print the maximum area.


Cont=[]
n=int(input("Enter number of Poles: "))
for i in range(n):
    Cont.append(int(input(f"Enter {i+1} element: ")))

print("your list: ",Cont)

def maxarea(A):
    front=0
    rear=len(A)-1
    area=0
    while front<rear:
        area=max(area,min(A[front],A[rear])*(rear-front))

    if A[front]<A[rear]:
        front+=1
    else:
        rear-=1
    return area

maxarea(Cont)