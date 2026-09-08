# Exercise 4-08: Cubes
# Creating a list of the first 10 cubes using a loop and printing each value.

cubes = []
for number in range(1, 11):
    cube_value = number ** 3
    cubes.append(cube_value)

for cube in cubes:
    print(cube)
