def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Example:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary_search_iterative(arr, target)
print(f"Element {target} is at index {result}")  
