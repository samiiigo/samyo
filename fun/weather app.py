from customtkinter import *

set_appearance_mode("System")
set_default_color_theme("green")

def get_ans(event):
    global num
    num = entry.get()
    loading_win()

def ans():
    global num
    num = entry.get()
    loading_win()

def loading_win():
    loading_window = CTkFrame(main,width=300,height=260)
    loading_window.place(relx=0.5, rely=0.5, anchor=CENTER)

    loading_label = CTkLabel(loading_window,width=260, text="Analyzing Brainwaves...")
    loading_label.pack(padx=10, pady=10)

    progress = CTkProgressBar(loading_window, mode='indeterminate')
    progress.pack(padx = 20, pady=30)

    # Simulate loading process (you can replace this with your actual logic)
    # Here, we're using the `after` method to schedule a callback after a delay
    progress.start()  # Start the progress bar

    # Update the loading text periodically
    def update_loading_text():
        l = ["Searching Location...","Analyzing the clouds...","Looking outside your window...","Gathering last information..."]
            
        loading_label.configure(text=l[count],font=('Dubai',15))
        loading_window.after(500, update_loading_text)

    # Simulate loading process (you can replace this with your actual logic)
    count = -1
    def simulate_loading():
        nonlocal count
        count += 1
        if count < 3:
            loading_window.after(2000, simulate_loading)
        else:
            progress.stop()  # Stop the progress bar
            loading_window.after(10, lambda: show_message(loading_window,progress))

    update_loading_text()
    loading_window.after(1000, simulate_loading)

def show_message(loading_window, progress):
    progress.stop()  # Stop the progress bar
    loading_window.destroy()  # Close the loading window

    # Display a message box with a message
    ans_window = CTkFrame(main,width=300,height=260)
    ans_window.place(relx=0.5, rely=0.5, anchor=CENTER)

    label = CTkLabel(ans_window, text="IDK, just look outside",width=260, font=('Dubai',15))
    label.pack(padx=20,pady=80)

    root.after(5000,lambda:ans_window.destroy())

root = CTk()
root.geometry("300x260")
root.title("AI Weather Forecast")

# Create a button that triggers the loading screen
main = CTkFrame(root, width=300, height=220, corner_radius=10)
main.place(relx=0.5, rely=0.6, anchor=CENTER)
title = CTkLabel(root, corner_radius=10, text='AI Weather Forecast' , font=('Dubai',25))
title.place(relx=0.5, rely=0.1, anchor=CENTER)

qn = CTkLabel(main, text="Enter your Location:", font=('Dubai',18))
qn.place(relx=0.5, rely=0.3, anchor=CENTER)

entry = CTkEntry(main, placeholder_text="Enter Location", width=200, border_width=2, corner_radius=10)
entry.place(relx=0.5, rely=0.5, anchor=CENTER)

button_guess = CTkButton(main, text="Search", width=15, border_width=0, corner_radius=8, command=ans)
button_guess.place(relx=0.5, rely=0.7, anchor=CENTER)

root.bind('<Return>', get_ans)  

root.mainloop()