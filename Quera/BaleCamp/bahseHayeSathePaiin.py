def find_kth_element(k, t):
    # Basic sequence plus the extra "Peygir" that gets added every t elements
    pattern = ["Peygir", "Tannaz", "Jeddy", "Morshed"]
    # Calculate the total length of the cycle, including the extra "Peygir"
    cycle_length = t + 1  # t elements and 1 "Peygir"

    # Find position within the cycle
    position_in_cycle = (k - 1) % cycle_length

    # If the position is exactly the extra "Peygir" place
    if position_in_cycle == t:
        return "Peygir"
    else:
        # Find the element in the pattern excluding the additional "Peygir"
        return pattern[position_in_cycle % len(pattern)]

n, t = map(int, input().split())
results = []
for _ in range(n):
    k = int(input())
    results.append(find_kth_element(k, t))

for result in results:
    print(result)
