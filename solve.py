import numpy as np 

# 3y = x 
# x + y = 100
A = np.array([ [1 ,1] , [-1 ,3] ])
B = np.array([100 , 0 ])

x = np.linalg.solve(A, B)
print(f"x  = {x[0]} \n y = {x[1]}")