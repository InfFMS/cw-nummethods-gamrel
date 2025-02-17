import matplotlib.pyplot as plt

a = 0.1382
b = 3.19*10**-5
R = 8.314
V=b+10**(-5)
T=-140+273.15
v = []
P = []
while V<0.3*10**(-3):
    v.append(V)
    P.append(R * T / (V - b) - a / V ** 2)
    V+=10**(-7)
plt.plot(v, P)
plt.title('T=-140')
T=-130+273.15
V=b+10**(-5)
v=[]
P=[]
while V<0.3*10**(-3):
    v.append(V)
    P.append(R * T / (V - b) - a / V ** 2)
    V+=10**(-6)
plt.plot(v, P)
plt.title('T=-130')
T=-120+273.15
V=b+10**(-5)
v=[]
P=[]
while V<0.3*10**(-3):
    v.append(V)
    P.append(R * T / (V - b) - a / V ** 2)
    V+=10**(-7)

plt.plot(v, P)
plt.title('T=-120')
T=-110+273.15
V=b+10**(-5)
v=[]
P=[]
while V<0.3*10**(-3):
    v.append(V)
    P.append(R * T / (V - b) - a / V ** 2)
    V+=10**(-7)

plt.plot(v, P)
plt.title('T=-110')
T=-100+273.15
V=b+10**(-5)
v=[]
P=[]
while V<0.3*10**(-3):
    v.append(V)
    P.append(R*T/(V-b)-a/V**2)
    V+=10**(-7)

plt.plot(v, P)
plt.title('T=-100')
plt.show()