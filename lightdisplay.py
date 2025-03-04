import time
from adafruit_circuitplayground import cp


class LightDisplay:
    BLACK = [0, 0, 0]
    NUM_PIXELS = len(cp.pixels)  # Typically 10 neopixels on the board

    def __init__(self, brightness):
        cp.pixels.brightness = brightness
        cp.pixels.auto_write = False

    def half_pattern(self, colour):
        positions = [(0, 9), (1, 8), (2, 7), (3, 6), (4, 5)]
        for pair in positions:
            for index in pair:
                cp.pixels[index] = colour
            cp.pixels.show()
            time.sleep(0.5)
        cp.pixels.fill(self.BLACK)
        cp.pixels.show()

    def light(self, side, colour):
        side_map = {0: [1, 2, 3], 1: [6, 7, 8], 2: [4, 5], 3: [0, 9]}
        if side in side_map:
            for index in side_map[side]:
                cp.pixels[index] = colour
        cp.pixels.show()

    def snake(self, snake_size, colour, interval):
        if snake_size < 2 or snake_size > self.NUM_PIXELS // 2:
            return
        for i in range(self.NUM_PIXELS - snake_size + 1):
            cp.pixels.fill(self.BLACK)
            for j in range(snake_size):
                cp.pixels[i + j] = colour
            cp.pixels.show()
            time.sleep(interval)
