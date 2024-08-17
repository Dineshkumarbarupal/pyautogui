import pyautogui
import time

print("You have 5 seconds to position your mouse over the input box...")

time.sleep(5)  # Wait for 5 seconds

# Print the current mouse cursor position
print(pyautogui.position())
