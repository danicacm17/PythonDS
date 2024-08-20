def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """

# Iterate through the list with a window of size 3
    for i in range(len(nums) - 2):
        # Calculate the sum of the current triplet
        triplet_sum = nums[i] + nums[i + 1] + nums[i + 2]
        
        # Check if the sum is odd
        if triplet_sum % 2 == 1:
            return True
    
    # If no triplet sum is odd, return False
    return False    
