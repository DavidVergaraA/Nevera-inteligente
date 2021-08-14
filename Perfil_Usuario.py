from tkinter import *
from PIL import ImageTk, Image
import Ayudas

#-----Ventana de perfil Usuario-----
perfil_Usuario = Tk()

perfil_Usuario.iconbitmap(Ayudas.icono)

perfil_Usuario.title("Perfil de usuario")
perfil_Usuario.configure(background = Ayudas.azul_hielo)

posx = int(perfil_Usuario.winfo_screenwidth() / 2 - (Ayudas.ancho / 2))
posy = int(perfil_Usuario.winfo_screenheight() / 2 - (Ayudas.alto / 2))
perfil_Usuario.geometry("{}x{}+{}+{}".format(Ayudas.ancho, Ayudas.alto, posx, posy))
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


perfil_Usuario.mainloop()
