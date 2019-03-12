import math

n=10
c=list(range(2,n))

#newC = [aC - c[0] for aC in c]

print(c)



def foncp(p):
    if p>3:
        return None
    else:
        d=list(range(2*p,n,p))
        print(d)
        print(len(d))
        for i in range(len(d)):
            print(c)
            c.remove(d[i])
        print(c)

        PP=list(range(1))
        print(PP)
        for i in range(len(c)):
            if c[i]>p:
                PP.extend([c[i]])
                print(PP)
        p=PP[1]
        print(p)
        return foncp(p)

pp = 2

foncp(pp)
