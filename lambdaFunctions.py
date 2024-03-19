class LambdaFunctions:
    @staticmethod
    # Update happiness in the GUI
    def update_happiness(
        gui, emotion_modifier, base_list, image_manager, emotional_bars
    ):
        # Update happiness using the emotion modifier
        result = emotion_modifier.update_happiness(base_list, 5)
        # Update the base list in the GUI
        gui.base_list = result
        # Update the image, emotional bars and response in the GUI
        image_manager.update_image_and_response(result, gui, emotional_bars)

    @staticmethod
    def update_negative_emotions(
        gui, emotion_modifier, base_list, image_manager, emotional_bars
    ):
        result = emotion_modifier.update_negative_emotions(base_list, 2, 3, 4, 1)
        gui.base_list = result
        image_manager.update_image_and_response(result, gui, emotional_bars)
