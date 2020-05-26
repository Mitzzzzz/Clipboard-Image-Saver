from PIL import ImageGrab, Image
from glob import glob
from io import BytesIO
import time
import tkinter as tk

window = None
entry = None
name_of_file = None


def handle_click(event):
    global name_of_file
    name_of_file = entry.get()
    label = tk.Label(text="Please Enter a file name")
    if name_of_file != "":
        print("You Entered " + name_of_file)
        entry.delete(0, tk.END)
        window.destroy()
    else:
        label.pack()


def create_window():
    global window
    global entry
    window = tk.Tk()
    window.geometry("600x600")
    window.title("Name for your image")
    label = tk.Label(text="What do you want to name the image?")
    entry = tk.Entry()
    button = tk.Button(text="Create")
    button.bind("<Button-1>", handle_click)
    window.bind("<Return>", handle_click)
    label.pack()
    entry.pack()
    entry.focus_set()
    button.pack()
    window.lift()
    window.attributes("-topmost", True)
    window.mainloop()


while True:
    print("Looping")
    image_list = map(Image.open, glob('*.png'))
    presentItem = ImageGrab.grabclipboard()
    if presentItem is not None:
        with BytesIO() as f:
            presentItem.save(f, format='PNG')
            x = Image.open(f)
            if x not in image_list:
                print("New item found")
                create_window()
                presentItem.save(name_of_file + '.png', 'PNG')
    else:
        print("No item in clipboard")
    time.sleep(0.1)
