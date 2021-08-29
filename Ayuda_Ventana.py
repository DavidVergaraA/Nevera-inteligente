from tkinter import *
from PIL import ImageTk, Image
import Ayudas
#from MenuBar import MenuClass

def Ayuda_Ventana(Ayuda_ventana):
        
    #-----Ventana de Ayuda_ventana-----
    Ayuda_ventana.iconbitmap(Ayudas.icono)

    Ayuda_ventana.title("Inventario")
    Ayuda_ventana.configure(background=Ayudas.azul_hielo)

    posx = int(Ayuda_ventana.winfo_screenwidth() / 2 - (Ayudas.ancho2 / 2))
    posy = int(Ayuda_ventana.winfo_screenheight() / 2 - (Ayudas.alto2 / 2))
    Ayuda_ventana.geometry(
        "{}x{}+{}+{}".format(Ayudas.ancho2, Ayudas.alto2, posx, posy))
    Ayuda_ventana.resizable(0, 0)

    #-----Titulo-----
    titulo = Label(Ayuda_ventana, text="Ayuda", font=Ayudas.titulo,
                bg=Ayudas.azul_hielo, fg=Ayudas.negro_letra)
    titulo.place(relx=0.50, rely=0.08)

    #-----Logo-----
    global ImgInterrogacion
    ImgInterrogacion = ImageTk.PhotoImage(
        Image.open("Imagenes/interrogacion.png"))
    LogoInterrogacion = Label(Ayuda_ventana,image=ImgInterrogacion,
                            height=70, width=70, bg=Ayudas.azul_hielo)
    LogoInterrogacion.place(relx=0.40, rely=0.05)

    #-----Botones-----
    Boton_Ayuda = Button(Ayuda_ventana,height=4, width=17, text="Ayuda",
                        bg=Ayudas.gris, font=Ayudas.subtitulo, fg=Ayudas.blanco)
    Boton_Ayuda.place(relx=0.378, rely=0.32)

    Boton_AcercaDe = Button(Ayuda_ventana,height=4, width=17, text="Acerca de...",
                            bg=Ayudas.gris, font=Ayudas.subtitulo, fg=Ayudas.blanco)
    Boton_AcercaDe.place(relx=0.378, rely=0.62)
