# Linear Motion Calculator

This Python script provides a simple GUI application for calculating linear motion parameters such as acceleration, velocity, displacement, and time. The program is built using the `tkinter` library for the graphical user interface and `matplotlib` for plotting the motion graphs.

## Features

- **Calculate Acceleration**: Given the initial velocity, time, and displacement, calculate the acceleration.
- **Calculate Final Velocity**: Given the initial velocity, time, and acceleration, calculate the final velocity.
- **Calculate Displacement**: Given the initial velocity, time, and acceleration, calculate the displacement.
- **Calculate Time**: Given the initial velocity, acceleration, and displacement, calculate the time taken.
- **Plot Motion Graphs**: Visualize the velocity vs. time and displacement vs. time graphs based on the input parameters.

## Requirements

- Python 3.x
- `tkinter` (usually included with Python installations)
- `matplotlib`

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/username/linear-motion-calculator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd linear-motion-calculator
    ```

3. Install the required Python packages (if not already installed):

    ```bash
    pip install matplotlib
    ```

## Usage

1. Run the script:

    ```bash
    python linear_motion_calculator.py
    ```

2. A GUI window will open with the following fields:
   - **Initial Velocity (m/s)**: Enter the initial velocity of the object.
   - **Time (s)**: Enter the time duration.
   - **Acceleration (m/s²)**: Enter the acceleration (optional for certain calculations).
   - **Displacement (m)**: Enter the displacement (optional for certain calculations).

3. Choose what you want to calculate from the drop-down menu:
   - Acceleration
   - Velocity
   - Displacement
   - Time

4. Click the **Calculate** button to perform the calculation. The result will be displayed in the window, and if applicable, graphs of the motion will be plotted.

## Example

If you want to calculate the final velocity of an object with an initial velocity of 5 m/s after 10 seconds under an acceleration of 2 m/s²:
- Enter `5` in the **Initial Velocity** field.
- Enter `10` in the **Time** field.
- Enter `2` in the **Acceleration** field.
- Select **Velocity** from the drop-down menu.
- Click **Calculate**.

The result will be displayed as `Final Velocity: 25.00 m/s`, and the motion graphs will be shown.

