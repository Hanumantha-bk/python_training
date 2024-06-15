# # # tos=int(input())
# # # size=int(input())
# # # dis=list(map(int,input().split()))
# # dis=[1,2,3,4,5]
# # d=[]
# # for i in range(len(dis)-1):
# #     d.append([dis[i],dis[i+1]])
# # print(d)
# # a=max(d)
# # print(a)
# # # print(d)


inp1=int(input())
inp2=int(input())
arr=list(map(int,input().split()))

mx=-1
for i in range(0,len(arr)-inp2+1):
    temp=arr[i:inp2]
    k,s=1,0
    for j in temp:
        s+=(j*k)
        k+=1
    if s>mx:
        mx=s
print(mx)


# PS D:\10days_Coding> python -u "d:\10days_Coding\basket.py"
# 5
# 2
# 1 2 3 4 5
# 5
# PS D:\10days_Coding> 
