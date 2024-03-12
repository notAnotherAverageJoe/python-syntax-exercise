def print_upper_words(words):
    """this function will take one positiona argument,
      and print each word on a seperate line and it will be uppercased.
      for example print_upper_words(["I", "love", "Pizza"]) would print out
      I
      LOVE
      PIZZA

 """
    for word in words:
        print(word.upper())


def print_upper_words2(words):
    """ Each word will get printed on a seperate line,
     as long as the word starts with the letter E or e.
      
       the example would be >>> print_upper_words2(["eagle", "APPLE", "Edamame"])
        EAGLE
        EDAMAME """
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


def print_upper_words3(words, must_start_with):
   
    """ each word will be printed uppercased on seperate line if they begin with the 
    letter chosen for the must_start_with argument.
    >>> print_upper_words3(["Beehive", "Pool", "aplphabet", "Bananas", "DRIVE"],["B", "P"]) 
   ...
    BEEHIVE
    POOL
    BANANAS
    """
    for word in words:
        if any(word.startswith(letter) for letter in must_start_with):
            print(word.upper())
