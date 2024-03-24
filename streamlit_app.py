import tkinter as tk
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("300x200")  # Set window size
weight_label = tk.Label(window, text="Weight (kg):")
weight_label.pack()

weight_entry = tk.Entry(window)
weight_entry.pack()

height_label = tk.Label(window, text="Height (cm):")
height_label.pack()

height_entry = tk.Entry(window)
height_entry.pack()
def calculate_bmi():
  try:
    weight = float(weight_entry.get())
    height = float(height_entry.get()) / 100  # Convert cm to meters

    bmi = weight / height**2

    bmi_label = tk.Label(window, text="BMI: {:.2f}".format(bmi))
    bmi_label.pack()

    category_label = tk.Label(window, text="")
    if bmi < 18.5:
      category_label.config(text="Category: Underweight")
    elif bmi < 25:
      category_label.config(text="Category: Normal")
    elif bmi < 30:
      category_label.config(text="Category: Overweight")
    else:
      category_label.config(text="Category: Obese")
    category_label.pack()

  except ValueError:
    # Handle invalid input (non-numeric values)
    pass

calculate_button = tk.Button(window, text="Calculate", command=calculate_bmi)
calculate_button.pack()
window.mainloop()
