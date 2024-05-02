def cake_cutting(m, a, b, c):
    # Calculate the total volume of the cake
    total_volume = a * b * c
    
    # Calculate the volume of each piece
    piece_volume = total_volume / m
    
    # Calculate the lengths of the pieces in each dimension
    length_x = a
    length_y = b
    length_z = c / m
    
    # Initialize the list to store cutting points
    cutting_points = []
    
    # Calculate the cutting points in the z dimension
    for i in range(1, m):
        z_cut = i * length_z
        cutting_points.append((0, 0, z_cut))
    
    return cutting_points

# Input
m = int(input())
a, b, c = map(int, input().split())

# Generate cutting points
cutting_points = cake_cutting(m, a, b, c)

# Output cutting points
for cut_point in cutting_points:
    print(*cut_point)
