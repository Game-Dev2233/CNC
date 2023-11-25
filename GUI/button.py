import subprocess
import tkinter as tk
import threading

root = tk.Tk()
root.geometry("550x160")
root.title("CNC GUI")
stop_thread = False

def estop():
    global stop_thread
    stop_thread = True
    exit()

def on_button_click():
    try:
        # run Main.py in a separate thread
        threading.Thread(target=subprocess.run, args=(["Python3", "Main.py"],)).start()
    except Exception as e:
        label.config(text=f"Error: {str(e)}")

def setup():
    # Create the Start CNC machine button
    button_start = tk.Button(root, text="Start CNC Machine", command=on_button_click)
    button_start.pack(pady=10)

    # Warning label
    global label  # Make label global so it can be accessed in the exception block
    label = tk.Label(root, text="Warning do not touch the CNC machine insides while running the CNC machine\n it will kill you")
    label.pack(pady=10)

    # Emergency Shutdown button
    button_estop = tk.Button(root, text="Emergency Stop", command=estop)
    button_estop.pack(pady=10)

def ends():
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    root.mainloop()

# Call the setup function
setup()
