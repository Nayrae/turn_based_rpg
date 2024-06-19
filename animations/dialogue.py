import sys
import time

def typing_effect(text, delay=0.015):
    """
    Prints text with a typing effect.

    :param text: The text to print.
    :param delay: Delay between each character.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()