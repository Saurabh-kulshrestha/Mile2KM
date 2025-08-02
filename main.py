# This project is for converting Miles to Kilometers using Tkinter

from tkinter import *

# Create the main window
window = Tk()
window.title("Mile to Km converter")  # Window title
window.minsize(width=300, height=200)  # Minimum size of window
window.config(padx=50, pady=50)  # Padding around the content

# ---------------------- Converter Function ----------------------
def converter():
    M = float(input.get())  # Get value from input box and convert to float
    Km = M * 1.60934  # Convert miles to kilometers
    result["text"] = Km  # Show result in the label
    input.delete(0, END)  # Clear input box after conversion

# ---------------------- UI Elements ----------------------

# Label: "is equal to"
equal = Label(text="is equal to", font=("Arial", 20, "bold"))
equal.grid(column=0, row=1)

# Entry box for user input (in miles)
input = Entry(width=15, font=("Arial", 20), bd=1, relief="solid")
input.grid(column=1, row=0)

# Label to show result (converted kilometers)
result = Label(text="0", font=("Arial", 20, "bold"))
result.grid(column=1, row=1)

# Button to trigger the converter function
button = Button(text="Calculate", font=("Arial", 20, "bold"), command=converter)
button.grid(column=1, row=2)

# Label: "Km"
km = Label(text="Km", font=("Arial", 20, "bold"))
km.grid(column=2, row=1)

# Run the Tkinter event loop
window.mainloop()
