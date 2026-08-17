def Pair_Sum(arr, target):
    n = len(arr)

    # Find the index of the smallest element (pivot)
    pivot = 0
    for i in range(1, n):
        if arr[i] < arr[pivot]:
            pivot = i

    left = pivot
    right = (pivot - 1 + n) % n

    while left != right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return True
        elif current_sum < target:
            left = (left + 1) % n
        else:
            right = (right - 1 + n) % n

    return False
