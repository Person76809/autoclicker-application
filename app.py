import pyautogui
import time

# Set the coordinates where you want to click
x, y = 100, 200

# Set the number of clicks and the interval between clicks in seconds
num_clicks = 10
click_interval = 1

# Start the loop to simulate the clicks
for i in range(num_clicks):
    # Move the mouse to the coordinates
    pyautogui.moveTo(x, y, duration=0.1)

    # Click the left mouse button
    pyautogui.click()

    # Wait for the interval before clicking again
    time.sleep(click_interval)
