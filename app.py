import tkinter as tk

def on_click():
    label.config(text="Button Clicked!")

app = tk.Tk()
app.title("My App")

label = tk.Label(app, text="Hello, World!")
label.pack()

button = tk.Button(app, text="Click Me", command=on_click)
button.pack()

app.mainloop()


