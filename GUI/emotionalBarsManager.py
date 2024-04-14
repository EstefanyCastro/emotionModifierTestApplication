import matplotlib.pyplot as plt
from tkinter import Frame, BOTTOM
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# List of emotions and colors
EMOTIONS = ["Happiness", "Sadness", "Fear", "Anger", "Disgust", "Surprise"]
COLORS = ["yellow", "blue", "violet", "red", "green", "orange"]


class EmotionalBarsManager:
    def __init__(self, parent, base_list):
        # Initialize emotional bars
        self.parent = parent
        self.base_list = base_list
        self.bar_width = 0.4
        self.fig_size = (5, 3)

        # Create a frame to contain the emotional bars
        self.emotional_bars_frame = Frame(self.parent)
        self.emotional_bars_frame.pack(side=BOTTOM, padx=10, pady=10)

        self.init_emotional_bars()

    def init_emotional_bars(self):
        # Create a figure and axis for the emotional bars with the specified size
        self.fig, self.ax = plt.subplots(figsize=self.fig_size)

        # Plot the emotional bars
        self.plot_bars()

        # Embed the plot into a Tkinter canvas and pack it into the frame
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.emotional_bars_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

    def plot_bars(self):
        # Plot the bars with specified colors and bar width
        self.bars = self.ax.bar(
            EMOTIONS, self.base_list, width=self.bar_width, color=COLORS
        )

    def update_emotional_bars(self, base_list):
        # Update the base list of emotions and adjust the heights of the bars accordingly
        self.base_list = base_list
        for bar, value in zip(self.bars, self.base_list):
            bar.set_height(value)

        # Adjust the y-axis limits and redraw the canvas to reflect the changes
        self.ax.set_ylim(0, max(self.base_list) + 1)
        self.canvas.draw()
