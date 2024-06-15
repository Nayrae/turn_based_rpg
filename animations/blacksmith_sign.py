import sys, time

def animate_message(message, typing_delay=0.1, blink_delay=0.5, blink_count=3):
    """
    Enhances the message animation with typing and blinking effects.
    
    :param message: The message to animate.
    :param typing_delay: The delay (in seconds) between each character for the typing effect.
    :param blink_delay: The delay (in seconds) between blinks.
    :param blink_count: The number of times the message blinks.
    """
    # Typing effect
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(typing_delay)
    sys.stdout.write('\n')  # Move to the next line after the message
    
    time.sleep(blink_delay)
    
    # Blinking effect
    for _ in range(blink_count):
        sys.stdout.write("\033[A" + " " * len(message) + "\r")  # Move up a line and overwrite with spaces
        sys.stdout.flush()
        time.sleep(blink_delay)
        sys.stdout.write("\r" + message + '\n')  # Move to the start of the line and show the message
        sys.stdout.flush()
        time.sleep(blink_delay)

# The message to animate
message = "Blacksmith closed, thanks the programmer"
# DEBUG    animate_message(message)