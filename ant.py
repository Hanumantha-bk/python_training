# a=int(input())
# b=list(map(int,input().split()))
# def ant(n):
#     for i in range(1,n):
#         if(b[i]==a):
#             return -1
#         else:
#             return 1
# print(ant(a))


step=int(input())
a=list(map(int,input().split()))
sp=0
ans=0
for i in a:
    sp=sp+i
    if sp==0:
        ans=ans+1
print(ans)

# PS D:\10days_Coding> python -u "d:\10days_Coding\ant.py"
# 5
# 1 -1 1 -1 1
# 2
# PS D:\10days_Coding> 
            
    

        
   