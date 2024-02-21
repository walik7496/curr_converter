import tkinter as tk
from tkinter import messagebox
import requests

def convert_currency():
    amount = float(entry_amount.get())
    from_currency = entry_from_currency.get().upper()
    to_currency = entry_to_currency.get().upper()

    url = f"https://www.google.com/search?q={amount}+{from_currency}+to+{to_currency}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        result = response.text.split(' = ')[1].split()[0]
        label_result.config(text=f"{amount} {from_currency} = {result} {to_currency}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Creating a window
window = tk.Tk()
window.title("Currency Converter")

# Creating and placing widgets
label_amount = tk.Label(window, text="Amount:")
label_amount.grid(row=0, column=0)

entry_amount = tk.Entry(window)
entry_amount.grid(row=0, column=1)

label_from_currency = tk.Label(window, text="From Currency:")
label_from_currency.grid(row=1, column=0)

entry_from_currency = tk.Entry(window)
entry_from_currency.grid(row=1, column=1)

label_to_currency = tk.Label(window, text="To Currency:")
label_to_currency.grid(row=2, column=0)

entry_to_currency = tk.Entry(window)
entry_to_currency.grid(row=2, column=1)

button_convert = tk.Button(window, text="Convert", command=convert_currency)
button_convert.grid(row=3, column=0, columnspan=2)

label_result = tk.Label(window, text="")
label_result.grid(row=4, column=0, columnspan=2)

window.mainloop()