d, r = divmod(5, 2)
print(d + (r != 0))


def rotate(nums, k):
    nums.reverse()
    n = len(nums)
    k = k % n

    # nums[:n - k] = reversed(nums[:n - k])
    # nums[n - k:] = reversed(nums[n - k:])

    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])


a = [1, 2, 3]
rotate(a, 4)
print(a)
