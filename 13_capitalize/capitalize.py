def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    #return phrase.capitalize()

    return phrase[:1].upper() + phrase[1:]
    
    