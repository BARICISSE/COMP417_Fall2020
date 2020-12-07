# Starter code for those trying to use LQR. Your
# K matrix controller should come from a call to lqr(A,B,Q,R),
# which we have provided. Below this are "dummy" matrices of the right
# type and size. If you fill in these with values you derive by hand
# they should work correctly to call the function.

# Here is the provided LQR function
import scipy.linalg
import numpy as np
import math
def lqr( A, B, Q, R ):	
	x = scipy.linalg.solve_continuous_are( A, B, Q, R )
	k = np.linalg.inv(R) * np.dot( B.T, x )
	return k

# FOR YOU TODO: Fill in the values for A, B, Q and R here.
# Note that they should be matrices not scalars. 
# Then, figure out how to apply the resulting k
# to solve for a control, u, within the policyfn that balances the cartpole.
# A = np.array([[ 1, 0, 0, 0 ],
# 	          [ 0, 1, 0, 0 ],
# 	          [ 0, 0, 1, 0 ],
#               [ 0, 0, 0, 1 ]] )

# B = np.array( [[1, 1, 1, 1 ]] )
# B.shape = (4,1)

# Q =  np.array([[ 1, 0, 0, 0 ],
#        	       [ 0, 1, 0, 0 ],
# 	           [ 0, 0, 1, 0 ],
#                [ 0, 0, 0, 1 ]] )

# R = np.array([[100]])
g = 9.82
m = 0.5
M = 0.5
l = 0.5
b = 0.1

const = 4*M+m
A1 = -4*b/const
A2 = 3*m*g/const
A3 = 6*b/(l*const)
A4 = -6*g*(M+m)/(l*const)
A = np.array([[ 0, 1, 0, 0 ],
	      [ 0, A1, 0, A2 ],
	      [ 0, A3, 0, A4 ],
          [ 0, 0, 1, 0 ]] )

B1 = 4/const
B2 = -6/(const*l)
B = np.array( [[0, B1, B2, 0]] )
B.shape = (4,1)

Q =  np.array([[ 1, 0, 0, 0 ],
       	       [ 0, 35, 0, 0 ],
	           [ 0, 0, 500, 0 ],
               [ 0, 0, 0, 100]] )


R = np.array([[5]]) 
print( "A holds:",A)
print( "B holds:",B)
print( "Q holds:",Q)
print( "R holds:",R)
    
# Uncomment this to get the LQR gains k once you have
# filled in the correct matrices.
k = lqr( A, B, Q, R )
print( "k holds:",k)
# k = [[  0.4472136    2.96508445  -9.35417298 -16.36231334]]