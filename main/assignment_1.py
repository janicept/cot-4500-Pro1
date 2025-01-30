#Approximation algorithm, root 2

# Change starting point here.
x0 = 1.5 

# Change tolerance here.
tol = 0.000001 

iter = 0
diff = x0
x = x0

print("Approximation algorithm, root 2 results:")
print(f"{iter}: {x}")
while diff >= tol:
   iter += 1
   y = x  
   x = (x / 2) + (1 / x)
   print(f"{iter}: {x}")
   diff = abs(x - y)

print(f"\nConvergence after {iter} iterations")

print()

#________________________________
#Bisection Method

# Change equation here
def f(x):
    return x**3 - 4*x - 9

# Change tolerance here.
tol = 0.000001

# Change interval here.
left = -4
right = 7
a = left
b = right

#Change max iterations here
max = 100

def bisection_method(f, a, b, tol, max):
    i = 0

    while abs(b - a) > tol and i < max:
        i += 1
        p = (a + b) / 2  # Midpoint of the interval
        
        if f(p) == 0:  # If we found the root
            return p, i
        
        # Narrow down the interval based on the signs of f(a) and f(p)
        if (f(a) < 0 and f(p) > 0) or (f(a) > 0 and f(p) < 0):
            b = p  # Root lies in the left half
        else:
            a = p  # Root lies in the right half
            
    # Return the root approximation
    return (a + b) / 2, i

root, iterations = bisection_method(f, a, b, tol, max)

print("Bisection Method result:")
if root is not None:
    print(f"Root found: {root}")
    print(f"Converged in {iterations} iterations.")
else:
    print("Bisection method failed.")
    
print()

#________________________________
#Fixed Point Operation

# Change equation here.
def g(x):
    return (10 - x**2)**(1/3)

# Change tolerance here.
tol = 0.000001

# Change initial approximation here.
p0 = 3

#Change max iterations here
n0 = 100

def fixed_point_iteration(g, p0, tol, n0):
    
    i = 1
    p = p0  # Starting value
    print("Fixed Point Operation result:")
    
    while i <= n0:
        p_next = g(p)  # Apply the fixed-point iteration

        # Check if the change is less than the tolerance
        if abs(p_next - p) < tol:
            print(f"Success: p = {p_next}")
            return  # Exit when convergence is achieved

        p = p_next  # Update the approximation for the next iteration
        i += 1

    # If we reach max iterations without convergence
    print("Failure: Max iterations reached without convergence.")

# Call the fixed-point iteration method
fixed_point_iteration(g, p0, tol, n0)

print()

#________________________________
#Newton-Raphson Method

import sympy as sp

# Change interval here.
a, b = -4, 7
initial_guess = (a + b) / 2  # Midpoint

# Change tolerance here
tol = 1e-4 
x = sp.Symbol('x')

# Change equation here
f = x**3 + 4*x**2 - 10

#Change max iterations here
max_iter = 100

f_prime = sp.diff(f, x)
f_func = sp.lambdify(x, f, 'numpy')
f_prime_func = sp.lambdify(x, f_prime, 'numpy')

def newton_raphson(func, func_prime, initial_guess, tol, max_iter):
    x_current = initial_guess
    for i in range(max_iter):
        f_value = func(x_current)
        f_prime_value = func_prime(x_current)
        
        if f_prime_value == 0:
            print("Derivative is zero. No solution found.")
            return None, i
        
        x_next = x_current - f_value / f_prime_value
        
        if abs(x_next - x_current) < tol:
            return x_next, i + 1
        
        x_current = x_next
    
    print("Maximum iterations reached without convergence.")
    return x_current, max_iter

root, iterations = newton_raphson(f_func, f_prime_func, initial_guess, tol, max_iter)
print("Newton-Raphson Method results:")

if root is not None:
    print(f"Root: {root:.4f}, found in {iterations} iterations.")
else:
    print("Solution could not be found.")
