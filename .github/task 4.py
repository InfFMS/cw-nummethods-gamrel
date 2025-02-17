import matplotlib.pyplot as plt
a = 0.1382
b = 3.19*10**(-5)
R = 8.314
V=b+10**(-5)
T=-130+273.15
v = []
P = []
Q=[]
q=[]
y=1000000000
x=1111111111
count=0
Pa=3664186.998
while V<0.1*10**(-3):
    v.append(V)
    P.append((R*T)/(V-b)-(a/(V**2)))
    y = ((R * T) / (V - b) - (a / (V ** 2)))
    x1=x
    x=(y-Pa)
    if x1<x:
        count=V
    V+=10**(-8)
V+=10**(-8)*3
print(V)
x=1111111111
y=1000000000
while V<10**(-3):
    v.append(V)
    P.append((R*T)/(V-b)-(a/(V**2)))
    y = ((R * T) / (V - b) - (a / (V ** 2)))
    x1=x
    x=(y-Pa)
    if x1<x:
        count=V
    V+=10**(-7)
print(V)
plt.subplot(2, 1, 1)
plt.plot(v, P)
plt.title('T=-130')
plt.show()