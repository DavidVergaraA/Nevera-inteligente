from tkinter import *
import Ayudas
from PIL import ImageTk, Image
import tkinter.ttk
from tkinter.ttk import Entry
from tkinter.ttk import Button

    #Ventana registrar
registrar = Tk()

registrar.iconbitmap(Ayudas.icono)

registrar.title("Ingreso de Usuario")
registrar.configure(background= Ayudas.blanco)

posx = int(registrar.winfo_screenwidth() / 2 - (Ayudas.ancho / 2))
posy = int(registrar.winfo_screenheight() / 2 - (Ayudas.alto / 2))
registrar.geometry("{}x{}+{}+{}".format(Ayudas.ancho, Ayudas.alto, posx, posy))
registrar.resizable(0, 0)

    #Imagenes
fondo=PhotoImage (file="Imagenes/fondo.png")
lblImagen= Label (registrar, image=fondo)
lblImagen.place(x=209.5, y=93)
lblImagen.configure(borderwidth= 1)

logo=PhotoImage (file="Imagenes/logo.png")
lblImagen= Label (registrar, image=logo)
lblImagen.place(x=283.5, y=16)
lblImagen.configure(borderwidth= 0)

    #Titulo
titulo= Label(registrar, text= "Registrar Usuario", font= Ayudas.titulo, bg= Ayudas.azul_claro, fg= Ayudas.negro_letra)
titulo.place(x=230, y=175)

    #Nombre
label_nombre= Label(registrar, text="Nombre :", font=Ayudas.normal, fg=Ayudas.negro_letra, bg= Ayudas.azul_claro)
label_nombre.place(x=220, y=230)

entry_contrasena = Entry(registrar, width=27)
entry_contrasena.place(x=310.1, y=230)

    #Correo
label_correo= Label(registrar, text="Correo :", font=Ayudas.normal, fg=Ayudas.negro_letra, bg= Ayudas.azul_claro)
label_correo.place(x=220, y=280)

entry_correo = Entry(registrar, width=32)
entry_correo.place(x=280, y=280)

    #Contraseña
label_contrasena= Label(registrar, text="Contraseña :", font=Ayudas.normal, fg=Ayudas.negro_letra, bg= Ayudas.azul_claro)
label_contrasena.place(x=220, y=330)

entry_contrasena = Entry(registrar, width=27)
entry_contrasena.place(x=310.1, y=330)

    #Botón Registrarse
buton_ingresar= Button(registrar,
                       text= "Registrarse",
                       style= "C.TButton")
buton_ingresar.place(x= 320, y= 375)

#Boton volver
boton_volver= Button(registrar,
                    text="Volver")
boton_volver.place(x=600, y=450)

registrar.mainloop()