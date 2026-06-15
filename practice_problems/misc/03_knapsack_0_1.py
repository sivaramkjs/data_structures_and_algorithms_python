def knapsack_0_1(values, weights, capacity):  # T: O(n * capacity), S: O(n * capacity)
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):  # O(n)
        for w in range(1, capacity + 1):  # O(capacity)
            # exclude item (0)
            dp[i][w] = dp[i - 1][w]

            # include item (1)
            if weights[i - 1] <= w:
                # weights[i - 1]: Weight of the current item "i".
                # values[i - 1]: Value of the current item "i".
                # dp[i-1] refers to the knapsack weight at "w - weights[i-1]" before adding the current item.
                # As the "weights" and "values" arrays are 0-index based, using "i-1" index.
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
    # print(dp)
    return dp[n][capacity]


def knapsack_0_1_space_optimized(values, weights, capacity):  # T: O(n * capacity), S: O(capacity)
    dp = [0] * (capacity + 1)

    for i in range(len(values)):
        # If we start the below loop at the first item in the list ("range(weights[i], capacity+1)")
        # then it will update all the corresponding indexed values by including the current item "i" before we reach
        # further w-th iterations. As a result, when we take "dp[w - weights[i]]" at some w-th iteration, it already
        # includes the current item even before adding the "values[i]" at that weight "w". This leads to reusing the
        # current item more than once (unbounded knapsack) in contrast to 0/1 knapsack.
        # However, we want "dp[w - weights[i]]" to be the total value of all previous items until "i" at that weight "w".
        # Hence, reverse iteration will keep all the previous values for "dp[w - weights[i]]" properly and restrict using
        # the current item only once by adding "values[i]" to it.
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    # print(dp)
    return dp[capacity]


print(knapsack_0_1([1, 2, 5], [2, 3, 4], 8))
print(knapsack_0_1_space_optimized([1, 2, 5], [2, 3, 4], 8))
