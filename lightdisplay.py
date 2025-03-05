import time
from random import randint
from adafruit_circuitplayground import cp

class LightDisplay:
    BLACK = [0, 0, 0]
    NUM_PIXELS = len(cp.pixels)

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

    def random_light(self, colour, sec_interval):
        for _ in range(5):
            indices = []
            while len(indices) < 5:
                num = randint(0, self.NUM_PIXELS - 1)
                if num not in indices:
                    indices.append(num)
            for i in indices:
                cp.pixels[i] = colour
            cp.pixels.show()
            time.sleep(sec_interval)
            for i in indices:
                cp.pixels[i] = self.BLACK
            cp.pixels.show()
            time.sleep(sec_interval)

    def snake(self, snake_size, colour, interval):
        if snake_size < 2 or snake_size > self.NUM_PIXELS // 2:
            return
        for i in range(self.NUM_PIXELS - snake_size + 1):
            cp.pixels.fill(self.BLACK)
            for k in range(snake_size):
                cp.pixels[i + k] = colour
            cp.pixels.show()
            time.sleep(interval)

