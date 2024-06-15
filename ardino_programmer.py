# n=list(map(int,input().split()))
# sum=0
# for i in n:
#     sum+=i
# print(sum)


a=list(map(int,input().split()))
max=-1
s=0
for i in a:
    s=s+i
    if s>max:
        max=s
print(max)

#1) PS D:\10days_Coding> python -u "d:\10days_Coding\ardino_programmer.py"
# 1 -2 3 4
# 6
# PS D:\10days_Coding> 

# 2)PS D:\10days_Coding> python -u "d:\10days_Coding\ardino_programmer.py"
# 1 2 6 -5
# 9
# PS D:\10days_Coding> 


