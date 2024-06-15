def search():
    if(s>e):
        return -1
    m=s+(e-s)/2
    if(arr[m]==tar):
        return search(arr,tar,s,m-1)
    return search(arr,tar,m+1,e)
list=[1,2,3,4,5]
tar=4
arr=[]
s=0
e=0
print(search(arr,tar,s,e))

    