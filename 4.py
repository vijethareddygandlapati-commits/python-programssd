mylist=input("enter a number separated by space:")
mylist=list(map(int,mylist.split()))
sum=0
for number in mylist:
    sum+=number
    print("the sum of the number is:",sum)


