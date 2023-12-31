#!/usr/bin/env python
# coding: utf-8

# In[38]:


import matplotlib.pyplot as plt
import numpy as np

# -10 < x < 10 
x = np.arange(-100, 100, 0.1)

a=1
b=-6
c=-8


y = a*x**2 + b*x + c


#グラフへのプロット実行*/
plt.plot(x, y)
plt.xlim(-50,50) #x軸の範囲
plt.ylim(-50,50) #y軸の範囲
plt.minorticks_on()

plt.grid(which="major", color="black", alpha=0.7)
plt.grid(which="minor", color="gray", linestyle="--")
plt.hlines(0, -100, 100, linestyle="dashed", color="red")
plt.vlines(0, -100, 100, linestyles="dashed", colors="red")


plt.show()


# In[ ]:





# In[ ]:




