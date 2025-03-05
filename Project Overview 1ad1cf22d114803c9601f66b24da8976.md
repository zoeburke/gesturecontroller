# Project Overview

## Overview:

This project uses the Adafruit Circuit Playground hardware to create various light patterns.
It demonstrates Object-Oriented Programming (OOP) concepts such as encapsulation, the use of hardware variables,
and discusses how inheritance could be applied to share common functionality. The project is divided into three parts:
1. LightDisplay class: Provides methods for static and dynamic light patterns.
2. SensorLightDisplay class: Uses sensor (acceleration) data to determine which LED patterns to show.
3. Main execution script: Creates instances of the classes and cycles through the light patterns in a loop.

## OOP Concepts:

1. Encapsulation:
    - Both the LightDisplay and SensorLightDisplay classes encapsulate properties (such as brightness, BLACK color, and the number of pixels)
    and methods that control the LED hardware. This hides the internal implementation details (like direct manipulation of cp.pixels)
    and exposes a simple interface (e.g., half_pattern, snake, light, random_light, control_feedback_y).
2. Hardware Variables:
    - The classes use hardware-specific variables from the adafruit_circuitplayground library (e.g., cp.pixels and cp.acceleration).
    - These variables abstract the actual physical device, allowing the code to modify LED states and read sensor data easily.
    - In the **init** methods of the classes, the brightness is set and auto_update is disabled (auto_write = False) so that
    changes to the pixels are only visible after an explicit update.
3. Inheritance (Discussion):
    - While the project uses separate classes for different light behaviours, both classes share some common properties:
    • Initialisation of brightness and auto_write.
    • Constants like BLACK (to turn off LEDs) and NUM_PIXELS (the number of LEDs).
    - In a more advanced design, a base class (e.g., BaseLightDisplay) could be used to house these common elements.
    - Then, LightDisplay and SensorLightDisplay could inherit from the base class, reducing code duplication and improving maintainability.

Below, the complete code with detailed inline comments is provided.

```python
# ======================================================
# Module: lightdisplay.py
# ======================================================
import time                          # Provides time-related functions.
from random import randint           # Used to generate random pixel indices.
from adafruit_circuitplayground import cp  # Imports the hardware-specific library for controlling the Circuit Playground.

class LightDisplay:
    # Define a constant representing the "off" state (black) for the pixels.
    BLACK = [0, 0, 0]
    # Determine the total number of pixels available on the device.
    NUM_PIXELS = len(cp.pixels)

    def __init__(self, brightness):
        """
        Constructor for LightDisplay.
        Sets the brightness for the LED pixels and disables auto_write so that
        the display is only updated when cp.pixels.show() is called.
        """
        cp.pixels.brightness = brightness     # Set the global brightness for all pixels.
        cp.pixels.auto_write = False            # Disable auto-updating of the LED display.

    def half_pattern(self, colour):
        """
        Displays a sequential "half pattern" by lighting up predefined pairs of pixels.
        This creates a symmetrical visual effect across the LED array.
        """
        # Define pairs of pixel indices for symmetry.
        positions = [(0, 9), (1, 8), (2, 7), (3, 6), (4, 5)]
        # Iterate over each pair.
        for pair in positions:
            # For each pixel in the current pair, set it to the specified colour.
            for index in pair:
                cp.pixels[index] = colour
            cp.pixels.show()        # Update the display to show the newly set pixels.
            time.sleep(0.5)         # Pause to allow the pattern to be visible.
        # After the pattern is complete, clear the display.
        cp.pixels.fill(self.BLACK)
        cp.pixels.show()

    def light(self, side, colour):
        """
        Lights a specific group of pixels based on a 'side' number.
        The method uses a dictionary to map a side number to specific pixel indices.
        """
        # Define the mapping from side numbers to pixel groups.
        side_map = {0: [1, 2, 3], 1: [6, 7, 8], 2: [4, 5], 3: [0, 9]}
        # Check if the provided side exists in the mapping.
        if side in side_map:
            for index in side_map[side]:
                cp.pixels[index] = colour   # Set each pixel in the mapped group to the given colour.
        cp.pixels.show()                    # Update the display.

    def random_light(self, colour, sec_interval):
        """
        Creates a random light pattern by selecting 5 unique random pixels to light up.
        The lit pixels remain on for 'sec_interval' seconds before being turned off.
        This process is repeated 5 times.
        """
        for _ in range(5):
            indices = []  # List to store unique random indices.
            # Loop until 5 unique indices are generated.
            while len(indices) < 5:
                num = randint(0, self.NUM_PIXELS - 1)  # Generate a random pixel index.
                if num not in indices:
                    indices.append(num)
            # Set each selected pixel to the specified colour.
            for i in indices:
                cp.pixels[i] = colour
            cp.pixels.show()  # Update the display with the randomly lit pixels.
            time.sleep(sec_interval)  # Wait for the specified interval.
            # Turn off the randomly lit pixels.
            for i in indices:
                cp.pixels[i] = self.BLACK
            cp.pixels.show()  # Update the display.
            time.sleep(sec_interval)  # Pause before the next iteration.

    def snake(self, snake_size, colour, interval):
        """
        Creates a "snake" effect by lighting a consecutive group of pixels.
        The snake_size determines the number of pixels lit at one time, and the effect
        moves across the LED array with a pause (interval) between moves.
        """
        # Validate the snake_size to ensure it is neither too small nor too large.
        if snake_size < 2 or snake_size > self.NUM_PIXELS // 2:
            return  # Exit the function if snake_size is invalid.
        # Iterate over the pixels such that a snake of the given size fits on the display.
        for i in range(self.NUM_PIXELS - snake_size + 1):
            cp.pixels.fill(self.BLACK)  # Clear the display before lighting the next snake segment.
            # Light consecutive pixels to form the snake.
            for k in range(snake_size):
                cp.pixels[i + k] = colour
            cp.pixels.show()  # Update the display.
            time.sleep(interval)  # Wait before moving the snake to the next set of pixels.

# ======================================================
# Module: sensorlightdisplay.py
# ======================================================
from adafruit_circuitplayground import cp

class SensorLightDisplay:
    # Define the off state (black) for the pixels.
    BLACK = [0, 0, 0]
    # Get the total number of pixels from the Circuit Playground.
    NUM_PIXELS = len(cp.pixels)

    def __init__(self, brightness):
        """
        Constructor for SensorLightDisplay.
        Sets the brightness for the LED pixels and disables auto_write so that
        the display is only updated when explicitly requested.
        """
        cp.pixels.brightness = brightness     # Set the brightness for all LEDs.
        cp.pixels.auto_write = False            # Disable automatic updates.

    def light(self, acceleration, colour):
        """
        Lights up specific pixels based on the acceleration data.
        Uses the x and y components of the acceleration to decide which group of pixels to illuminate.
        """
        x, y = acceleration   # Unpack the acceleration values (x and y).
        cp.pixels.fill(self.BLACK)  # Clear the display.
        # Determine which group of pixels to light based on sensor data thresholds.
        if x < -3 and x < y:
            # Tilted left: Light pixels 6, 7, 8.
            for i in range(6, 9):
                cp.pixels[i] = colour
        elif x > 3 and x > y:
            # Tilted right: Light pixels 1, 2, 3.
            for i in range(1, 4):
                cp.pixels[i] = colour
        elif y > 3 and y > x:
            # Tilted forward: Light pixels 4 and 5.
            for i in range(4, 6):
                cp.pixels[i] = colour
        elif y < -3 and y < x:
            # Tilted backward: Light pixels 0 and 9.
            for i in [0, 9]:
                cp.pixels[i] = colour
        cp.pixels.show()  # Update the display with the new sensor-based pattern.

    def control_feedback_y(self, acceleration_y):
        """
        Provides visual feedback based on the y-axis acceleration.
        The feedback is given as a blue color whose intensity is proportional to the absolute y acceleration.
        """
        # Ignore acceleration values that exceed the gravitational limit (to prevent erratic behavior).
        if acceleration_y < -9.81 or acceleration_y > 9.81:
            return
        # Calculate the intensity by scaling the absolute acceleration to the 0-255 range.
        intensity = int((abs(acceleration_y) / 9.81) * 255)
        # Ensure that the intensity does not exceed the maximum value of 255.
        if intensity > 255:
            intensity = 255
        # Define a blue colour with the calculated intensity.
        color = [0, 0, intensity]
        cp.pixels.fill(color)  # Set all pixels to the blue color.
        cp.pixels.show()       # Update the display.

# ======================================================
# Main Execution: code.py
# ======================================================
import time
from adafruit_circuitplayground import cp
# In this combined file, the classes LightDisplay and SensorLightDisplay are already defined above.
# In a separated module project, you would import them:
# from lightdisplay import LightDisplay
# from sensorlightdisplay import SensorLightDisplay

def clear_lights(delay=1):
    """
    Clears the LED display by turning all pixels off and pausing for a given delay.
    This function is used after each pattern to ensure the display is reset.
    """
    cp.pixels.fill([0, 0, 0])  # Set all pixels to BLACK (off).
    cp.pixels.show()           # Update the display.
    time.sleep(delay)          # Pause execution to let the change be visible.

# Create an instance of LightDisplay with a specified brightness.
light_display = LightDisplay(brightness=0.1)
# Create an instance of SensorLightDisplay with a specified brightness.
sensor_display = SensorLightDisplay(brightness=0.1)

# Begin an infinite loop to continuously display different light patterns.
while True:
    # -----------------------------------------------------------------
    # Display a half pattern using red color.
    # This lights up pairs of pixels sequentially.
    light_display.half_pattern([255, 0, 0])
    clear_lights()  # Clear the display after the pattern.
    
    # -----------------------------------------------------------------
    # Display a snake pattern using yellow color.
    # The snake pattern lights 3 consecutive pixels at a time, moving across the display.
    light_display.snake(3, [255, 255, 0], 0.2)
    clear_lights()  # Clear the display after the snake pattern.
    
    # -----------------------------------------------------------------
    # Light a specific side (side 0) using green color.
    # The method maps side 0 to a predefined group of pixels.
    light_display.light(0, [0, 255, 0])
    time.sleep(0.5)  # Pause to allow the pattern to be seen.
    clear_lights()   # Clear the display.
    
    # -----------------------------------------------------------------
    # Display random light patterns using blue color.
    # Randomly selected groups of pixels are lit, then turned off repeatedly.
    light_display.random_light([0, 0, 255], 0.5)
    clear_lights()   # Clear the display.
    
    # -----------------------------------------------------------------
    # Use sensor data to determine which pixels to light.
    # The light() method in SensorLightDisplay uses the x and y acceleration values.
    sensor_display.light(cp.acceleration[:2], [255, 255, 255])
    clear_lights()   # Clear the display.
    
    # -----------------------------------------------------------------
    # Provide visual feedback based on y-axis acceleration.
    # The intensity of blue displayed is proportional to the y-axis acceleration.
    sensor_display.control_feedback_y(cp.acceleration[1])
    clear_lights()   # Clear the display.
    
    # -----------------------------------------------------------------
    # Short pause before starting the next cycle of patterns.
    time.sleep(0.5)

```

# Conclusion

This file demonstrates the entire project, including all code and detailed inline commentary.
It shows how the Adafruit Circuit Playground is used to create engaging light patterns based on both
predefined sequences and sensor data.

### Key OOP Concepts:

- Encapsulation is used to bundle the LED control logic within classes (LightDisplay and SensorLightDisplay),
providing a clear interface for the main script.
- Hardware variables such as cp.pixels and cp.acceleration abstract the physical device details,
making the code easier to read and maintain.
- Inheritance could be applied in a more advanced design by extracting common elements (like brightness initialisation
and pixel constants) into a base class that both display classes extend.