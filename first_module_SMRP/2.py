def larger_root(p,q):
    return (-p+(p*p-4*q)**0.5)/2

def smaller_root(p,q):
    return (-p-(p*p-4*q)**0.5)/2

def discriminant(a,b,c):
    return b*b-4*a*c

p=float(input())
q=float(input())
print(f"{discriminant(1,p,q)}\n{larger_root(p,q)} {smaller_root(p,q)}")