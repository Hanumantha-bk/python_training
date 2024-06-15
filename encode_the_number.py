# input:167
# output:13649
n=167
def sod(n):
    c=0
    while n>0:
        c+=1
        n//=10
    return c

def rev(n):
    ans=0
    while n>0:     #167#16#1
        dig=n%10   #10#7#6#1
        sq=dig**2  #49#36#1
        sod_sq=sod(sq) #2#2#1
        ans=ans*(10**sod_sq)+sq
        n=n//10   
    return ans
ans=rev(n)

def rev2(n):
    ans2=0
    while n>0:
        dig=n%10
        ans2=ans2*10+dig
        n//=10
    return ans2
print(rev2(ans))
        