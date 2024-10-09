import tkinter as tk
from tkinter import messagebox

def show_loading_screen():
    loading_window = tk.Toplevel(root)
    loading_window.title("Loading")
    loading_label = tk.Label(loading_window, text="Loading...")
    loading_label.pack(padx=50, pady=20)

    # Simulate loading process (you can replace this with your actual logic)
    # Here, we're using the `after` method to schedule a callback after a delay
    root.after(3000, lambda: show_message(loading_window))

def show_message(loading_window):
    loading_window.destroy()  # Close the loading window

    # Display a message box with a message
    messagebox.showinfo("Message", "Loading complete!")

root = tk.Tk()
root.title("Loading App")

# Create a button that triggers the loading screen
button = tk.Button(root, text="Press me!", command=show_loading_screen)
button.pack(padx=50, pady=20)

root.mainloop()
