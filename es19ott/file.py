import numpy as np
import matplotlib.pyplot as plt

arrayx=np.array([34,5,67,1])
arrayy=np.arange(0,5)

plt.plot(arrayx,arrayy, 'o-', color='salmon', label='grafico array')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
