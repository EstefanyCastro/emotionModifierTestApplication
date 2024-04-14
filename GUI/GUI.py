from tkinter import Frame, LEFT, RIGHT, Button, Label
from PIL import ImageTk
from Toolkit.toolkitConnection import ToolkitConnection
from Toolkit.toolkitFunctions import ToolkitFunctions
from .emotionalBarsManager import EmotionalBarsManager
from .imageManager import ImageManager
from .functionsManager import FunctionsManager
from .tooltipManager import TooltipManager


class GUI:
    def __init__(self, window):
        self.window = window
        self.window.configure(bg="white")
        self.window.resizable(False, False)
        self.window.title("My Pet")
        self.base_list = [0, 0, 0, 0, 0, 0]

        # Left Part: Buttons
        self.button_frame = Frame(self.window, bg="white")
        self.button_frame.pack(side=LEFT, padx=10, pady=10)

        indulge_button = Button(
            self.button_frame,
            text="Dar golosina",
            command=lambda: FunctionsManager.indulge(
                self,
                self.emotion_modifier,
                self.base_list,
                self.image_manager,
                self.emotional_bars,
            ),
        )
        indulge_button.pack(pady=5)

        disgust_button = Button(
            self.button_frame,
            text="Oler calcetín sucio",
            command=lambda: FunctionsManager.disgust(
                self,
                self.emotion_modifier,
                self.base_list,
                self.image_manager,
                self.emotional_bars,
            ),
        )
        disgust_button.pack(pady=5)

        hit_button = Button(
            self.button_frame,
            text="Dar golpe",
            command=lambda: FunctionsManager.hit(
                self,
                self.emotion_modifier,
                self.base_list,
                self.image_manager,
                self.emotional_bars,
            ),
        )
        hit_button.pack(pady=5)

        caress_button = Button(
            self.button_frame,
            text="Dar caricia",
            command=lambda: FunctionsManager.caress(
                self,
                self.emotion_modifier,
                self.base_list,
                self.image_manager,
                self.emotional_bars,
            ),
        )
        caress_button.pack(pady=5)

        leave_button = Button(
            self.button_frame,
            text="Dejarlo solo",
            command=lambda: FunctionsManager.leave(
                self,
                self.emotion_modifier,
                self.base_list,
                self.image_manager,
                self.emotional_bars,
            ),
        )
        leave_button.pack(pady=5)

        shame_button = Button(
            self.button_frame,
            text="Orinarse",
            command=lambda: FunctionsManager.shame(
                self,
                self.emotion_modifier,
                self.base_list,
                self.image_manager,
                self.emotional_bars,
            ),
        )
        shame_button.pack(pady=5)

        guilty_button = Button(
            self.button_frame,
            text="Dañar objeto",
            command=lambda: FunctionsManager.guilty(
                self,
                self.emotion_modifier,
                self.base_list,
                self.image_manager,
                self.emotional_bars,
            ),
        )
        guilty_button.pack(pady=5)

        envy_button = Button(
            self.button_frame,
            text="No prestar atención",
            command=lambda: FunctionsManager.envy(
                self,
                self.emotion_modifier,
                self.base_list,
                self.image_manager,
                self.emotional_bars,
            ),
        )
        envy_button.pack(pady=5)

        alarm_button = Button(
            self.button_frame,
            text="Escuchar pirotecnia",
            command=lambda: FunctionsManager.alarm(
                self,
                self.emotion_modifier,
                self.base_list,
                self.image_manager,
                self.emotional_bars,
            ),
        )
        alarm_button.pack(pady=5)

        nag_button = Button(
            self.button_frame,
            text="Regañar",
            command=lambda: FunctionsManager.nag(
                self,
                self.emotion_modifier,
                self.base_list,
                self.image_manager,
                self.emotional_bars,
            ),
        )
        nag_button.pack(pady=5)

        # Right Part: Dog Image
        self.image_frame = Frame(self.window, bg="white")
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
        self.emotional_bars = EmotionalBarsManager(self.window, self.base_list)

        # Create instance of TooltipManager
        self.tooltip_manager = TooltipManager(self.window)

        # Associate events to show and hide tooltips to each button
        for button, tooltip_text in zip(
            [
                indulge_button,
                disgust_button,
                hit_button,
                caress_button,
                leave_button,
                shame_button,
                guilty_button,
                envy_button,
                alarm_button,
                nag_button,
            ],
            [
                "Happiness:10  Sadness:-5  Fear:-2  Anger:-3  Disgust:-1  Surprise:2",
                "Happiness:-2  Sadness:-1  Fear:-2  Anger:-1  Disgust:5  Surprise:1",
                "Happiness:-8  Sadness:5  Fear:4  Anger:8  Disgust:2  Surprise:1",
                "Happiness:10  Sadness:-5  Fear:-5  Anger:-3  Disgust:-1  Surprise:3",
                "Happiness:-5  Sadness:8  Fear:6  Anger:1  Disgust:-2  Surprise:-5",
                "Happiness:-2  Sadness:0  Fear:2  Anger:0  Disgust:4  Surprise:-2",
                "Happiness:3  Sadness:-2  Fear:5  Anger:-3  Disgust:-1  Surprise:0",
                "Happiness:-3  Sadness:5  Fear:0  Anger:6  Disgust:1  Surprise:1",
                "Happiness:-5  Sadness:1  Fear:7  Anger:2  Disgust:1  Surprise:5",
                "Happiness:-3  Sadness:6  Fear:3  Anger:1  Disgust:0  Surprise:2",
            ],
        ):
            button.bind(
                "<Enter>",
                lambda e, t=tooltip_text: self.tooltip_manager.show_tooltip(e, t),
            )
            button.bind("<Leave>", self.tooltip_manager.hide_tooltip)

        # Create an instance of ToolkitConnection
        self.api = ToolkitConnection()

        # Create an instance of ToolkitFunctions
        self.emotion_modifier = ToolkitFunctions(self.api)
