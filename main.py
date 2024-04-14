from tkinter import Tk
from GUI.GUI import GUI


class Main:
    def __init__(self):
        gui = Tk()
        app = GUI(gui)
        gui.mainloop()


# Create the main GUI
if __name__ == "__main__":
    Main()
