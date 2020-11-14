# Binary response => Image
from PIL import Image, ImageTk
from io import BytesIO
import tkinter as tk

import requests

r = requests.get(url=r"https://images.pexels.com/photos/5804257/pexels-photo-5804257.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260")

# Create an image from binary data returned by a request
i = Image.open(BytesIO(r.content))

# GUI window from tkinter toolkit
window = tk.Tk()
photo = ImageTk.PhotoImage(i)
canvas = tk.Canvas(window, width = 1000, height = 1000)
canvas.pack()
canvas.create_image(500, 500, image=photo)
window.mainloop()