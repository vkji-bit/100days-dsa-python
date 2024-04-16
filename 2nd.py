#Day 2 to reverse a integer like 1234 to 4321

n=int(input("Enter a number: "))
sum=0
r=0
while(n!=0):
    r=n%10
    sum=sum*10+r
    n//=10 #Everytime n enters it gets dived by 10 
    
print("Result: ",sum)

#also by converting into string