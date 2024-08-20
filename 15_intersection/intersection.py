def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """

     # Convert lists to sets to find the intersection
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection and convert it back to a list
    intersected_set = set1.intersection(set2)
    
    return list(intersected_set)

#  set2 = set(l2)

#     return [val for val in l1 if val in set2]