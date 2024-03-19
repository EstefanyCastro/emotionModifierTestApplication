import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class EmotionalBars:
    def __init__(self, parent, base_list):
        # Initialize EmotionalBars with a parent widget and a base list of emotions
        self.base_list = base_list
        self.parent = parent

        # Create a frame to contain the emotional bars
        self.emotional_bars_frame = Frame(self.parent)
        self.emotional_bars_frame.pack(side=BOTTOM, padx=10, pady=10)

        # Initialize emotional bars
        self.init_emotional_bars()

    # Function to initialize emotional bars
    def init_emotional_bars(self):
        # Create a figure and axis for the emotional bars, adjust the size
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.emotions = ["Happiness", "Sadness", "Fear", "Anger", "Disgust", "Surprise"]
        self.bars = self.ax.bar(self.emotions, self.base_list)

        # Embed the plot into a Tkinter canvas and pack it into the frame
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.emotional_bars_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

    # Function to update emotional bars
    def update_emotional_bars(self, base_list):
        # Update the base list of emotions and adjust the heights of the bars accordingly
        self.base_list = base_list
        for bar, value in zip(self.bars, self.base_list):
            bar.set_height(value)

        # Adjust the y-axis limits and redraw the canvas to reflect the changes
        self.ax.set_ylim(0, max(self.base_list) + 1)
        self.canvas.draw()
