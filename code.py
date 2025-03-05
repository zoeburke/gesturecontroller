import time
from adafruit_circuitplayground import cp
from lightdisplay import LightDisplay
from sensorlightdisplay import SensorLightDisplay

def clear_lights(delay=1):
    cp.pixels.fill([0, 0, 0])
    cp.pixels.show()
    time.sleep(delay)

light_display = LightDisplay(brightness=0.1)
sensor_display = SensorLightDisplay(brightness=0.1)

while True:
    light_display.half_pattern([255, 0, 0])
    clear_lights()
    
    light_display.snake(3, [255, 255, 0], 0.2)
    clear_lights()
    
    light_display.light(0, [0, 255, 0])
    time.sleep(0.5)
    clear_lights()
    
    light_display.random_light([0, 0, 255], 0.5)
    clear_lights()
    
    sensor_display.light(cp.acceleration[:2], [255, 255, 255])
    clear_lights()
    
    sensor_display.control_feedback_y(cp.acceleration[1])
    clear_lights()

    time.sleep(0.5)
