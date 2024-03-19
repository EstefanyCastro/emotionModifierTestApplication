from openai import OpenAI
from openAIKey import OpenAI_Key

# Initialize OpenAI client
client = OpenAI(api_key=OpenAI_Key)


def get_image_url(alegria, tristeza, miedo, enojo, asco, sorpresa):
    # Call OpenAI's image editing API to generate an image
    response = client.images.edit(
        model="dall-e-2",
        image=open("Images/dog.png", "rb"),
        mask=open("Images/mask_dog.png", "rb"),
        prompt="´Perro animado con las siguientes emociones en porcentajes: "
        f"${alegria} alegria, "
        f"${tristeza} tristeza, "
        f"${miedo} miedo, "
        f"${enojo} enojo, "
        f"${asco} asco, "
        f"${sorpresa} sorpresa",
        n=1,
        size="256x256",
    )

    # Get the URL of the generated image
    image_url = response.data[0].url
    return image_url
