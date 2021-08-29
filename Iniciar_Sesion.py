from tkinter import *
from Perfil_Usuario import *
from Ayuda_Ventana import *
from Inventario import *
from Registrar import *
from Olvido_Contrasena import *
import Ayudas
from io import *
from win10toast import ToastNotifier
from PIL import ImageTk, Image
import threading
import time
import tkinter.ttk
from tkinter.ttk import Entry
from tkinter.ttk import Button

principal = Tk()

def crear_principal():

    principal.iconbitmap(Ayudas.icono)

    principal.title("Ingreso de Usuario")

    principal.configure(bg = Ayudas.blanco)
    posx = int(principal.winfo_screenwidth() / 2 - (Ayudas.ancho / 2))
    posy = int(principal.winfo_screenheight() / 2 - (Ayudas.alto / 2))
    principal.geometry(
        "{}x{}+{}+{}".format(Ayudas.ancho, Ayudas.alto, posx, posy))
    principal.resizable(0, 0)

    # -----Imagenes-----
    global Imgfondo
    Imgfondo = ImageTk.PhotoImage(Image.open("Imagenes/fondo.png"))
    Logofondo = Label(image=Imgfondo, height=355, width=300, bg=Ayudas.azul_claro)
    Logofondo.place(in_=principal, anchor= "c", relx=0.5, rely=0.545)

    global Imglogoi
    Imglogoi = ImageTk.PhotoImage(Image.open("Imagenes/logo.png"))
    Logologoi = Label(image=Imglogoi, height=154, width=154, bd=0 )
    Logologoi.place(relx=0.4, rely=0.061)

    #-----Titulo-----
    titulo= Label(principal, text= "Iniciar Sesión", font= Ayudas.titulo, bg= Ayudas.azul_claro, fg= Ayudas.negro_letra)
    titulo.place(in_=principal, anchor="c", relx=0.5, rely=0.4)

    principal.overrideredirect(1)

    def crear_barra():
        barra = Frame(principal, bd=1, relief = RAISED)

        def salir():
            principal.quit()
            #FIN salir

        perfil_usuario = Button(barra, text="Perfil del Usuario", command=EntrarPerfil_Usuario)
        perfil_usuario.pack(side=LEFT, padx=2, pady=2)

        inventario = Button(barra, text="Inventario", command=EntrarInventario)
        inventario.pack(side=LEFT, padx=2, pady=2)

        ayuda = Button(barra, text="Ayuda", command=EntrarAyuda)
        ayuda.pack(side=LEFT, padx=2, pady=2)

        Salir = Button(barra, text = "Salir", command = salir)
        Salir.pack(side = RIGHT, padx = 2, pady = 2)

        cerrar_sesion = Button(barra, text="Cerrar sesión", command=salir)
        cerrar_sesion.pack(side=RIGHT, padx=2, pady=2)

        barra.pack(side = TOP, fill = X)
    crear_barra()

    def crear_panel_login():
        login = Frame(principal, bd = 1, relief = RAISED, background = Ayudas.azul_claro)
        login.place(in_=principal, anchor= "c", relx=0.5, rely=0.57)

        # -----Correo-----
        correolabel = Label(login, text="Correo:", background= Ayudas.azul_claro)
        correolabel.grid(row=0, column=0, sticky= "w" ,padx=10, pady=10);
        correo = Entry(login)
        correo.grid(row=0, column=1, padx=10, pady=10)
        correo.config(justify="center")

        # -----Contraseña-----
        contrasenalabel = Label(login, text="Contraseña:", background= Ayudas.azul_claro)
        contrasenalabel.grid(row=2, column=0, sticky= "w" ,padx=10, pady=10);
        contrasena = Entry(login)
        contrasena.grid(row=2, column=1, padx=10, pady=10)
        contrasena.config(show= "*", justify="center")

        #-----Boton ingresar-----
        boton_ingresar= Frame(login, background= Ayudas.azul_claro)
        ingresar= Button(boton_ingresar, text="Contraseña:", command= principal.destroy)
        boton_ingresar.grid(row=3, column=0, sticky= "w", padx=10, pady=10)

        #FIN crear_panel_login
    crear_panel_login()

    #-----Olvidar contraseña-----
    olvidar_contrasena= Button(principal, text= "¿Olvidaste tu contraseña?", command= principal.destroy)
    olvidar_contrasena.place(in_=principal, anchor="c", relx=0.5, rely=0.755)

    #-----Registrarse-----
    registrarse= Button(principal, text= "Crear nueva cuenta", command= principal.destroy)
    registrarse.place(in_=principal, anchor="c", relx=0.5, rely=0.835)

crear_principal()


#----- Llamado de las ventanas------
def EntrarRegistrar():

    registro = Toplevel(principal)
    Registrar_Ventana(registro)

def EntrarOlvido_Contrasena():

    recuperar_contrasena = Toplevel(principal)
    Olvido_Constrasena_Ventana(recuperar_contrasena)

def EntrarInventario():

    inventario = Toplevel(principal)
    InventarioVentana(inventario)

def EntrarPerfil_Usuario():

    perfil_Usuario = Toplevel(principal)
    PerfilUsuarioVentana(perfil_Usuario)

def EntrarAyuda():

    Ayuda_ventana = Toplevel(principal)
    Ayuda_Ventana(Ayuda_ventana)

#----- Crear Menú -----

"""def CrearMenu(ventana,ventana_actual):

    menuVentanas = Menu(ventana)

    menuVentanas.add_command(label="Inventario",command = lambda:[ventana_actual.quit(),EntrarInventario()])
    menuVentanas.add_command(label="Perfil Usuario",command = lambda:[ventana_actual.quit(),EntrarPerfil_Usuario()])
    menuVentanas.add_command(label="Ayuda",command = lambda:[ventana_actual.quit(),EntrarAyuda()])
    menuVentanas.add_command(label="Salir",command = principal.quit)
    
    ventana.config(menu=menuVentanas)"""


#----------Notificaciones---------------

def verificarNotificaciones(segundos):

    for i in range (10):
            
        Archivo_Notificaciones = open ("Archivos planos\\Notificaciones.txt", "r")
        LineasNotificaciones = Archivo_Notificaciones.readlines()

        Archivo_Inventario = open("Archivos planos\InventarioInfo.txt", "r")
        LineasInventario = Archivo_Inventario.readlines()

        if ( int(LineasNotificaciones[3]) >= (int(LineasInventario[3])) ):

            Notificacion = ToastNotifier()
            Notificacion.show_toast("Es hora de pedir más arepas!!!","Tienes solo " + LineasInventario[3] + " arepas en tu nevera",Ayudas.icono, duration=10)

        elif ( int(LineasNotificaciones[6]) >= (int(LineasInventario[6])) ):
            
            Notificacion = ToastNotifier()
            Notificacion.show_toast("Es hora de pedir más bolsas de leche!!!","Tienes solo " + LineasInventario[6] + " bolsas de leche en tu nevera",Ayudas.icono, duration=10)

        elif ( int(LineasNotificaciones[9]) >= (int(LineasInventario[9])) ):
            
            Notificacion = ToastNotifier()
            Notificacion.show_toast("Es hora de pedir más libras de carne!!!","Tienes solo " + LineasInventario[9] + " libras de carne en tu nevera",Ayudas.icono, duration=10)

        elif ( int(LineasNotificaciones[12]) >= (int(LineasInventario[12])) ):
            
            Notificacion = ToastNotifier()
            Notificacion.show_toast("Es hora de pedir más huevos!!!","Tienes solo " + LineasInventario[12] + " huevos en tu nevera",Ayudas.icono, duration=10)

        elif ( int(LineasNotificaciones[15]) >= (int(LineasInventario[15])) ):
            
            Notificacion = ToastNotifier()
            Notificacion.show_toast("Es hora de pedir más tomates!!!","Tienes solo " + LineasInventario[15] + " tomates en tu nevera",Ayudas.icono, duration=10)

        elif ( int(LineasNotificaciones[18]) >= (int(LineasInventario[18])) ):
            
            Notificacion = ToastNotifier()
            Notificacion.show_toast("Es hora de pedir más salchichas!!!","Tienes solo " + LineasInventario[18] + " salchichas en tu nevera",Ayudas.icono, duration=10)

        Archivo_Inventario.close()
        Archivo_Notificaciones.close()
        time.sleep(segundos)

hilo = threading.Thread(target=verificarNotificaciones, args=(60,))
hilo.start()

principal.mainloop()

