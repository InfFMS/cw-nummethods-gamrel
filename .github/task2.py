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
while V<10**(-3):
    v.append(V)
    P.append((R*T)/(V-b)-(a/(V**2)))
    y1=y
    y = ((R * T) / (V - b) - (a / (V ** 2)))
    if y1 < y and count==0:
        Q.append(y)
        q.append(V)
        count += 1
    if count != 0 and y1 > y:
        Q.append(y)
        q.append(V)
        count -= 1
    V+=10**(-7)
plt.subplot(2, 1, 1)
plt.plot(v, P)
plt.title('T=-130')
print (Q[0], q[0])
print (Q[1], q[1])
plt.show()