from tkinter import *

class MenuClass:

    def Traer_AyudaVentana(ventana_funcion):
            global AyudaVentana_variable
            AyudaVentana_variable = ventana_funcion()

    def Traer_Inventario(ventana_funcion):
            global Inventario_variable 
            Inventario_variable = ventana_funcion()

    def MenuFunction(ventana):

        def Entrar_AyudaVentana ():
            ventana.quit()
            AyudaVentana_variable()
        
        def Entrar_Inventario():
            ventana.quit()
            Inventario_variable()

        menubar = Menu(ventana)
        menubar.add_command(label="Ayuda",command = Entrar_AyudaVentana)
        menubar.add_command(label="Inventario",command = Entrar_Inventario)
        ventana.config(menu=menubar)

