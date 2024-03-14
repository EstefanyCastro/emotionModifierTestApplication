import requests
from tkinter import *
from PIL import Image, ImageTk
from conexionAPI import updateNegativeEmotions
from conexionDALLE import obtener_url_imagen_generada

# response = updateNegativeEmotions([10, 10, 10, 10, 10, 10], 5, 10, 5, 20)


# Función para activar la API propia y actualizar la imagen
def activar_api_propia():
    # Llamar a tu función de actualización de emociones negativas
    response = updateNegativeEmotions([10, 10, 10, 10, 10, 10], 5, 10, 5, 20)

    # Extraer valores de la respuesta de la API propia
    alegria = response[0]
    tristeza = response[1]
    miedo = response[2]
    enojo = response[3]
    asco = response[4]
    sorpresa = response[5]

    # Obtener la URL de la imagen generada por DALL-E basada en la respuesta de la API propia
    url_imagen_generada = obtener_url_imagen_generada(
        alegria=alegria,
        tristeza=tristeza,
        miedo=miedo,
        enojo=enojo,
        asco=asco,
        sorpresa=sorpresa,
    )

    # Cargar y mostrar la nueva imagen en la ventana
    mostrar_nueva_imagen(url_imagen_generada)

    # Actualizar el texto del label con la respuesta de la API propia
    label_respuesta.config(text=response)


# Función para cargar y mostrar la nueva imagen en la ventana
def mostrar_nueva_imagen(url_imagen):
    # Descargar la imagen desde la URL
    imagen_descargada = Image.open(requests.get(url_imagen, stream=True).raw)

    # Redimensionar la imagen según sea necesario
    imagen_redimensionada = imagen_descargada.resize((500, 500))

    # Convertir la imagen a un formato compatible con Tkinter
    imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)

    # Mostrar la nueva imagen
    label_imagen.config(image=imagen_tk)
    label_imagen.image = imagen_tk


# Crear la ventana
ventana = Tk()

# Mostrar una imagen predeterminada en la ventana
imagen_predeterminada = Image.open("Imagenes/perro.png")
imagen_predeterminada_redimensionada = imagen_predeterminada.resize((500, 500))
imagen_predeterminada_tk = ImageTk.PhotoImage(imagen_predeterminada_redimensionada)
label_imagen = Label(ventana, image=imagen_predeterminada_tk)
label_imagen.pack()

# Crear un botón para activar la API propia y actualizar la imagen
boton = Button(ventana, text="DALLE", command=activar_api_propia)
boton.pack()

# Crear un label para mostrar la respuesta de la API propia
label_respuesta = Label(ventana, text="")
label_respuesta.pack()

ventana.mainloop()
