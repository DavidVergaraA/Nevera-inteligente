from tkinter import *
import Ayudas
from PIL import ImageTk, Image
import tkinter.ttk
from tkinter.ttk import Entry
from tkinter.ttk import Button

    #Ventana recuperar_contrasena
recuperar_contrasena = Tk()

recuperar_contrasena.iconbitmap(Ayudas.icono)

recuperar_contrasena.title("Ingreso de Usuario")
recuperar_contrasena.configure(background= Ayudas.blanco)

posx = int(recuperar_contrasena.winfo_screenwidth() / 2 - (Ayudas.ancho / 2))
posy = int(recuperar_contrasena.winfo_screenheight() / 2 - (Ayudas.alto / 2))
recuperar_contrasena.geometry("{}x{}+{}+{}".format(Ayudas.ancho, Ayudas.alto, posx, posy))
recuperar_contrasena.resizable(0, 0)

    #Imagenes
fondo=PhotoImage (file="Imagenes/fondo.png")
lblImagen= Label (recuperar_contrasena, image=fondo)
lblImagen.place(x=209.5, y=93)
lblImagen.configure(borderwidth= 1)

logo=PhotoImage (file="Imagenes/logo.png")
lblImagen= Label (recuperar_contrasena, image=logo)
lblImagen.place(x=283.5, y=16)
lblImagen.configure(borderwidth= 0)

    # Titulo
titulo = Label(recuperar_contrasena, text="Recuperar\n Contraseña", font=Ayudas.titulo, bg=Ayudas.azul_claro,
               fg=Ayudas.negro_letra)
titulo.place(x=280, y=175)

    # Correo
label_correo = Label(recuperar_contrasena, text="Correo :", font=Ayudas.normal, fg=Ayudas.negro_letra,
                     bg=Ayudas.azul_claro)
label_correo.place(x=220, y=280)

entry_correo = Entry(recuperar_contrasena, width=32)
entry_correo.place(x=280, y=280)

    # Botón recuperar_contrasena
buton_ingresar = Button(recuperar_contrasena,
                        text="Confirmar",
                        style="C.TButton")
buton_ingresar.place(x=320, y=375)

recuperar_contrasena.mainloop()