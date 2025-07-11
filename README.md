# Automatic Door Opening System using ESP32

This project is an automatic door system built using an **ESP32**, an **LDR (Light Dependent Resistor)** sensor, and a **servo motor**. The system detects changes in light intensity and opens or closes the door accordingly using a servo motor.

---

## How It Works

- The **LDR** reads ambient light levels.
- When the light intensity **crosses a threshold** (e.g., someone approaches or light increases), the **servo motor rotates** to open the door.
- After a short delay or when the light level decreases, the **servo closes** the door.

---

## Components Used

- ESP32 board
- LDR (Light Dependent Resistor)
- SG90 Servo Motor
- Jumper Wires
- Breadboard (optional)
- MicroPython (programmed via Thonny IDE)
