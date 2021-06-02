from PIL import ImageTk, Image

class Ayudas:

    #Colores:

    azul_hielo = '#d7fffe'
    blanco = '#FFFFFF'
    naranja = '#E59866'
    gris = '#CCCCCC'
    negro = '#000000'

    #Tipos de letras
    #Letras family, size,weight: bold or normal, slant: italic or roman, underline, overstrike

    letra_grande= ("Arial 20 bold roman")
    letra_mediana = ("Arial 16 bold roman")
    letra_pequeña = ("Arial 12 bold roman")

    #Imagenes
    imagen1 = Image.open("imagenes/nevera2.jpg").resize((100,100), Image.ANTIALIAS)