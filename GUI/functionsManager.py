class FunctionsManager:
    @staticmethod
    # Update functions in the GUI
    def indulge(gui, emotion_modifier, base_list, image_manager, emotional_bars):
        # Adjust negative emotions based on the result of action
        adjust_negative_emotions = emotion_modifier.update_negative_emotions(
            base_list, -5, -2, -3, -1
        )
        # Adjust positive emotions based on the result of action
        adjust_positive_emotions = emotion_modifier.update_positive_emotions(
            adjust_negative_emotions, 10, 2
        )
        # Update the base list in the GUI
        gui.base_list = adjust_positive_emotions
        # Update the image, emotional bars and response in the GUI
        image_manager.update_image_and_response(
            adjust_positive_emotions, gui, emotional_bars
        )

    @staticmethod
    def disgust(gui, emotion_modifier, base_list, image_manager, emotional_bars):
        adjust_negative_emotions = emotion_modifier.update_negative_emotions(
            base_list, -1, -2, -1, 5
        )
        adjust_positive_emotions = emotion_modifier.update_positive_emotions(
            adjust_negative_emotions, -2, 1
        )
        gui.base_list = adjust_positive_emotions
        image_manager.update_image_and_response(
            adjust_positive_emotions, gui, emotional_bars
        )

    @staticmethod
    def hit(gui, emotion_modifier, base_list, image_manager, emotional_bars):
        adjust_negative_emotions = emotion_modifier.update_negative_emotions(
            base_list, 5, 4, 8, 2
        )
        adjust_positive_emotions = emotion_modifier.update_positive_emotions(
            adjust_negative_emotions, -8, 1
        )
        gui.base_list = adjust_positive_emotions
        image_manager.update_image_and_response(
            adjust_positive_emotions, gui, emotional_bars
        )

    @staticmethod
    def caress(gui, emotion_modifier, base_list, image_manager, emotional_bars):
        adjust_negative_emotions = emotion_modifier.update_negative_emotions(
            base_list, -5, -5, -3, -1
        )
        adjust_positive_emotions = emotion_modifier.update_positive_emotions(
            adjust_negative_emotions, 10, 3
        )
        gui.base_list = adjust_positive_emotions
        image_manager.update_image_and_response(
            adjust_positive_emotions, gui, emotional_bars
        )

    @staticmethod
    def leave(gui, emotion_modifier, base_list, image_manager, emotional_bars):
        adjust_negative_emotions = emotion_modifier.update_negative_emotions(
            base_list, 8, 6, 1, -2
        )
        adjust_positive_emotions = emotion_modifier.update_positive_emotions(
            adjust_negative_emotions, -5, -5
        )
        gui.base_list = adjust_positive_emotions
        image_manager.update_image_and_response(
            adjust_positive_emotions, gui, emotional_bars
        )

    @staticmethod
    def shame(gui, emotion_modifier, base_list, image_manager, emotional_bars):
        adjust_negative_emotions = emotion_modifier.update_negative_emotions(
            base_list, 0, 2, 0, 4
        )
        adjust_positive_emotions = emotion_modifier.update_positive_emotions(
            adjust_negative_emotions, -2, -2
        )
        gui.base_list = adjust_positive_emotions
        image_manager.update_image_and_response(
            adjust_positive_emotions, gui, emotional_bars
        )

    @staticmethod
    def guilty(gui, emotion_modifier, base_list, image_manager, emotional_bars):
        adjust_negative_emotions = emotion_modifier.update_negative_emotions(
            base_list, -2, 5, -3, -1
        )
        adjust_positive_emotions = emotion_modifier.update_positive_emotions(
            adjust_negative_emotions, 3, 0
        )
        gui.base_list = adjust_positive_emotions
        image_manager.update_image_and_response(
            adjust_positive_emotions, gui, emotional_bars
        )

    @staticmethod
    def envy(gui, emotion_modifier, base_list, image_manager, emotional_bars):
        adjust_negative_emotions = emotion_modifier.update_negative_emotions(
            base_list, 5, 0, 6, 1
        )
        adjust_positive_emotions = emotion_modifier.update_positive_emotions(
            adjust_negative_emotions, -3, 1
        )
        gui.base_list = adjust_positive_emotions
        image_manager.update_image_and_response(
            adjust_positive_emotions, gui, emotional_bars
        )

    @staticmethod
    def alarm(gui, emotion_modifier, base_list, image_manager, emotional_bars):
        adjust_negative_emotions = emotion_modifier.update_negative_emotions(
            base_list, 1, 7, 2, 1
        )
        adjust_positive_emotions = emotion_modifier.update_positive_emotions(
            adjust_negative_emotions, -5, 5
        )
        gui.base_list = adjust_positive_emotions
        image_manager.update_image_and_response(
            adjust_positive_emotions, gui, emotional_bars
        )

    @staticmethod
    def nag(gui, emotion_modifier, base_list, image_manager, emotional_bars):
        adjust_negative_emotions = emotion_modifier.update_negative_emotions(
            base_list, 6, 3, 1, 0
        )
        adjust_positive_emotions = emotion_modifier.update_positive_emotions(
            adjust_negative_emotions, -3, 2
        )
        gui.base_list = adjust_positive_emotions
        image_manager.update_image_and_response(
            adjust_positive_emotions, gui, emotional_bars
        )
