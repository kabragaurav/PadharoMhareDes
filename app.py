import tkinter as tk
import webbrowser

def open_website():
    webbrowser.open("https://gauravkabra.netlify.app/")

# Initialize main window with custom dimensions, title, and resizing behavior
root = tk.Tk()
root.title("Explore Gaurav Kabra's Portfolio")
root.geometry("500x400")
root.configure(bg="#1e1e2f")  # Dark background for contrast
root.minsize(500, 400)

# Canvas for background gradient and layout
canvas = tk.Canvas(root, width=500, height=400, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Function to create gradient background on canvas resize
def create_gradient(event=None):
    canvas.delete("gradient")
    width, height = root.winfo_width(), root.winfo_height()
    gradient_colors = ["#1e1e2f", "#343650", "#4a4a6a", "#616184", "#79799f"]
    num_colors = len(gradient_colors)
    for i in range(num_colors):
        color = gradient_colors[i]
        y1 = int(i * height / num_colors)
        y2 = int((i + 1) * height / num_colors)
        canvas.create_rectangle(0, y1, width, y2, outline="", fill=color, tags="gradient")

# Bind gradient creation to window resize
root.bind("<Configure>", create_gradient)

# Heading Text
heading = tk.Label(root, text="Welcome to My World!", font=("Helvetica Neue", 18, "bold"),
                   fg="#ffffff", bg="#1e1e2f", padx=20, pady=10)
heading_window = canvas.create_window(250, 120, window=heading, anchor="center")

# Description Text
description = tk.Label(root, text="Explore my projects, skills, and more on my website.",
                       font=("Arial", 12), fg="#dddddd", bg="#1e1e2f", wraplength=350, justify="center")
description_window = canvas.create_window(250, 180, window=description, anchor="center")

# Button style and hover effects
def on_enter(e):
    visit_button.config(bg="#ffb703", fg="#ffffff")

def on_leave(e):
    visit_button.config(bg="#fb8500", fg="#1e1e2f")

# Visit Button with rounded corners and hover effects
visit_button = tk.Button(root, text="Visit My Website", font=("Helvetica Neue", 14, "bold"),
                         bg="#fb8500", fg="#1e1e2f", activebackground="#ffb703", activeforeground="#ffffff",
                         command=open_website, relief="flat", cursor="hand2", width=20, height=2)
visit_button.bind("<Enter>", on_enter)
visit_button.bind("<Leave>", on_leave)

# Position button in the center of the canvas
visit_button_window = canvas.create_window(250, 280, window=visit_button, anchor="center")

# Run the application
root.mainloop()
