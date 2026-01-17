def count(c, t):
    dp = [0] * (t + 1)
    dp[0] = 1
    for coin in c:
        for i in range(coin, t + 1):
            dp[i] += dp[i - coin]
    return dp[t]
d1 = [1, 2, 5]
t1 = 5
w1 = count(d1, t1)
print(f"For amount {t1} with coins {d1}, there are {w1} ways.")
d2 = [2, 3, 6]
t2 = 10
w2 = count(d2, t2)
print(f"For amount {t2} with coins {d2}, there are {w2} ways.")
d3 = [1, 2, 5]
t3 = 11
w3 = count(d3, t3)
print(f"For amount {t3} with coins {d3}, there are {w3} ways.")