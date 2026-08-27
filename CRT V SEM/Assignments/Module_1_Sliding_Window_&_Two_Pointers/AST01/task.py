def maxGirls(arr, k):
    window_sum = sum(arr[:k])
    maximum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        maximum = max(maximum, window_sum)

    return maximum


if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    print(maxGirls(arr, k))