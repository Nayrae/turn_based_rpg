import os
import time
import sys
#
## Define the frames of the animation
#frames = [
#"""
#    \o
#     |\\
#    / \\
#""",
#"""
#     o/
#    /|
#    / \\
#""",
#]
#
## Function to clear the screen
#def clear():
#    if sys.platform == 'win32':
#        os.system('cls')  # For Windows
#    else:
#        os.system('clear')  # For Linux/OS X

## Animation loop
#while True:
#    for frame in frames:
#        clear()
#        print(frame)
#        time.sleep(0.5)  # Adjust to control the animation speed
        



bed_frames = [
    """
       |||||
    [] ||||| []
       |||||
    """,
    """
       |||||
    [] ||||| [Z]
       |||||
    """,
    """
       |||||
    [] ||||| [Zz]
       |||||
    """,
    """
       |||||
    [] ||||| [ZzZ]
       |||||
    """
]
def clear():
    print("\n" * 100)
start_time = time.time()  # Record the start time
print("You lay down on the bed, ready to rest...")
time.sleep(1)
while True:
    current_time = time.time()
    if current_time - start_time >= 5:  # Check if 5 seconds have passed
        break  # Exit the loop after 5 seconds
    for frame in bed_frames:
        clear()
        print(frame)
        time.sleep(0.5)  # Adjust to control the animation speed


