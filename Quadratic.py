#I cannot find the imaginary roots Fahad bhaijan help me a bit PLease
# Solving the quadratic formula
# ax^2 + bx + c = 0  # quadratic equation

# Important relevant modules
import cmath  # complex math module

# Solve the quadratic formula!
a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))

# Calculate the discriminant
d = (b**2) - (4*a*c)
# This will return an imaginary number if b^2 < 4ac

# Calculate the formula
solution1 = (-b + cmath.sqrt(d))/(2*a)
solution2 = (-b - cmath.sqrt(d))/(2*a)

# Print the solutions
print("The solutions to the quadratic "
      "equation are {} and {}".format(solution1, solution2))