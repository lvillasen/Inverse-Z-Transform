import lcapy as lc
from lcapy.discretetime import z
import matplotlib.pyplot as plt
import numpy as np
N = 20
#--------------------- Put the Z transform X(z) here
X=2*z/(2*z-1)
#---------------------
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
