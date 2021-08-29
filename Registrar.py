from tkinter import *
import Ayudas
from PIL import ImageTk, Image
import tkinter.ttk
from tkinter.ttk import Entry
from tkinter.ttk import Button

def Registrar_Ventana(registro):

    registro = Tk()

    registro.iconbitmap(Ayudas.icono)

    registro.title("Registrar Usuario")

    registro.configure(bg = Ayudas.blanco)
    posx = int(registro.winfo_screenwidth() / 2 - (Ayudas.ancho / 2))
    posy = int(registro.winfo_screenheight() / 2 - (Ayudas.alto / 2))
    registro.geometry(
        "{}x{}+{}+{}".format(Ayudas.ancho, Ayudas.alto, posx, posy))
    registro.resizable(0, 0)

    # -----Imagenes-----
    Imgfondo = ImageTk.PhotoImage(Image.open("Imagenes/fondo.png"))
    Logofondo = Label(image=Imgfondo, height=355, width=300, bg=Ayudas.azul_claro)
    Logofondo.place(in_=registro, anchor= "c", relx=0.5, rely=0.545)

    Imglogo = ImageTk.PhotoImage(Image.open("Imagenes/logo.png"))
    Logologo = Label(image=Imglogo, height=154, width=154, bd=0 )
    Logologo.place(relx=0.4, rely=0.061)

    #-----Titulo-----
    titulo= Label(registro, text= "Registrarse", font= Ayudas.titulo, bg= Ayudas.azul_claro, fg= Ayudas.negro_letra)
    titulo.place(in_=registro, anchor="c", relx=0.5, rely=0.4)

    registro.overrideredirect(1)

    def crear_barra():
        barra = Frame(registro, bd=1, relief = RAISED)

        def salir():
            registro.quit()
            #FIN salir

        def perfil_usuario():
            registro.destroy()

            #FIN perfil_usuario

        def inventario():
            registro.quit()
            #FIN inventario

        def ayuda():
            registro.quit()
            #FIN ayuda

        def cerrar_sesion():
            registro.destroy()

            #FIN cerrar_sesion

        perfil_usuario = Button(barra, text="Perfil del Usuario", command=salir)
        perfil_usuario.pack(side=LEFT, padx=2, pady=2)

        inventario = Button(barra, text="Inventario", command=salir)
        inventario.pack(side=LEFT, padx=2, pady=2)

        ayuda = Button(barra, text="Ayuda", command=salir)
        ayuda.pack(side=LEFT, padx=2, pady=2)

        Salir = Button(barra, text = "Salir", command = salir)
        Salir.pack(side = RIGHT, padx = 2, pady = 2)

        cerrar_sesion = Button(barra, text="Cerrar sesión", command=cerrar_sesion)
        cerrar_sesion.pack(side=RIGHT, padx=2, pady=2)

        barra.pack(side = TOP, fill = X)
    crear_barra()

    def crear_panel_registro():
        login = Frame(registro, bd = 1, relief = RAISED, background = Ayudas.azul_claro)
        login.place(in_=registro, anchor= "c", relx=0.5, rely=0.62)

        # -----Nombre de usuario-----
        usuariolabel = Label(login, text="Usuario:", background=Ayudas.azul_claro)
        usuariolabel.grid(row=0, column=0, sticky="w", padx=10, pady=10);
        usuario = Entry(login)
        usuario.grid(row=0, column=1, padx=10, pady=10)
        usuario.config(justify="center")

        # -----Correo-----
        correolabel = Label(login, text="Correo:", background= Ayudas.azul_claro)
        correolabel.grid(row=2, column=0, sticky= "w" ,padx=10, pady=10);
        correo = Entry(login)
        correo.grid(row=2, column=1, padx=10, pady=10)
        correo.config(justify="center")

        # -----Contraseña-----
        contrasenalabel = Label(login, text="Contraseña:", background= Ayudas.azul_claro)
        contrasenalabel.grid(row=4, column=0, sticky= "w" ,padx=10, pady=10);
        contrasena = Entry(login)
        contrasena.grid(row=4, column=1, padx=10, pady=10)
        contrasena.config(show= "*", justify="center")

        boton_registrarse= Button(login, text= "Registrar")
        boton_registrarse.grid(row=5, column=0, sticky= "w", padx=10, pady=10)
        #FIN crear_panel_login
    crear_panel_registro()
    
    registro.mainloop()
    # FIN crear_registro