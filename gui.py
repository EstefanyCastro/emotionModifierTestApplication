from tkinter import *
from PIL import ImageTk
from lambdaAPI import LambdaAPI
from emotionModifier import EmotionModifier
from emotionalBars import EmotionalBars
from imageManager import ImageManager
from lambdaFunctions import LambdaFunctions


class GUI:
    def __init__(self, gui):
        self.gui = gui
        self.gui.title("My Pet")
        self.base_list = [0, 0, 0, 0, 0, 0]

        # Left Part: Buttons
        self.button_frame = Frame(self.gui)
        self.button_frame.pack(side=LEFT, padx=10, pady=10)

        happiness_button = Button(
            self.button_frame,
            text="Update Happiness",
            command=lambda: LambdaFunctions.update_happiness(
                self,
                self.emotion_modifier,
                self.base_list,
                self.image_manager,
                self.emotional_bars,
            ),
        )
        happiness_button.pack(pady=5)

        negative_emotions_button = Button(
            self.button_frame,
            text="Update negative emotions",
            command=lambda: LambdaFunctions.update_negative_emotions(
                self,
                self.emotion_modifier,
                self.base_list,
                self.image_manager,
                self.emotional_bars,
            ),
        )
        negative_emotions_button.pack(pady=5)

        # Right Part: Dog Image
        self.image_frame = Frame(self.gui)
        self.image_frame.pack(side=RIGHT, padx=10, pady=10)

        # Create an instance of ImageManager
        self.image_manager = ImageManager()

        default_image = self.image_manager.get_default_image()
        self.default_image_tk = ImageTk.PhotoImage(default_image)

        self.image_label = Label(self.image_frame, image=self.default_image_tk)
        self.image_label.pack()

        # Label to display the response from the own API
        self.response_label = Label(self.image_frame, text="")
        self.response_label.pack()

        # Bottom Part: Emotional Bars
        self.emotional_bars = EmotionalBars(self.gui, self.base_list)

        # Create an instance of the LambdaAPI class with the URL of the Lambda API
        self.api = LambdaAPI()

        # Create an instance of the EmotionModifier class with the instance of LambdaAPI created earlier.
        self.emotion_modifier = EmotionModifier(self.api)
