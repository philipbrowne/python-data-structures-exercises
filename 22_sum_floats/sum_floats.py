def sum_floats(nums):
    """Return sum of floating point numbers in nums.

        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9

        >>> sum_floats([1, 2, 3])
        0
    """
    # Without Comprehension and Sum Method
    # total = 0
    # for num in nums:
    #     if isinstance(num, float):
    #         total += num
    # return total

    # Using Comprehension and Built-In Sum Method
    return sum(num for num in nums if isinstance(num, float))
