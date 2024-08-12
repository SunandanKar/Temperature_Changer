import tkinter as tk
from tkinter import ttk, messagebox

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def convert_temperature(value, from_scale, to_scale):
    if from_scale == "Celsius":
        if to_scale == "Fahrenheit":
            return celsius_to_fahrenheit(value)
        elif to_scale == "Kelvin":
            return celsius_to_kelvin(value)
    elif from_scale == "Fahrenheit":
        if to_scale == "Celsius":
            return fahrenheit_to_celsius(value)
        elif to_scale == "Kelvin":
            return fahrenheit_to_kelvin(value)
    elif from_scale == "Kelvin":
        if to_scale == "Celsius":
            return kelvin_to_celsius(value)
        elif to_scale == "Fahrenheit":
            return kelvin_to_fahrenheit(value)
    return None

def on_convert_button_click():
    try:
        value = float(entry_value.get())
        from_scale = combo_from.get()
        to_scale = combo_to.get()
        
        if from_scale == to_scale:
            messagebox.showerror("Conversion Error", "Please select different scales for conversion.")
            return

        result = convert_temperature(value, from_scale, to_scale)
        
        if result is not None:
            if to_scale == "Kelvin":
                label_result.config(text=f"Result: {result:.2f} {to_scale}")
            else:
                label_result.config(text=f"Result: {result:.2f}° {to_scale}")
        else:
            label_result.config(text="Result: Conversion error")
            messagebox.showerror("Conversion Error", "Invalid conversion scales entered.")
    except ValueError:
        label_result.config(text="Result: Input error")
        messagebox.showerror("Input Error", "Please enter a valid temperature value.")

def on_reset_button_click():
    entry_value.delete(0, tk.END)
    entry_value.insert(0, str(slider.get()))
    label_result.config(text="Result: --")
    combo_from.current(0)
    combo_to.current(1)
    slider.set(0)

def update_entry_from_slider(value):
    entry_value.delete(0, tk.END)
    entry_value.insert(0, value)

def update_slider_from_entry(*args):
    try:
        value = float(entry_value.get())
        slider.set(value)
    except ValueError:
        pass

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x300")  # Adjusted size
root.minsize(400, 400)    # Minimum size to prevent shrinking too much
root.resizable(False, False)  # Allow resizing

# Define styles
style = ttk.Style()
style.configure("TFrame", background="lightblue")
style.configure("TLabel", background="lightblue", font=("Arial", 12))
style.configure("TButton", background="lightgreen", font=("Arial", 10))

# Create and place the components
frame = ttk.Frame(root, padding="20", style="TFrame")
frame.pack(fill=tk.BOTH, expand=True)

label_value = ttk.Label(frame, text="Enter Temperature:")
label_value.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

entry_value = ttk.Entry(frame, width=10)
entry_value.grid(row=0, column=1, padx=5, pady=5)

slider = tk.Scale(frame, from_=-100, to=200, orient=tk.HORIZONTAL, command=update_entry_from_slider, bg="grey", troughcolor="lightgrey")
slider.set(0)  # Set default slider value
slider.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=tk.EW)

label_from = ttk.Label(frame, text="From:")
label_from.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

combo_from = ttk.Combobox(frame, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
combo_from.grid(row=2, column=1, padx=5, pady=5)
combo_from.current(0)

label_to = ttk.Label(frame, text="To:")
label_to.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

combo_to = ttk.Combobox(frame, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
combo_to.grid(row=3, column=1, padx=5, pady=5)
combo_to.current(1)

button_convert = ttk.Button(frame, text="Convert", command=on_convert_button_click)
button_convert.grid(row=4, column=0, columnspan=2, pady=10)

# Result Section
label_result = ttk.Label(frame, text="Result: --", font=("Arial", 14, "bold"))
label_result.grid(row=5, column=0, columnspan=2, pady=10)

# Reset Button
button_reset = ttk.Button(frame, text="Reset", command=on_reset_button_click)
button_reset.grid(row=6, column=0, columnspan=2, pady=10)

# Configure row and column weights to expand the window properly
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)
frame.rowconfigure(3, weight=1)
frame.rowconfigure(4, weight=1)
frame.rowconfigure(5, weight=1)
frame.rowconfigure(6, weight=1)

# Bind entry value updates to slider
entry_value.bind("<KeyRelease>", update_slider_from_entry)

# Run the application
root.mainloop()
