# l=[[1,3],[2,2]]
# c=0
# for i in l:
#     if i!=0:
#         c+=1
# print(c)
# def mis():
#     res = 1
#     while res in l:
#         res += 1
#         return res
# print(mis(l))

#Input:[[1,3][2,2]]
#Output:[2,4]

r=2
c=2
a=[]
for i in range(0,r):
    sub=[]
    print("enter values for row",i)
    for j in range(0,c):
        print("enter values for col",j)
        ele=int(input())
        sub.append(ele)
        print(sub)
    a.append(sub)
    print(a) 

d={}
ans=[]
for i in range(0,r):
    for j in range(0,c):
        if a[i][j] not in d:
            d[a[i][j]]=1
        else:
            d[a[i][j]]+=1
            if d[a[i][j]]==2:
                ans.append(a[i][j])
print(d)
#missing
for i in range(1,r**2+1):
    if i not in d:
        ans.append(i)
print(d)
print(ans)

# PS D:\10days_Coding> python -u "d:\10days_Coding\misssing_number_and_reapeted_val.py"
# enter values for row 0
# enter values for col 0
# 1
# [1]
# enter values for col 1
# 3
# [1, 3]
# [[1, 3]]
# enter values for row 1
# enter values for col 0
# 2
# [2]
# enter values for col 1
# 2
# [2, 2]
# [[1, 3], [2, 2]]
# {1: 1, 3: 1, 2: 2}
# {1: 1, 3: 1, 2: 2}
# [2, 4]
# PS D:\10days_Coding> 
    
        
            
        
    
