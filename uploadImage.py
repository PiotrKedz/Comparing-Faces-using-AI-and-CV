import tkinter as tk
from tkinter import filedialog


def choose_photo_path(image_title):
    root = tk.Tk()
    root.withdraw()

    image_path = filedialog.askopenfilename(
        title=image_title,
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )

    if image_path:
        print("File selected:", image_path)
    else:
        print("No file was selected.")

    return image_path
