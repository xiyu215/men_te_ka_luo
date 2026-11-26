# ps={2:1/36,3:2/36,4:3/36,5:4/36,6:5/36,7:6/36,8:5/36,9:4/36,10:3/36,11:2/36,12:1/36}

# V=0
# for x,p in ps.items():
#     V += x*p
# print(V)


import numpy as np
def sample (decise=2):
    x=0
    for _ in range(decise):
        x+=np.random.choice([1,2,3,4,5,6])
    return x

trail=100000
V,n=0,0
samples=[]
for _ in range(trail):
    s=sample()
    n+=1
    V+=(s-V)/n
print(V)