n=int(input())
temp=n
rev=0
num_str=str(n)
num_dgt=len(num_str)
for i in range(num_dgt) :
    dgt=n%10
    rev=rev*10+dgt
    n//=10
if temp==rev:
    print(temp,"its palindrome")
else:
    print(temp,"its not palindrome")
    
# 121
# 121 its palindrome