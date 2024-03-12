## Introduction
This Python script, `words.py`, contains a set of functions that operate on lists of words. The script provides functionality to print words in uppercase, filter words starting with a specific letter, and generalize the filtering based on a set of letters.

## Usage
1. **Print Words in Uppercase**
    - Function: `print_upper_words(words: List[str]) -> None`
    - Description: Prints each word from the given list on a separate line in uppercase.
    - Example:
        ```python
        word_list = ["apple", "banana", "cherry"]
        print_upper_words(word_list)
        ```
        Output:
        ```
        APPLE
        BANANA
        CHERRY
        ```

2. **Filter Words Starting with 'e'**
    - Function: `print_words_starting_with_e(words: List[str]) -> None`
    - Description: Prints words from the given list that start with the letter 'e' (case-insensitive).
    - Example:
        ```python
        word_list = ["elephant", "apple", "orange", "banana", "cherry"]
        print_words_starting_with_e(word_list)
        ```
        Output:
        ```
        ELEPHANT
        ```
