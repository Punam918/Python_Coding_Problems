'''
 Your code for interacting with the latest web authentication scheme has encountered a
 singularity and your only solution is to go around it in the complex plane. Or maybe
 you just need to perform some calculations using complex numbers. like conjugate, exploring real parts
 and imaginary parts, addition, subtraction, and converting into polar form. 
'''
z = complex(3, 4)  
print("Complex number:", z)

print("Real part:", z.real)   
print("Imaginary part:", z.imag)  

print("Conjugate:", z.conjugate())  

z1 = complex(2, 3)
z2 = complex(1, -1)

print("Addition:", z1 + z2) 
print("Subtraction:", z1 - z2)  
print("Multiplication:", z1 * z2)  
print("Division:", z1 / z2) 

import cmath

r, theta = cmath.polar(z)  
print("Magnitude:", r)  
print("Phase (radians):", theta)  


z_polar = cmath.rect(r, theta)  
print("Rectangular form:", z_polar) 
