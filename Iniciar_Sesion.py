from tkinter import *
import Ayudas
from PIL import ImageTk, Image
import tkinter.ttk
from tkinter.ttk import Entry
from tkinter.ttk import Button

    #Ventana Principal
principal = Tk()

principal.iconbitmap(Ayudas.icono)

principal.title("Ingreso de Usuario")
principal.configure(background= Ayudas.blanco)

posx = int(principal.winfo_screenwidth() / 2 - (Ayudas.ancho / 2))
posy = int(principal.winfo_screenheight() / 2 - (Ayudas.alto / 2))
principal.geometry("{}x{}+{}+{}".format(Ayudas.ancho, Ayudas.alto, posx, posy))
principal.resizable(0, 0)

    #Imagenes
fondo=PhotoImage (file="Imagenes/fondo.png")
lblImagen= Label (principal, image=fondo)
lblImagen.place(x=209.5, y=93)
lblImagen.configure(borderwidth= 1)

logo=PhotoImage (file="Imagenes/logo.png")
lblImagen= Label (principal, image=logo)
lblImagen.place(x=283.5, y=16)
lblImagen.configure(borderwidth= 0)

    #Titulo
titulo= Label(principal, text= "Iniciar Sesión", font= Ayudas.titulo, bg= Ayudas.azul_claro, fg= Ayudas.negro_letra)
titulo.place(x=260, y=180)

    #Correo
label_correo= Label(principal, text="Correo :", font=Ayudas.normal, fg=Ayudas.negro_letra, bg= Ayudas.azul_claro)
label_correo.place(x=220, y=230)

entry_correo = Entry(principal, width=32)
entry_correo.place(x=280, y=230)

    #Contraseña
label_contrasena= Label(principal, text="Contraseña :", font=Ayudas.normal, fg=Ayudas.negro_letra, bg= Ayudas.azul_claro)
label_contrasena.place(x=220, y=270)

entry_contrasena = Entry(principal, width=27)
entry_contrasena.place(x=310.1, y=270)

    #Botón Ingresar
buton_ingresar= Button(principal,
                       text= "Ingresar",
                       style= "C.TButton")
buton_ingresar.place(x= 320, y= 310)

    #Boton salir
boton_salir= Button(principal,
                    text="Salir",
                    command= principal.destroy)
boton_salir.place(x=600, y=450)

    #Olvidar contraseña
olvidar_contrasena= Label(principal, text= "¿Olvidaste tu contraseña?", font= Ayudas.normal, bg= Ayudas.azul_claro, fg= Ayudas.negro_letra)
olvidar_contrasena.place(x=275, y=350)

    #Registrarse
registrarse= Label(principal, text= "Crear nueva cuenta", font= Ayudas.normal, bg= Ayudas.azul_claro, fg= Ayudas.negro_letra)
registrarse.place(x=293, y=372)

principal.mainloop()