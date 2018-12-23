import math

# Location of orbiting point is (x, y)
# Location of fixed point is always (100, 0) but can be changed

pointX = 100
pointY = 0
radians = 10 * math.pi / 180
cos10 = math.cos(radians)
sin10 = math.sin(radians)

# Get the initial satalite points from user

x, y = eval(input("Enter the initial satalite coordinates (x, y): "))

distance1 = math.sqrt((pointX - x) * (pointX - x) + (pointY - y) * (pointY - y))

# The satalite orbits 10 degrees
xOld = x;
x = x*cos10 - y*sin10

# Compute the new distance
distance2 = math.sqrt((pointX - x) * (pointX - x) + (pointY - y) * (pointY - y))

# Print the differences in distances
print("Difference in distances: %3.f" % (distance2 - distance1))