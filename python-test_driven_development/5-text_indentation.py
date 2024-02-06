#!/usr/bin/python3
"""Module for text_indentation function."""


def text_indentation(text):
    """Prints a text with 2 new lines after
        each of these characters: ., ? and :.

    Args:
        text (str): The text to print.

    Returns:
        None.

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not (str):
        raise TypeError("text must be a string")

    sentence = ""

    for letter in text:

        sentence += letter

        if letter in [".", "?", ":"]:
            print("{}\n".format(sentence.strip()))
            sentence = ""

    if sentence.strip() != "":
        print("{}".format(sentence.strip()), end="")
