from adafruit_circuitplayground import cp

class SensorLightDisplay:
    BLACK = [0, 0, 0]
    NUM_PIXELS = len(cp.pixels)

    def __init__(self, brightness):
        cp.pixels.brightness = brightness
        cp.pixels.auto_write = False

    def light(self, acceleration, colour):
        x, y = acceleration
        cp.pixels.fill(self.BLACK)
        if x < -3 and x < y:
            for i in range(6, 9):
                cp.pixels[i] = colour
        elif x > 3 and x > y:
            for i in range(1, 4):
                cp.pixels[i] = colour
        elif y > 3 and y > x:
            for i in range(4, 6):
                cp.pixels[i] = colour
        elif y < -3 and y < x:
            for i in [0, 9]:
                cp.pixels[i] = colour
        cp.pixels.show()

    def control_feedback_y(self, acceleration_y):
        if acceleration_y < -9.81 or acceleration_y > 9.81:
            return
        intensity = int((abs(acceleration_y) / 9.81) * 255)
        if intensity > 255:
            intensity = 255
        color = [0, 0, intensity]
        cp.pixels.fill(color)
        cp.pixels.show()
