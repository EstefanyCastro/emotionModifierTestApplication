import requests
from PIL import Image, ImageTk
from DALLEConnection import get_image_url


class ImageManager:
    @staticmethod
    # Get the default image
    def get_default_image():
        default_image = Image.open("Images/dog.png")
        resized_default_image = default_image.resize((300, 300))
        return resized_default_image

    @staticmethod
    # Get a new image edit by DALLE based on the response from the API
    def get_new_image(response):
        generated_image_url = get_image_url(
            alegria=response[0],
            tristeza=response[1],
            miedo=response[2],
            enojo=response[3],
            asco=response[4],
            sorpresa=response[5],
        )
        downloaded_image = Image.open(
            requests.get(generated_image_url, stream=True).raw
        )
        resized_image = downloaded_image.resize((300, 300))
        return resized_image

    @staticmethod
    # Show the given image in the specified label
    def show_image_in_label(image, label):
        image_tk = ImageTk.PhotoImage(image)
        label.config(image=image_tk)
        label.image = image_tk

    @staticmethod
    # Update the image and response in the GUI
    def update_image_and_response(response, gui, emotional_bars):
        generated_image = ImageManager.get_new_image(response)
        ImageManager.show_image_in_label(generated_image, gui.image_label)

        # Update the text of the label with the response from the own API
        gui.response_label.config(text=response)
        emotional_bars.update_emotional_bars(response)
