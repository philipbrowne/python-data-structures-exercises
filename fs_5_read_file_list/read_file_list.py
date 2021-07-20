def read_file_list(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """

    # hint: when you read lines of files, there will be a "newline"
    # (end-of-line character) at the end of each line, and you want to
    # strip that off before you print it. Do some research on that!
    filelines = open(filename).read().split('\n')
    newtext = ''
    for i in range(len(filelines)):
        if len(filelines) - i - 1 > 0:
            newtext += f'- {filelines[i]}\n'
        else:
            newtext += f'- {filelines[i]}'
    print(newtext)
