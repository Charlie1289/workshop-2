# Polynomial coefficients
a0 = 1
a1 = -2
a2 = 4.6
a3 = 0.2

# Point at which we evaluate the derivative
x0 = 3.1


p_prime =a1+2*a2*x0+3*a3*x0**2

a=[a0,a1,a2,a3]
n=(0,1,2,3)
y=0
for element in a:
 p_prime+=element*x0**n[y-1]*y


eval_derivative(a, x0,m)
for element in a:
 p_prime+=element*x0**n[y-1]*y

# This will be True if the code is correct
print(p_prime)
print(p_prime == 32.286)
