# n=6 28 66 120 190 276 ?
# an^2+bn+c
def seq(n):
    d=[]
    for n in range(1,n+1):
        a=2*n*(4*n-1)
        d.append(a)
    return d
num=7
sq=seq(num)
print(sq)
