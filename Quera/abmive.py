def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index][0] > right[right_index][0]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result

n, V = input().split(" ")
V = int(V)
items = []
for _ in range(int(n)):
    h, v = map(int, input().split())
    priority = h / v
    items.append((priority, h, v))

# Sort items by priority descending using merge sort
sorted_items = merge_sort(items)[::-1]

max_h = 0
sum_v = 0
for _, h_val, v_val in sorted_items:
    print(sum_v, v_val)
    if sum_v + v_val <= V:
        max_h += h_val
        sum_v += v_val
    if V-sum_v !=
        remaining_v = V - sum_v
        max_h += (remaining_v / v_val) * h_val
        break

print(round(max_h))  # Using round to handle floating-point arithmetic
