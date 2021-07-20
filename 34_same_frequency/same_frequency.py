def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    freqlist1 = list(str(num1))
    freqlist2 = list(str(num2))
    setfreq1 = set(freqlist1)
    setfreq2 = set(freqlist2)
    setdict1 = {}
    setdict2 = {}
    for digit in setfreq1:
        setdict1[digit] = freqlist1.count(digit)
    for digit in setfreq2:
        setdict2[digit] = freqlist2.count(digit)
    return setdict1 == setdict2
