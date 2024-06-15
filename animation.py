import os
import time
import sys

# Define the frames of the animation
frames = [
"""
    \o
     |\\
    / \\
""",
"""
     o/
    /|
    / \\
""",
]

# Function to clear the screen
def clear():
    if sys.platform == 'win32':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Linux/OS X

# Animation loop
while True:
    for frame in frames:
        clear()
        print(frame)
        time.sleep(0.5)  # Adjust to control the animation speed