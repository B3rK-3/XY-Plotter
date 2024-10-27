import eel
import tkinter
from tkinter import filedialog

eel.init("web")


@eel.expose
def selectFolder():
    # Initialize tk object
    root = tkinter.Tk()
    # Set always on top for the Tk window
    root.attributes("-topmost", True)
    # Make it dissappear
    root.withdraw()
    # root.iconbitmap('logo_path') or -window_icon = ImageTk.PhotoImage(file="icon.jpg") root.iconphoto(True, window_icon)- to change upload image logo

    # Open file explorer for image upload
    directory_path = filedialog.askopenfile(
        title="Upload Image", filetypes=[("Image Files", "*.png;*.jpeg;*.jpg")]
    )  # return path of file
    print(directory_path.name)
    return 0


# Start the index.html file
eel.start("index.html")
