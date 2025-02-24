#Author: Mason Betz
#Module 6: Project Milestone 2
#Date: 2/23/2025

import tkinter as tk
from tkinter import messagebox

# Global variables to store order details
order_details = {
    "ice_cream": None,
    "toppings": [],
    "size": None,
}

# Prices for selections
prices = {
    "small": 5,
    "medium": 7,
    "large": 9,
    "chocolate": 1,
    "vanilla": 1,
    "strawberry": 1,
    "sprinkles": 0.5,
    "chocolate_syrup": 0.5,
    "whipped_cream": 0.5,
}


# Function to go to the second page
def start_order():
    welcome_page.pack_forget()
    ordering_page.pack()


# Function to save the ice cream choice
def select_ice_cream(ice_cream):
    order_details["ice_cream"] = ice_cream


# Function to save the topping choice
def select_topping(topping, var):
    if var.get():
        order_details["toppings"].append(topping)
    else:
        order_details["toppings"].remove(topping)


# Function to save the size choice
def select_size(size):
    order_details["size"] = size


# Function to finish the order and show the summary
def done_ordering():
    ordering_page.pack_forget()
    summary_page.pack()

    # Calculate the total cost
    total_cost = prices[order_details["size"]]
    for topping in order_details["toppings"]:
        total_cost += prices[topping]
    total_cost += prices[order_details["ice_cream"]]

    # Display the summary
    summary_label.config(
        text=f"Milkshake Summary:\n\n"
             f"Ice Cream: {order_details['ice_cream']}\n"
             f"Size: {order_details['size']}\n"
             f"Toppings: {', '.join(order_details['toppings'])}\n\n"
             f"Total Cost: ${total_cost:.2f}"
    )


# Initialize the main window
root = tk.Tk()
root.title("Milkshake Ordering Program")

# Welcome Page (Page 1)
welcome_page = tk.Frame(root)
welcome_label = tk.Label(welcome_page, text="Welcome to the Milkshake Ordering Program!")
welcome_label.pack(pady=20)
start_button = tk.Button(welcome_page, text="Start", command=start_order)
start_button.pack(pady=10)
welcome_page.pack()

# Ordering Page (Page 2)
ordering_page = tk.Frame(root)

# Ice Cream Selection
ice_cream_label = tk.Label(ordering_page, text="Select your Ice Cream Flavor:")
ice_cream_label.pack()

ice_cream_options = ["chocolate", "vanilla", "strawberry"]
for option in ice_cream_options:
    button = tk.Button(ordering_page, text=option.capitalize(),
                       command=lambda option=option: select_ice_cream(option))
    button.pack(pady=5)

# Topping Selection
topping_label = tk.Label(ordering_page, text="Select your Toppings:")
topping_label.pack()

topping_options = ["sprinkles", "chocolate_syrup", "whipped_cream"]
topping_vars = {}
for topping in topping_options:
    var = tk.BooleanVar()
    topping_vars[topping] = var
    checkbox = tk.Checkbutton(ordering_page, text=topping.capitalize(),
                              variable=var,
                              command=lambda topping=topping, var=var: select_topping(topping, var))
    checkbox.pack(pady=5)

# Size Selection
size_label = tk.Label(ordering_page, text="Select your Milkshake Size:")
size_label.pack()

size_options = ["small", "medium", "large"]
for size in size_options:
    button = tk.Button(ordering_page, text=size.capitalize(),
                       command=lambda size=size: select_size(size))
    button.pack(pady=5)

# Done Button
done_button = tk.Button(ordering_page, text="Done", command=done_ordering)
done_button.pack(pady=20)

# Summary Page (Page 3)
summary_page = tk.Frame(root)

summary_label = tk.Label(summary_page, text="Milkshake Summary will appear here.")
summary_label.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
