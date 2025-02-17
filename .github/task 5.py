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
y=10000000000000
count=0
z=0
z1=0
Pa=3664186.998
while V<10**(-3):
    v.append(V)
    P.append((R*T)/(V-b)-(a/(V**2)))
    y = ((R * T) / (V - b) - (a / (V ** 2)))
    z+=(10**(-6))*y
    z1+=(10**(-6))*Pa
    V+=10**(-6)
plt.subplot(2, 1, 1)
plt.plot(v, P)
plt.title('T=-130')
print(z)

print(z1)
#print (Q[0], q[0])
#print (Q[1], q[1])
plt.show()