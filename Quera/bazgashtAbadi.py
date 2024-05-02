result = []

n = int(input())
for _ in range(n):
    index_needed = int(input())
    if index_needed == 1:
        result.append(2)
    else:
        # Calculate the index within the pattern
        index_within_pattern = (index_needed - 2) % 4
        # Retrieve the corresponding element from the pattern
        result.append([1, -3, 2, -2][index_within_pattern])

for i in result:
    print(i)