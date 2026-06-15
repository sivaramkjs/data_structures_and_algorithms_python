def knapsack_unbounded(values, weights, capacity):  # T: O(n * capacity), S: O(n * capacity)
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):  # O(n)
        for w in range(capacity + 1):  # O(capacity)
            # Key difference from 0/1 knapsack:
            # 1. We "skip" the current item if the bag value is already better excluding the current item.
            # 2. We "take" the current item including same item again (notice "dp[i][w - weights[i - 1]]" instead of
            # "dp[i-1][w - weights[i - 1]]" as in 0/1 knapsack). This helps to reuse an item as many times as we want
            # as long as it's satisfying the total weight constraint.

            # skip
            dp[i][w] = dp[i - 1][w]

            # pick
            if weights[i - 1] <= w:
                # weights[i - 1]: Weight of the current item "i".
                # values[i - 1]: Value of the current item "i".
                # However, as the "weights" and "values" arrays are 0-index based, using "i-1" index.
                dp[i][w] = max(dp[i][w], dp[i][w - weights[i - 1]] + values[i - 1])
    print(dp)
    return dp[n][capacity]


def knapsack_unbounded_space_optimized(values, weights, capacity):  # T: O(n * capacity), S: O(capacity)
    n = len(values)
    dp = [0] * (capacity + 1)

    for i in range(n):  # O(n)
        for w in range(weights[i], capacity + 1):  # O(capacity)
            if weights[i] <= w:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    print(dp)
    return dp[capacity]


def knapsack_unbounded_3(values, weights, capacity):  # T: O(n * capacity), S: O(capacity)
    n = len(values)
    dp = [values[i] / weights[i] for i in range(n)]
    dp.sort()

    for i in range(n):
        allowed_weight_multiple = capacity / weights[i]


print(knapsack_unbounded([15, 20], [2, 3], 4))
print(knapsack_unbounded_space_optimized([15, 20], [2, 3], 4))
