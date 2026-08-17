def The_Great_Run(N, K, girls):
    current = sum(girls[:K])
    maximum = current

    for i in range(K, N):
        current += girls[i] - girls[i - K]
        maximum = max(maximum, current)

    return maximum