# # list=[1, 1, 2, 2, 2, 3, 3]
# # d={}
# # for ele in list:
# #     if ele in d:
# #         d[ele]+=1
# #     else:
# #         d[ele]=1
# # win=max(d,key=d.get)
# # print(win)

# # a=[1, 1, 2, 2, 2, 3, 3]
# # d={}
# # for i in a:
# #     if i not in d:
# #         d[i]=1
# #     else:
# #         d[i]=d[i]+1

# #No of Votes
# # n=int(input())

# # #No of Votes For Each
# # a=list(map(int,input().split()))

# # Map Ex:3 4
# # a,b=map(int,input(),split())

# #k=lamda x:x%10
# # k(123)

# n=int(input())
# arr=list(map(int,input().split()))
# d={}
# if n==1:
#     print(arr[0])
# else:
#     for i in arr:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
# ans=-1
# vals=list(d.items())
# print(vals)
# vals.sort(reverse=True,key=lambda x:x[1])
# #(1,2) (2,3) (3,3)
# print(vals)
# if len(vals)==1:
#     ans=vals[0][0]
# else:
#     if vals[0][1]==vals[1][1]:
#         ans=-1
#     else:
#         ans=vals[0][0]
# print(ans)