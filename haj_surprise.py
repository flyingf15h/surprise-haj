import os
import time
import tkinter as tk
from random import randint
from PIL import Image, ImageTk

# Makes the image popups appear
def display_image(image_path, duration=3, count=16):
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    root.configure(bg='black')
    root.wm_attributes('-transparentcolor', 'black') 
    rootImg = Image.open(image_path)

    # Images stored in the array then deleted
    windows = []  

    # Random size and location for each image in labels in separate windows
    for _ in range(count):
        resize = randint(30, 60)/100.0    
        width = int(rootImg.width * resize)
        height = int(rootImg.height * resize)

        img = rootImg.resize((width, height))
        img = ImageTk.PhotoImage(img)

        window = tk.Toplevel(root)
        window.attributes("-topmost", True)
        window.overrideredirect(True)  
        window.config(bg='black')
        window.wm_attributes('-transparentcolor', 'black') 

        x = randint(20, max(50, root.winfo_screenwidth()-img.width()-20))
        y = randint(20, max(50, root.winfo_screenheight()-img.height()-20))

        window.geometry(f"{img.width()}x{img.height()}+{x}+{y}")
        lbl = tk.Label(window, image=img, bg="black")  
        lbl.pack()
        windows.append((window, img))  

        root.update_idletasks()
        root.update()
        time.sleep(0.1)

    time.sleep(1.5)

    for window, _ in windows:
        window.destroy()
        time.sleep(0.1)

    root.after(duration * 1000 * count, root.destroy)
    root.mainloop()

# Script self deletes itself after executing
def self_delete():
    script_path = os.path.abspath(__file__)
    os.remove(script_path)

# Only runs when directly executed 
if __name__ == "__main__":
    image_path = "blobhaj_heart.png" 
    display_image(image_path)
    time.sleep(1)  
    # self_delete()
