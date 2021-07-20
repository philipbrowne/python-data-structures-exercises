def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = 'aeiou'
    vowelslist = [char for char in s if char.lower() in vowels]
    reverse = vowelslist[::-1]
    stringlist = list(s)
    for i in range(len(stringlist)):
        if stringlist[i].lower() in vowels:
            stringlist[i] = reverse[0]
            reverse.pop(0)
    return ''.join(stringlist)
