from openai import OpenAI
from openAIKey import OpenAI_API_Key

# Conexión
client = OpenAI(api_key=OpenAI_API_Key)


def obtener_url_imagen_generada(alegria, tristeza, miedo, enojo, asco, sorpresa):
    response = client.images.edit(
        model="dall-e-2",
        image=open("Imagenes/perro.png", "rb"),
        mask=open("Imagenes/mask_perro.png", "rb"),
        prompt="Perro animado con las siguientes emociones en porcentaje ${alegria} de alegria, ${tristeza} de tristeza, ${miedo} de miedo, ${enojo} de enojo, ${asco} de asco, ${sorpresa} de sorpresa",
        # prompt="Fondo de un cielo despejado, con casas y arboles",
        # prompt="Gato con la lengua afuera y cejas rojas",
        n=1,
        size="1024x1024",
    )

    # Obtén la URL de la imagen generada
    image_url = response.data[0].url
    return image_url
