def find_pattern(string):
    """
    A function that finds all the occurrences of a certain pattern, that starts with “un” has unlimited number of letters and ends with “an”
    :param string: the text to check for parameters
    :return: number of matches
    """
    counter = 0  # Starts counter for words
    words = string.split()  # Splits the string so it iterates over individual words
    for word in words:
        if word[:2] == "un" and word[-2:] == "an":  # Checks if a word has "un" in positions 0:2 and "an" in the last two positions
            counter += 1  # If the word follows this pattern it adds 1 to the counter
    return counter


print(find_pattern("The unbroken union of the unusual unhuman clan remained strong."))


