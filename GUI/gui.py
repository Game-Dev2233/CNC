import tkinter as tk
import subprocess

def on_button_click():
    try:
        # run Main.py
        subprocess.run(["Python", "Main.py"])
    except Exception as e:
        label.config(text=f"Error: {str(e)}")

# Create the Window
root = tk.Tk()
root.geometry("500x150")
root.title("CNC GUI")
# Add Start CNC lable
label = tk.Label(root, text="Start CNC machine")
label.pack(pady=10)
# Create the Start CNC machine button
button = tk.Button(root, text="Start CNC Machine", command=on_button_click)
button.pack(pady=10)
# Warning label
label = tk.Label(root, text="Warning do not touch the CNC machine insides while running the CNC machine")
label.pack(pady=10)
# exit stuff
root.protocol("WM_DELETE_WINDOW", root.destroy)
root.mainloop()
