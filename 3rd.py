#3rd day ::  Checking a number is palindrone or not::

n=int(input("enter number: "))
temp=n
sum=0
r=0
while n!=0:
    r=n%10
    sum=sum*10+r
    n//=10
    
if temp==sum:
    print("Result Palindrone: ",sum)
else:
    print(f"not palindrone {temp} != {sum}")