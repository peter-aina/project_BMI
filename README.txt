BMI Calculator

Overview
This project is a BMI (Body Mass Index) Calculator built with Python using the 'customtkinter' library. It provides a modern, user-friendly interface for calculating BMI based on a user's weight and height in imperial measurement systems by default but with the option to use the metric system.

Features
- Supports Imperial Systems and Metric:
  - Imperial: Weight in pounds, height in feet and inches.
  - Metric: Weight in kilograms, height in meters.
- Tabbed Interface: Separate tabs for imperial and metric input.
- Real-Time Calculations: Automatically calculates BMI when the user inputs their values and clicks "Calculate BMI."
- Error Handling: Alerts the user if invalid input is provided.
- Categorization: Displays the BMI value and category (Underweight, Normal weight, Overweight, or Obese).

Requirements
To run the project, ensure you have the following installed:
- Python 3.7 or higher
- `customtkinter` library
- IDE

Installation
1. Install the required library using pip:
   pip install customtkinter

2. Run the script using Python:
   BMI_Calculator_CustomTkinter.py

How to Use
1. Run the Python program
2. Choose the Imperial or Metric tab based on your preferred measurement system.
3. Enter your weight and height in the respective fields:
   - For Imperial: Enter weight in pounds, height in feet and inches.
   - For Metric: Enter weight in kilograms and height in meters.
4. Click the "Calculate BMI" button.
5. View the BMI value and category displayed in a popup.

BMI Categories
The calculator determines the BMI category based on the following ranges:
- Underweight: BMI < 18.5
- Normal weight: BMI 18.5 - 24.9
- Overweight: BMI 25 - 29.9
- Obese: BMI ≥ 30

Project Structure
- bmi_calculator.py: Main Python script containing the implementation of the BMI Calculator.

Key Functions
`bmi_imperial()`
- Converts imperial inputs (pounds, feet, inches) to metric units.
- Calculates BMI and determines the category.
- Displays the result using a popup message.

`bmi_metric()`
- Directly uses metric inputs (kilograms, meters).
- Calculates BMI and determines the category.
- Displays the result using a popup message.

CustomTkinter Highlights
This project uses `customtkinter` to enhance the visual appeal and functionality:
- Dark Mode: This theme is used.
- Polished UI Elements: Provides modern widgets like `CTkTabview`, `CTkEntry`, and `CTkButton`.

Future Enhancements
- Add support for additional languages.
- Include more detailed health recommendations based on BMI.
- Save results for future reference.

License
This project is open-source and free to use.

Acknowledgements
- Developed using the `customtkinter` library.
- Inspired by the need for a simple yet modern BMI Calculator with user friendly interface.

---
Feel free to contribute to the project or suggest improvements!

