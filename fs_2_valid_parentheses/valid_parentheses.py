def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    # Initialize a counter to track the balance of parentheses
    balance = 0

    # Iterate through each character in the string
    for char in parens:
        if char == '(':
            # Increment the balance counter for an opening parenthesis
            balance += 1
        elif char == ')':
            # Decrement the balance counter for a closing parenthesis
            balance -= 1
        
        # If balance is negative, there are more closing than opening parentheses
        if balance < 0:
            return False

    # If balance is zero, parentheses are balanced
    return balance == 0