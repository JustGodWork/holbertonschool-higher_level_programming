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
    if type(text) is not str:
        raise TypeError("text must be a string")

    text = text.strip()
    new_text = ""
    for char in text:
        new_text += char
        if char in ".?:":
            new_text += "\n\n"
    print(new_text, end="")
