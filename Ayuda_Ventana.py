from tkinter import *
from PIL import ImageTk, Image
import Ayudas

#-----Ventana de Ayuda_ventana-----
Ayuda_ventana = Tk()

Ayuda_ventana.iconbitmap(Ayudas.icono)

Ayuda_ventana.title("Inventario")
Ayuda_ventana.configure(background = Ayudas.azul_claro)

posx = int(Ayuda_ventana.winfo_screenwidth() / 2 - (Ayudas.ancho / 2))
posy = int(Ayuda_ventana.winfo_screenheight() / 2 - (Ayudas.alto / 2))
Ayuda_ventana.geometry("{}x{}+{}+{}".format(Ayudas.ancho, Ayudas.alto, posx, posy))
Ayuda_ventana.resizable(0, 0)

#-----Titulo-----
titulo = Label(Ayuda_ventana, text= "Ayuda", font= Ayudas.titulo, bg= Ayudas.azul_claro, fg= Ayudas.negro_letra)
titulo.place(relx=0.50, rely=0.08)

#-----Logo-----
ImgInterrogacion = ImageTk.PhotoImage(Image.open("Imagenes/interrogacion.png"))
LogoInterrogacion = Label (image = ImgInterrogacion,height = 70 , width= 70, bg= Ayudas.azul_claro)
LogoInterrogacion.place(relx=0.40, rely=0.05)

#-----Botones-----
Boton_Ayuda = Button(height = 4, width = 17 ,text = "Ayuda" , bg = Ayudas.gris, font = Ayudas.subtitulo , fg = Ayudas.blanco  )
Boton_Ayuda.place(relx = 0.378, rely = 0.32)

Boton_AcercaDe = Button(height = 4, width = 17 ,text = "Acerca de..." , bg = Ayudas.gris, font = Ayudas.subtitulo , fg = Ayudas.blanco  )
Boton_AcercaDe.place(relx = 0.378, rely = 0.62)

Ayuda_ventana.mainloop()
