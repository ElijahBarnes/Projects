from math import*

r=[2]
n=10000
c=0
q=r[c]
for s in range (3,n):
    c=0
    q=r[c]
    while q==r[c]:
        if s%q == 0:
            break
        else:
            if len(r)==c+1: 
                r.append(s)
                break
            else:
                c=c+1
                q=r[c]
                
        

print (r)

