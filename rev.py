#write a program to print the reverse of a given number
num=int(input("enter number : \t"))
temp=num
rev=0
num_str=str(num)
num_dgt=len(num_str)
for i in range(num_dgt) :
    dgt=num%10
    rev=rev*10+dgt
    num=num//10
print(f"the reverse of {temp} is : {rev}")

