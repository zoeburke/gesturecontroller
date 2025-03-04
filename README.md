# Gesture Controller - Circuit Playground Express

## Project Overview
This project implements **gesture-based controls** using the **Circuit Playground Express** board for _Pacman’s Battle for Food!_. It utilizes **Neopixels and an accelerometer** to provide visual feedback for gestures.

### Features:
- **Custom Neopixel Light Effects** – Half patterns, flashing lights, and a snake effect.  
- **Accelerometer-Based Control** – Lights respond to board tilt movements.  
- **User-Defined Brightness Settings** – Allows brightness adjustments.  
- **Randomized LED Patterns** – Uses built-in randomness to light up specific pixels.

## Project Structure

```
StudentID_assignment_2/
│
├── code.py                  # Main script for testing all methods
├── lightdisplay.py          # Handles general LED light effects
├── sensorlightdisplay.py    # Handles accelerometer-based LED effects
└── Documentation.pdf        # Includes explanation & commented code
```

### Files Explained:

#### `lightdisplay.py`  
Implements **Neopixel animations** with:
- `half_pattern(self, colour)`: Lights Neopixels in a symmetrical half pattern.
- `light(self, side, colour)`: Lights up specific sections of the board.
- `random_light(self, colour, sec_interval)`: Flashes five random LEDs **without duplicates**.
- `snake(self, snake_size, colour, interval)`: Moves a "snake" of lights across the Neopixels.

#### `sensorlightdisplay.py`  
Uses **accelerometer inputs** for controlling LEDs:
- `light(self, acceleration)`: Changes colors based on tilt direction.
- `control_feedback_y(self, acceleration_y)`: Lights **slowly turn on** when tilted and **turn off when flat**.

#### `code.py`  
Runs and tests all implemented features in a continuous loop.

## Installation & Setup

### Step 1: Install CircuitPython
1. **Download CircuitPython for Circuit Playground Express** from:  
   [CircuitPython Downloads](https://circuitpython.org/board/circuitplayground_express/)
2. **Put your board in "BOOT" mode** by double-tapping the **reset** button.
3. **Drag & drop the `.uf2` firmware file** onto the `BOOT` drive.

### Step 2: Set Up the Files
1. **Connect your board via USB.**  
   A drive named **CIRCUITPY** should appear.
2. **Copy these files to `CIRCUITPY`**:
   - `code.py`
   - `lightdisplay.py`
   - `sensorlightdisplay.py`
3. **Ensure Mu Editor is installed** for running CircuitPython code.

## How to Run the Program
1. **Run `code.py`** using Mu Editor or any CircuitPython-compatible IDE.
2. **Expected behavior**:
   - Neopixels display **half-pattern**, random lights, and a snake effect.
   - Board tilt controls **light behavior** (color change based on x/y acceleration).
   - Lights **gradually turn on** as you tilt the board **forward/backward**.

## License
This project is for academic use only and is part of the **CS2013 course at UCC**.
