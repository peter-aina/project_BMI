import customtkinter as ctk
from tkinter import messagebox

def bmi_imperial():
    try:
        # Inputs
        w_pounds = float(w_entry_imperial.get())
        h_feet = float(h_feet_entry_imperial.get())
        h_inches = float(h_inches_entry_imperial.get())

        # Converting from imperial unit to metric unit
        h_meters = ((h_feet * 12) + h_inches) * 0.0254
        w_kg = w_pounds * 0.453592

        # Formula for BMI
        bmi = w_kg / (h_meters ** 2)

        # BMI categories
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        messagebox.showinfo("BMI Result", f"Your BMI is: {bmi:.2f}\nCategory: {category}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numerical values for all fields.")

def bmi_metric():
    try:
        #Inputs
        w_kg = float(w_entry_metric.get())
        h_meters = float(h_meters_entry.get())

        # Formula for BMI
        bmi = w_kg / (h_meters ** 2)

        # BMI categories
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        messagebox.showinfo("BMI Result", f"Your BMI is: {bmi:.2f}\nCategory: {category}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numerical values for all fields.")


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("BMI Calculator")
root.geometry('400x250')

# Notebook for tabs
notebook = ctk.CTkTabview(root, width=350, height=250)
notebook.pack(pady=20)

# Create frames for each tab
imperial_frame = notebook.add("Imperial")
metric_frame = notebook.add("Metric")

# Imperial tab
ctk.CTkLabel(imperial_frame, text="Weight (pounds):", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
w_entry_imperial = ctk.CTkEntry(imperial_frame)
w_entry_imperial.grid(row=0, column=1, padx=10, pady=5)

ctk.CTkLabel(imperial_frame, text="Height (feet):", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5)
h_feet_entry_imperial = ctk.CTkEntry(imperial_frame)
h_feet_entry_imperial.grid(row=1, column=1, padx=10, pady=5)

ctk.CTkLabel(imperial_frame, text="Height (inches):", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5)
h_inches_entry_imperial = ctk.CTkEntry(imperial_frame)
h_inches_entry_imperial.grid(row=2, column=1, padx=10, pady=5)

calculate_imperial_button = ctk.CTkButton(imperial_frame, text="Calculate BMI", command=bmi_imperial)
calculate_imperial_button.grid(row=3, column=0, columnspan=2, pady=10)

# Metric tab
ctk.CTkLabel(metric_frame, text="Weight (kilograms):", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
w_entry_metric = ctk.CTkEntry(metric_frame)
w_entry_metric.grid(row=0, column=1, padx=10, pady=5)

ctk.CTkLabel(metric_frame, text="Height (meters):", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5)
h_meters_entry = ctk.CTkEntry(metric_frame)
h_meters_entry.grid(row=1, column=1, padx=10, pady=5)

calculate_metric_button = ctk.CTkButton(metric_frame, text="Calculate BMI", command=bmi_metric)
calculate_metric_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
