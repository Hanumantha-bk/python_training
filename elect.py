n=6
list=[1,1,2,2,2,3,3]
d={}
for ele in list:
    if ele in d:
        d[ele]+=1
    else:
        d[ele]=1
win=max(d,key=d.get)
print(win)