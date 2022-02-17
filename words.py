def print_upper_words(words, must_start_with):
    """Given a list of words, and a set of letters 
    Prints out each word that start with a letter in the given set on a separate line, but in all uppercase
    """
    for word in words:
        subset = {word[0]}
        if subset.issubset(must_start_with):
            print(word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                  must_start_with={"h", "y"})
