from tkinter import *
from PIL import ImageTk, Image
import Ayudas

def PerfilUsuarioVentana():

    #-----Ventana de perfil Usuario-----
    perfil_Usuario = Tk()

    perfil_Usuario.iconbitmap(Ayudas.icono)

    perfil_Usuario.title("Perfil de usuario")
    perfil_Usuario.configure(background = Ayudas.azul_hielo)

    posx = int(perfil_Usuario.winfo_screenwidth() / 2 - (Ayudas.ancho2 / 2))
    posy = int(perfil_Usuario.winfo_screenheight() / 2 - (Ayudas.alto2 / 2))
    perfil_Usuario.geometry("{}x{}+{}+{}".format(Ayudas.ancho2, Ayudas.alto2, posx, posy))
    perfil_Usuario.resizable(0, 0)

    #-----Titulo-----
    titulo = Label(perfil_Usuario, text= "Perfil del usuario", font= Ayudas.titulo, bg= Ayudas.azul_hielo, fg= Ayudas.negro_letra)
    titulo.place(relx = 0.41, rely = 0.06)

    #-----Imagen-----
    ImgCara = ImageTk.PhotoImage(Image.open("Imagenes/cara.png"))
    ImagenCara = Label (image = ImgCara,bg = Ayudas.azul_hielo,height = 180 , width = 210)
    ImagenCara.place(relx = 0.18, rely = 0.2)

    #-----Labels-----
    txtNombre = Label (text = "Nombre: ", bg = Ayudas.azul_hielo , font = Ayudas.subtitulo  )
    txtNombre.place (relx = 0.42, rely = 0.26)
    printNombre = Label (bg = Ayudas.blanco , font = Ayudas.normal , width = 30)
    printNombre.place (relx = 0.52, rely = 0.267)

    txtCorreo = Label (text = "Correo: ", bg = Ayudas.azul_hielo , font = Ayudas.subtitulo  )
    txtCorreo.place (relx = 0.42, rely = 0.34)
    printCorreo = Label (bg = Ayudas.blanco , font = Ayudas.normal , width = 30 )
    printCorreo.place (relx = 0.52, rely = 0.35)

    #-----Botones-----
    Boton_Cambiar_Contrasena = Button(height = 3, width = 17 ,text = "Cambiar contraseña" , bg = Ayudas.gris, font = Ayudas.subtitulo , fg = Ayudas.blanco  )
    Boton_Cambiar_Contrasena.place(relx = 0.6, rely = 0.65)

    #-----AlimentosActuales-----
    TituloAlimentosActuales = Label ( text = "Alimentos necesarios",bg=Ayudas.azul_hielo, font = Ayudas.subtitulo)
    TituloAlimentosActuales.place (relx = 0.176, rely = 0.55)
    AlimentosActuales = Label (bg = Ayudas.blanco, height = 13, width = 44)
    AlimentosActuales.place (relx = 0.133, rely = 0.62 )

    perfil_Usuario.mainloop()

PerfilUsuarioVentana()