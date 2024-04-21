#Merge Intervals that means: if list contains [[3,5],[3,6],[7,9]]
#than the output should be  [3,9]


arr=[[3,4],[5,8],[4,8],[7,10],[1,5,11]]

list=[]
#every elements keeps added in list
for i in arr:
    start=0
    end=len(i)-1
    list.append(i[start])
    list.append(i[end])

#used for sorting the array
list.sort()

print(f"interval: [{list[0]},{list[len(list)-1]}]")
            



