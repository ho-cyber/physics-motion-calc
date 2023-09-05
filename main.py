import tkinter as tk
import math
import matplotlib.pyplot as plt

def calculate_motion():
    try:
        # Get input values
        initial_velocity = float(velocity_entry.get() or 0)
        time = float(time_entry.get() or 0)
        acceleration = float(acceleration_entry.get() or 0)
        displacement = float(displacement_entry.get() or 0)

        # Initialize result strings
        result = ""

        # Determine which equation to use based on the selected option
        option = option_var.get()

        if option == "Acceleration":
            acceleration = 2 * (displacement - initial_velocity * time) / (time ** 2)
            result = f"Acceleration: {acceleration:.2f} m/s²"

        elif option == "Velocity":
            final_velocity = initial_velocity + acceleration * time
            result = f"Final Velocity: {final_velocity:.2f} m/s"

        elif option == "Displacement":
            displacement = (initial_velocity * time) + (0.5 * acceleration * (time ** 2))
            result = f"Displacement: {displacement:.2f} meters"

        elif option == "Time":
            if acceleration == 0:
                time = displacement / initial_velocity
                result = f"Time: {time:.2f} seconds"
            else:
                discriminant = initial_velocity**2 + 2*acceleration*displacement
                if discriminant >= 0:
                    time_1 = (-initial_velocity + math.sqrt(discriminant)) / acceleration
                    time_2 = (-initial_velocity - math.sqrt(discriminant)) / acceleration
                    result = f"Time 1: {time_1:.2f} seconds\nTime 2: {time_2:.2f} seconds"
                else:
                    result = "No real solution for time."

        result_label.config(text=result)

        # Plot a graph of the motion
        if option in ["Displacement", "Velocity"]:
            plot_graph(initial_velocity, time, acceleration, displacement)

    except ValueError:
        result_label.config(text="Please enter valid numbers.")

def plot_graph(initial_velocity, time, acceleration, displacement):
    t_values = []
    v_values = []
    d_values = []

    for t in range(int(time) + 1):
        t_values.append(t)
        v = initial_velocity + acceleration * t
        v_values.append(v)
        d = initial_velocity * t + 0.5 * acceleration * (t ** 2)
        d_values.append(d)

    # Plot velocity vs. time
    plt.figure(figsize=(8, 6))
    plt.subplot(2, 1, 1)
    plt.plot(t_values, v_values, marker='o')
    plt.title('Velocity vs. Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')

    # Plot displacement vs. time
    plt.subplot(2, 1, 2)
    plt.plot(t_values, d_values, marker='o')
    plt.title('Displacement vs. Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Displacement (m)')

    plt.tight_layout()
    plt.show()

# Create a GUI window
window = tk.Tk()
window.title("Linear Motion Calculator")

# Create labels and entry fields
option_label = tk.Label(window, text="Choose what to calculate:")
option_label.pack()

options = ["Acceleration", "Velocity", "Displacement", "Time"]
option_var = tk.StringVar()
option_var.set(options[0])

option_menu = tk.OptionMenu(window, option_var, *options)
option_menu.pack()

initial_velocity_label = tk.Label(window, text="Initial Velocity (m/s):")
initial_velocity_label.pack()
velocity_entry = tk.Entry(window)
velocity_entry.pack()

time_label = tk.Label(window, text="Time (s):")
time_label.pack()
time_entry = tk.Entry(window)
time_entry.pack()

acceleration_label = tk.Label(window, text="Acceleration (m/s²):")
acceleration_label.pack()
acceleration_entry = tk.Entry(window)
acceleration_entry.pack()

displacement_label = tk.Label(window, text="Displacement (m):")
displacement_label.pack()
displacement_entry = tk.Entry(window)
displacement_entry.pack()

result_label = tk.Label(window, text="", justify="left")
result_label.pack()

calculate_button = tk.Button(window, text="Calculate", command=calculate_motion)
calculate_button.pack()

# Start the GUI main loop
window.mainloop()
