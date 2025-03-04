import time
from adafruit_circuitplayground import cp
from lightdisplay import LightDisplay
from sensorlightdisplay import SensorLightDisplay

# Initialize instances with 10% brightness
light_display = LightDisplay(brightness=0.1)
sensor_display = SensorLightDisplay(brightness=0.1)

while True:
    # Test half-pattern method (red)
    light_display.half_pattern([255, 0, 0])

    # Test snake effect: snake of size 3 in yellow, with 0.2 seconds between movements
    light_display.snake(3, [255, 255, 0], 0.2)

    # Test light method: side 0 (green)
    light_display.light(0, [0, 255, 0])

    # RANDOM METHOD TO BE IMPLEMENTED

    # Uncomment below to test sensor methods.
    # sensor_display.light(cp.acceleration[:2])
    # sensor_display.control_feedback_y(cp.acceleration[1])

    time.sleep(0.1)
