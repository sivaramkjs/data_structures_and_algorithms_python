"""
Dynamic programming (DP) is an optimization technique.

1. It uses caching/memoization to solve a problem by breaking it down into subproblems and saving each subproblem solution
to avoid repetitive work in case same subproblem occurs again.

2. Memoization/Caching:
    1. Memoization is a specific form of caching that saves the solution/return value of a function for a specific set of
       parameters. It's used to store solution of each subproblem and reuse it instead of computing again.

        E.g., In the first function, we will need to recalculate the value everytime even for same "n" value.

                def add_to_80(n):
                    return n + 80

                cache = {}
                def memoized_add_to_80(n):
                    if n not in cache:
                        cache[n] = n + 80

                    return cache[n]
    2. Instead of using global cache object, we can improve this further by using a closure function and moving the cache
       to outer function. This will lead to keeping the cache local to the function.

       E.g.,
            def memoized_add_to_80():
                cache = {}

                def memo(n):
                    if n not in cache:
                        print('calc')
                        cache[n] = n + 80

                    return cache[n]

                return memo
            memo_func = memoized_add_to_80()
            memo_func(5)
            memo_func(5)
            memo_func(6)

3. We can classify DP as below:
    Dynamic programming (DP) = (Divide & Conquer subproblems) + (Memoization)

4. Steps to identify the case to use DP:
    1. Can a problem be divided into subproblems
    2. Recursive solution
        - This means same function is being called multiple times to reach a solution. In this case, we will need to
          check the next step.
    3. Are there repetitive subproblems?
        - For an instance, many tree-based problems are solved using recursion. However, not all tree-based problems would
          contain repetitive subproblems. Hence, this step is important to determine the eligibility to use DP.
    4. Memoize subproblems

    E.g., Classic example is fibonacci series problem using recursion, which contains repetitive subproblems for each of
          previous numbers fibonacci calculation.

Types of Dynamic Programming:
    1. Top-Down (Memoization):
        - This starts with the main problem and find solution recursively until the last required subproblem.
        - It uses cache to store each subproblem result to avoid recomputation. Basically, this can be interpreted
          as "Have I seen this subproblem before? If yes, return the result; if no, compute and remember it". Hence, this
          is viewed as "lazy on-demand" strategy.
        - Unlike Bottom-Up, this computes a subproblem only when needed.
        E.g., nth Fibonacci number using recursion

    2. Bottom-Up (Tabulation):
        - This starts at the smallest known subproblem (f(0)) and iteratively computes solution upto the main problem (f(n)).
        - It stores each subproblem result from smallest until the final solution. Basically, this can be interpreted
          as "Just compute all subproblem results until "n", remember and reuse when needed".
        - Technically, it solves all subproblems until "n", which can be interpreted as filling a table with all possible
          subproblem results. Hence, it is also called as "Tabulation" and viewed as "eager upfront" strategy.
        E.g., nth Fibonacci number using loop

"""
