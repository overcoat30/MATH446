import numpy as np
import matplotlib.pyplot as plt

#from program 4.2 (houseqr.m)
def hogs(A):
    m, n = A.shape
    Q = np.eye(m)

    for i in range(min(n, m-1)):
        x = A[i:,i]
        w = np.zeros(m-i)
        w[0] = -np.sign(x[0])*np.linalg.norm(x)
        v = w-x

        H = np.eye(m)
        H[i:,i:] = np.eye(m-i) - 2*np.outer(v,v)/np.dot(v,v)

        Q = np.dot(Q,H)
        A = np.dot(H,A)

    R = A
    return Q,R


def back_sub(R,d):
    n = len(d)
    c = np.zeros(n)

    for i in range(n-1,-1,-1):
        c[i] = (d[i] - np.dot(R[i,i+1:],c[i+1:]))/R[i,i]

    return c


def ls_qr(A,b):
    m,n = A.shape
    Q,R = hogs(A.astype(float))
    d = np.dot(Q.T,b)
    c = back_sub(R[:n,:n],d[:n])
    return c


def rmse(A,c,b):
    r = b - np.dot(A,c)
    return np.linalg.norm(r)/np.sqrt(len(b))


def g(t):
    return np.exp(np.sin(t-1))


m = 60
i = np.arange(1,m+1)
t = 2*np.pi*i/m
y = g(t)

#add noise
np.random.seed(0)
y_noisy = y*(1+0.1*np.random.randn(m))


#b
A1 = np.column_stack([t**k for k in range(7)])
c = ls_qr(A1,y_noisy)
rmse1 = rmse(A1,c,y_noisy)

print("Polynomial coefficients")
for k in range(7):
    print("c",k+1,"=",c[k])
print("RMSE =",rmse1)


#c 
A2 = np.column_stack([np.ones(m),np.cos(t),np.sin(t),
                      np.cos(2*t),np.sin(2*t)])
d = ls_qr(A2,y_noisy)
rmse2 = rmse(A2,d,y_noisy)

print("\nTrig coefficients")
for k in range(5):
    print("d",k+1,"=",d[k])
print("RMSE =",rmse2)


#d 
tt = np.linspace(t[0],t[-1],500)

y1 = np.column_stack([tt**k for k in range(7)])
y1 = np.dot(y1,c)

y2 = np.column_stack([np.ones(len(tt)),np.cos(tt),np.sin(tt),
                      np.cos(2*tt),np.sin(2*tt)])
y2 = np.dot(y2,d)

plt.plot(t,y_noisy,'ko',label='Noisy data')
plt.plot(tt,y1,'b-',label='Polynomial')
plt.plot(tt,y2,'r--',label='Trigonometric')

plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()

