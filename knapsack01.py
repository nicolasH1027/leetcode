def knapsack(W, N, weights, values):
    
    dp = [[0]*(W + 1) for _ in range(N + 1)]
    
    for i in range(N):
        dp[i][0] = 0
        
    for j in range(sum(weights)):
        dp[0][j] = 0
        
    for i in range(N + 1):
        for j in range(W + 1):
            if j >= weights[i - 1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - weights[i - 1]] + values[i-1])
            else:
                dp[i][j] = dp[i-1][j]