import lcapy as lc
from lcapy.discretetime import z
import matplotlib.pyplot as plt
import numpy as np
N = 20
#--------------------- Put the Z transform X(z) here
X=2*z/(2*z-1)
#---------------------
#X=z/(z-1)
#X=1 +2/z -1/z**2+5/z**3 -5/z**9
#X = 1 + .00001/z # Ejemplo 1. 𝛿[𝑛]
#X = 1 +2/z -1/z**2+5/z**3 -5/z**9 # Sequence [1,2,-1,5]
#X = (1 -1/z +2/z**2+6/z**3) # Secuencia [1,-1,2,6] desplazada 3 a la derecha
#X=z/(z-1) # Ejemplo 2. Escalón unitario 𝑢[𝑛]
#X=1/(z-1) # z**(-1)*z/(z-1) Ejemplo 2. Escalón unitario 𝑢[𝑛] desplazado 1 lugar
#X=1/(z*(z-1)) # z**(-2)*z/(z-1) Ejemplo 2. Escalón unitario 𝑢[𝑛] desplazado 2 lugares
#X=2*z/(2*z-1) # Ejemplo 3. Secuencia de potencias 𝑎**(−𝑛)𝑢[𝑛] 𝑥[𝑛]={𝑎−𝑛 para 𝑛=0,1,2,...,∞} con a = 2
#X=z/(z-2) # Ejemplo 3. Secuencia de potencias 𝑎**(−𝑛)𝑢[𝑛] con a = 1/2
#X=z/(z-1)**2 # Ejemplo 4. Secuencia nu[n] 𝑛𝑢[𝑛]=[0,1,2,3,4,...]
#X=(z**2-1)/((z-.9)*(z+.1))
#X = 1/(z-2) -1/(z-1)
#X=1/(1-1/z+.8/z*1/z)
#X=(z/(z-1))/(1-1/z+.8/z**2)
x_n=X.IZT()
seq = x_n.seq((0, N))
float_seq = [float(expr.value) for expr in seq]
fig=plt.figure(figsize=(12,4), dpi= 100)
for i,val in enumerate(float_seq):
    plt.vlines(i, 0, val, color='red')
plt.plot (float_seq,"go")
plt.xlabel('n', fontsize=14)
plt.ylabel('sequence [n]', fontsize=14)
plt.title('Inverse Z-Transform', fontsize=14)
plt.grid()
