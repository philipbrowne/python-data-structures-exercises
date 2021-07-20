def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    newphrase = list(phrase)
    for index, char in enumerate(newphrase):
        if char.lower() == to_swap.lower():
            newphrase[index] = newphrase[index].swapcase()
    return ''.join(newphrase)
