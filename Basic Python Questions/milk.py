import math

# Function to calculate the volume of a cuboid
def volume_of_cuboid(height, length, breadth):
    return height * length * breadth

# Function to calculate the volume of a cylinder (glass)
def volume_of_cylinder(height, radius):
    return math.pi * (radius ** 2) * height

# Input dimensions of the milk tank
H = float(input("Enter the height of the milk tank (in cm): "))
L = float(input("Enter the length of the milk tank (in cm): "))
B = float(input("Enter the breadth of the milk tank (in cm): "))

# Input dimensions of the glass
h = float(input("Enter the height of the glass (in cm): "))
r = float(input("Enter the radius of the glass (in cm): "))

# Calculate the volume of the milk tank
volume_tank = volume_of_cuboid(H, L, B)

# Calculate the volume of one glass
volume_glass = volume_of_cylinder(h, r)

# Calculate the number of glasses of milk that can be obtained
number_of_glasses = volume_tank // volume_glass

print(f"Number of glasses of milk that can be obtained: {int(number_of_glasses)}")