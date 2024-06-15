# l=[1,2,3]
# print(sum(l))

#Input:[1,2,3]
#Output:1+2+3=6
#Input:[10,21,31]
#Output:11+22+33=66

def enc(n):
    #maximum and count
    mx=-999
    c=0
    ans=0
    while n>0:
        dig=n%10
        if dig>mx:
            mx=dig
        c=c+1
        n=n//10
        
    #arrange
    while c>0:
        ans=ans*10+max
        c=c-1
        
f_ans=0   
ans=0    
a=list(map(int,input().split()))
for i in a:
    ans=enc(i)
    f_ans+=ans
print(f_ans)
        
        
        
        
        
    
