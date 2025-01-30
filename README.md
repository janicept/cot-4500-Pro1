Numerical Methods for Root Finding

This repository contains Python implementations of different numerical methods for finding roots of equations. The methods included are:

1. Approximation Algorithm for Root 2 

2. Bisection Method

3. Fixed Point Iteration Method

4. Newton-Raphson Method

Methods Overview:

Approximation Algorithm (Root 2)
This method is used to approximate the square root of 2. It starts with an initial guess and applies an iterative method to approximate the root of the equation.

Bisection Method
The bisection method is used to find the root of a function in a given interval. It repeatedly bisects the interval and selects the subinterval where the root lies, refining the estimate until convergence.

Fixed Point Iteration
Fixed Point Iteration is used to find the root of an equation by iterating with an equation that can be rearranged into the form x=g(x). The method stops when the difference between successive iterations is less than a specified tolerance. 

Newton-Raphson Method
The Newton-Raphson Method is an iterative method that uses the function and it's derivative to find the root of an equation. This implementation uses symbolic differentiation with the sympy library.

1. Approximation Algorithm (Root 2)
To change the initial guess or tolerance for the approximation, modify the following variables:
x0 = 1.5       # Starting point for the approximation
tol = 0.000001 # Tolerance level for stopping criteria

2. Bisection Method
To change the function, tolerance, interval, or maximum iterations, modify these values:
def f(x):
    return x**3 - 4*x - 9  # Function for which the root is sought
tol = 0.000001            # Tolerance for stopping criteria
left = -4                 # Left endpoint of the interval
right = 7                 # Right endpoint of the interval
max = 100                 # Maximum number of iterations

3. Fixed Point Iteration
To change the function or tolerance for the Fixed Point Iteration, modify these values:
def g(x):
    return (10 - x**2)**(1/3)  # Fixed point function
tol = 0.000001               # Tolerance for stopping criteria
p0 = 3                        # Initial approximation
n0 = 100                      # Maximum number of iterations

4. Newton-Raphson Method
To modify the function or tolerance for the Newton-Raphson method, change the following:
f = x**3 + 4*x**2 - 10      # Function for which the root is sought
tol = 1e-4                  # Tolerance for stopping criteria
initial_guess = (a + b) / 2 # Initial guess for the root
max_iter = 100              # Maximum number of iterations

Dependencies
This project uses the following Python packages:

sympy: For symbolic mathematics (used in the Newton-Raphson method).

You can install the necessary packages by running:
pip install -r requirements.txt

Running the Code
To run the script, simply execute the Python file:
python assignment_1.py
This will run all the methods in sequence and print the results of each method's root finding process.

Example output:
Approximation algorithm, root 2 results:
0: 1.5
1: 1.4166666666666667
2: 1.4142156862745099
3: 1.4142135623746899
...

Bisection Method result:
Root found: 2.879385948181152
Converged in 16 iterations.

Fixed Point Operation result:
Success: p = 2.879385948181152

Newton-Raphson Method results:
Root: 2.8794, found in 4 iterations.

Explanation of the File Structure:

main/: Main execution files for running the methods.

test/: Test cases for each of the methods.

assignment_1.py: Main file that includes all the methods.

requirements.txt: List of dependencies required to run the code.

README.md: Documentation for the project.

