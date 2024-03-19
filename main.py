from tkinter import Tk
from gui import GUI


class MainGUI:
    def __init__(self):
        gui = Tk()
        app = GUI(gui)
        gui.mainloop()


# Create the main GUI
if __name__ == "__main__":
    MainGUI()
