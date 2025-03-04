from adafruit_circuitplayground import cp


class SensorLightDisplay:
    BLACK = [0, 0, 0]
    NUM_PIXELS = len(cp.pixels)

    def __init__(self, brightness):
        cp.pixels.brightness = brightness
        cp.pixels.auto_write = False

    def light(self, acceleration):

        x, y = acceleration
        cp.pixels.fill(self.BLACK)
        if x < -3:
            cp.pixels.fill([0, 255, 0])  # Green for left tilt
        elif x > 3:
            cp.pixels.fill([255, 0, 0])  # Red for right tilt
        elif y < -3:
            cp.pixels.fill([255, 0, 255])  # Magenta for backward tilt
        elif y > 3:
            cp.pixels.fill([0, 255, 255])  # Cyan for forward tilt
        cp.pixels.show()

    def control_feedback_y(self, acceleration_y):

        # Calculate intensity as a percentage of maximum tilt (9.81)
        intensity = int((abs(acceleration_y) / 9.81) * 255)
        # Ensure the value doesn't exceed 255
        if intensity > 255:
            intensity = 255
        # Use blue color with the computed intensity: [R, G, B]
        color = [0, 0, intensity]
        cp.pixels.fill(color)
        cp.pixels.show()
