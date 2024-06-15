# Diwali Contest :
pr=int(input())
tot=int(input())
c=0
s=0
rt=4*60-tot
for i in range(1,pr+1):
    if s<rt:
        s=s+5*i
    c+=1
print(c)
