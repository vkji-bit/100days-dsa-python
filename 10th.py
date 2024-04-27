# Coin Change Problem
#day 10
#sum=5 coins=[1,2,3] 
#output 5

def count(coins, n, target_sum):
    
    dp = [[0 for j in range(target_sum + 1)] for i in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(target_sum + 1):
            dp[i][j] += dp[i - 1][j]
 
            if j - coins[i - 1] >= 0:
                
                dp[i][j] += dp[i][j - coins[i - 1]]
 
    return dp[n][target_sum]

coins = [1, 2, 3]
n = len(coins)
target_sum = 5
print(count(coins, n, target_sum))