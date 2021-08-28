from tkinter import *
from tkinter import messagebox
from io import *
import Ayudas

#-------------------------------------------------------------------------------------------------
 
class CantidadAlimento():

    def __init__(self, ventana):

        #-----Propiedades Ventana Emergente-----
        global PopUpCantidad
        PopUpCantidad = Toplevel(ventana)
        posx = int(PopUpCantidad.winfo_screenwidth() / 2 - (300 / 2))
        posy = int(PopUpCantidad.winfo_screenheight() / 2 - (150 / 2))
        PopUpCantidad.geometry("{}x{}+{}+{}".format(300,150,posx,posy))
        PopUpCantidad.resizable(0,0)
        PopUpCantidad.iconbitmap(Ayudas.icono)
        PopUpCantidad.config(bg = Ayudas.azul_claro)

        #-----Titulo de cada ventana emergente-----
        global LabelTituloCantidad
        LabelTituloCantidad = Label (PopUpCantidad, text = "", bg = Ayudas.azul_claro, fg = Ayudas.negro_letra, font = Ayudas.subtitulo)
        LabelTituloCantidad.place(relx = 0.17, rely = 0.09)

        #-----Label que muestra la cantidad del alimento-----
        global LabelCantidad
        LabelCantidad = Label (PopUpCantidad, text = "" , bg = Ayudas.blanco, fg = Ayudas.negro_letra, font = Ayudas.boton , width = 8 , height=2 )
        LabelCantidad.place(relx = 0.334, rely = 0.33)

        #-----Funcion para salir-----
        def SalirBotonCantidad():

            PopUpCantidad.destroy()

        #-----Boton para salir de la ventana emergente-----
        BotonSalirCantidad = Button (PopUpCantidad, text = "OK",bg= Ayudas.naranja, fg = Ayudas.negro_letra, font= Ayudas.boton_pequeno, width = 4, height= 1, command=SalirBotonCantidad)
        BotonSalirCantidad.place(relx = 0.423, rely = 0.70)
        
    #-----Inicio de las funciones (VE es ventana emergente)-----
    def VE_CantidadArepas():
        
        ArchivoInventario = open("Archivos planos\InventarioInfo.txt", "r")
        LineasInventario = ArchivoInventario.readlines()
        LabelTituloCantidad.config(text="Cantidad de arepas")
        LabelCantidad.config(text= LineasInventario[3])
        ArchivoInventario.close()

    def VE_CantidadLeche():

        ArchivoInventario = open("Archivos planos\InventarioInfo.txt", "r")
        LineasInventario = ArchivoInventario.readlines()
        LabelTituloCantidad.config(text="Bolsas de leche")
        LabelTituloCantidad.place(relx = 0.23)
        LabelCantidad.config(text = LineasInventario[6])
        ArchivoInventario.close()

    def VE_CantidadCarne():

        ArchivoInventario = open("Archivos planos\InventarioInfo.txt", "r")
        LineasInventario = ArchivoInventario.readlines()
        LabelTituloCantidad.config(text="Libras de carne")
        LabelTituloCantidad.place(relx = 0.23)
        LabelCantidad.config(text = LineasInventario[9])
        ArchivoInventario.close()

    def VE_CantidadHuevos():

        ArchivoInventario = open("Archivos planos\InventarioInfo.txt", "r")
        LineasInventario = ArchivoInventario.readlines()
        LabelTituloCantidad.config(text="Cantidad de huevos")
        LabelCantidad.config(text = LineasInventario[12])
        ArchivoInventario.close()

    def VE_CantidadTomate():

        ArchivoInventario = open("Archivos planos\InventarioInfo.txt", "r")
        LineasInventario = ArchivoInventario.readlines()
        LabelTituloCantidad.config(text="Cantidad de tomates")
        LabelTituloCantidad.place(relx = 0.16)
        LabelCantidad.config(text = LineasInventario[15])
        ArchivoInventario.close()

    def VE_CantidadSalchicha():

        ArchivoInventario = open("Archivos planos\InventarioInfo.txt", "r")
        LineasInventario = ArchivoInventario.readlines()
        LabelTituloCantidad.config(text="Cantidad de salchichas")
        LabelTituloCantidad.place(relx = 0.11)
        LabelCantidad.config(text = LineasInventario[18])
        ArchivoInventario.close()
        
#-------------------------------------------------------------------------------------------------    

class AgregarAlimento:

    def __init__(self, ventana):

        #-----Propiedades Ventana Emergente-----
        global PopUpAgregar
        PopUpAgregar = Toplevel(ventana)
        posx = int(PopUpAgregar.winfo_screenwidth() / 2 - (300 / 2))
        posy = int(PopUpAgregar.winfo_screenheight() / 2 - (150 / 2))
        PopUpAgregar.geometry("{}x{}+{}+{}".format(300,150,posx,posy))
        PopUpAgregar.resizable(0,0)
        PopUpAgregar.iconbitmap(Ayudas.icono)
        PopUpAgregar.config(bg = Ayudas.azul_claro)

        #-----Titulo de cada ventana emergente-----
        global LabelTituloAgregar
        LabelTituloAgregar = Label (PopUpAgregar, text = "", bg = Ayudas.azul_claro, fg = Ayudas.negro_letra, font = Ayudas.subtitulo)
        LabelTituloAgregar.place(relx = 0.223, rely = 0.16)

        #-----Entry que agrega cantidad del alimento-----
        global EntryAgregar
        EntryAgregar = Entry (PopUpAgregar, bg = Ayudas.blanco, fg = Ayudas.negro_letra, font = Ayudas.boton , width = 8 , justify=CENTER)
        EntryAgregar.place(relx = 0.334, rely = 0.43)



        #-----Boton para salir de la ventana emergente-----
        global BotonSalirAgregar
        BotonSalirAgregar = Button (PopUpAgregar, text = "OK",bg= Ayudas.naranja, fg = Ayudas.negro_letra, font= Ayudas.boton_pequeno, width = 4, height= 1)
        BotonSalirAgregar.place(relx = 0.423, rely = 0.70)

    #-----Funcion para salir-----
    def SalirBotonAgregar():

        PopUpAgregar.destroy()

    #-----Validar número-----
    def ValidarEntrada(Entrada):

        try:
            int(Entrada.get())
        
        except ValueError:

            messagebox.showerror("Error","El valor ingresado no es un número entero")

    #-----Inicio de las funciones (VE es ventana emergente)-----
    def VE_AgregarArepas():

        global EntryAgregarArepas
        EntryAgregarArepas = EntryAgregar 
        LabelTituloAgregar.config(text="Agregar arepas")
        BotonSalirAgregar.config(command= lambda: [AgregarAlimento.TomarValorArepas(),AgregarAlimento.SalirBotonAgregar()])

    def TomarValorArepas():

        AgregarAlimento.ValidarEntrada(EntryAgregarArepas)
        ValorTomado = EntryAgregarArepas.get()

        
        if int(ValorTomado)<0:

            PopUpAgregar.destroy()

            messagebox.showerror("Error","El valor ingresado es menor que 0")

        else:
            
            ArchivoInventario = open("Archivos planos\InventarioInfo.txt", "r+")
            LineasInventario = ArchivoInventario.readlines()
            ValorAnterior = LineasInventario[3]
            ValorFinal = str(int(ValorTomado)+int(ValorAnterior))
            LineasInventario[3] = (ValorFinal + "\n")
            ArchivoInventario.seek(0)
            ArchivoInventario.writelines(LineasInventario)
            ArchivoInventario.close()
        

    def VE_AgregarLeche():

        global EntryAgregarLeche
        EntryAgregarLeche = EntryAgregar 
        LabelTituloAgregar.config(text="Agregar bolsas de leche")
        BotonSalirAgregar.config(command= lambda: [AgregarAlimento.TomarValorLeche(),AgregarAlimento.SalirBotonAgregar()])

    def TomarValorLeche():

        AgregarAlimento.ValidarEntrada(EntryAgregarLeche)
        ValorTomado = EntryAgregarLeche.get()

        if int(ValorTomado)<0:

            PopUpAgregar.destroy()

            messagebox.showerror("Error","El valor ingresado es menor que 0")

        else:

            ArchivoInventario = open("Archivos planos\InventarioInfo.txt", "r+")
            LineasInventario = ArchivoInventario.readlines()
            ValorAnterior = LineasInventario[6]
            ValorFinal = str(int(ValorTomado)+int(ValorAnterior))
            LineasInventario[6] = (ValorFinal + "\n")
            ArchivoInventario.seek(0)
            ArchivoInventario.writelines(LineasInventario)
            ArchivoInventario.close()

    def VE_AgregarCarne():

        global EntryAgregarCarne
        EntryAgregarCarne = EntryAgregar 
        LabelTituloAgregar.config(text="Agregar libras de carne")
        BotonSalirAgregar.config(command= lambda: [AgregarAlimento.TomarValorCarne(),AgregarAlimento.SalirBotonAgregar()])

    def TomarValorCarne():

        AgregarAlimento.ValidarEntrada(EntryAgregarCarne)
        ValorTomado = EntryAgregarCarne.get()

        if int(ValorTomado)<0:

            PopUpAgregar.destroy()

            messagebox.showerror("Error","El valor ingresado es menor que 0")

        else:

            ArchivoInventario = open("Archivos planos\InventarioInfo.txt", "r+")
            LineasInventario = ArchivoInventario.readlines()
            ValorAnterior = LineasInventario[9]
            ValorFinal = str(int(ValorTomado)+int(ValorAnterior))
            LineasInventario[9] = (ValorFinal + "\n")
            ArchivoInventario.seek(0)
            ArchivoInventario.writelines(LineasInventario)
            ArchivoInventario.close()

    def VE_AgregarHuevos():

        global EntryAgregarHuevos
        EntryAgregarHuevos = EntryAgregar 
        LabelTituloAgregar.config(text="Agregar huevos")
        BotonSalirAgregar.config(command= lambda: [AgregarAlimento.TomarValorHuevos(),AgregarAlimento.SalirBotonAgregar()])

    def TomarValorHuevos():

        AgregarAlimento.ValidarEntrada(EntryAgregarHuevos)
        ValorTomado = EntryAgregarHuevos.get()

        if int(ValorTomado)<0:

            PopUpAgregar.destroy()

            messagebox.showerror("Error","El valor ingresado es menor que 0")

        else:

            ArchivoInventario = open("Archivos planos\InventarioInfo.txt", "r+")
            LineasInventario = ArchivoInventario.readlines()
            ValorAnterior = LineasInventario[12]
            ValorFinal = str(int(ValorTomado)+int(ValorAnterior))
            LineasInventario[12] = (ValorFinal + "\n")
            ArchivoInventario.seek(0)
            ArchivoInventario.writelines(LineasInventario)
            ArchivoInventario.close()

    def VE_AgregarTomate():

        global EntryAgregarTomate
        EntryAgregarTomate = EntryAgregar 
        LabelTituloAgregar.config(text="Agregar tomates")
        BotonSalirAgregar.config(command= lambda: [AgregarAlimento.TomarValorTomate(),AgregarAlimento.SalirBotonAgregar()])

    def TomarValorTomate():

        AgregarAlimento.ValidarEntrada(EntryAgregarTomate)
        ValorTomado = EntryAgregarTomate.get()

        if int(ValorTomado)<0:

            PopUpAgregar.destroy()

            messagebox.showerror("Error","El valor ingresado es menor que 0")

        else:

            ArchivoInventario = open("Archivos planos\InventarioInfo.txt", "r+")
            LineasInventario = ArchivoInventario.readlines()
            ValorAnterior = LineasInventario[15]
            ValorFinal = str(int(ValorTomado)+int(ValorAnterior))
            LineasInventario[15] = (ValorFinal + "\n")
            ArchivoInventario.seek(0)
            ArchivoInventario.writelines(LineasInventario)
            ArchivoInventario.close()

    def VE_AgregarSalchichas():

        global EntryAgregarSalchichas
        EntryAgregarSalchichas = EntryAgregar 
        LabelTituloAgregar.config(text="Agregar salchichas")
        BotonSalirAgregar.config(command= lambda: [AgregarAlimento.TomarValorSalchichas(),AgregarAlimento.SalirBotonAgregar()])

    def TomarValorSalchichas():

        AgregarAlimento.ValidarEntrada(EntryAgregarSalchichas)
        ValorTomado = EntryAgregarSalchichas.get()

        if int(ValorTomado)<0:

            PopUpAgregar.destroy()

            messagebox.showerror("Error","El valor ingresado es menor que 0")

        else:

            ArchivoInventario = open("Archivos planos\InventarioInfo.txt", "r+")
            LineasInventario = ArchivoInventario.readlines()
            ValorAnterior = LineasInventario[18]
            ValorFinal = str(int(ValorTomado)+int(ValorAnterior))
            LineasInventario[18] = (ValorFinal + "\n")
            ArchivoInventario.seek(0)
            ArchivoInventario.writelines(LineasInventario)
            ArchivoInventario.close()

#-------------------------------------------------------------------------------------------------

class EliminarAlimento:

    def __init__(self, ventana):

        #-----Propiedades Ventana Emergente-----
        global PopUpEliminar
        PopUpEliminar = Toplevel(ventana)
        posx = int(PopUpEliminar.winfo_screenwidth() / 2 - (300 / 2))
        posy = int(PopUpEliminar.winfo_screenheight() / 2 - (150 / 2))
        PopUpEliminar.geometry("{}x{}+{}+{}".format(300,150,posx,posy))
        PopUpEliminar.resizable(0,0)
        PopUpEliminar.iconbitmap(Ayudas.icono)
        PopUpEliminar.config(bg = Ayudas.azul_claro)

        #-----Titulo de cada ventana emergente-----
        global LabelTituloEliminar
        LabelTituloEliminar = Label (PopUpEliminar, text = "", bg = Ayudas.azul_claro, fg = Ayudas.negro_letra, font = Ayudas.subtitulo)
        LabelTituloEliminar.place(relx = 0.223, rely = 0.16)

        #-----Entry que agrega cantidad del alimento-----
        global EntryEliminar
        EntryEliminar = Entry (PopUpEliminar, bg = Ayudas.blanco, fg = Ayudas.negro_letra, font = Ayudas.boton , width = 8 , justify=CENTER)
        EntryEliminar.place(relx = 0.334, rely = 0.43)

        #-----Boton para salir de la ventana emergente-----
        global BotonSalirEliminar
        BotonSalirEliminar = Button (PopUpEliminar, text = "OK",bg= Ayudas.naranja, fg = Ayudas.negro_letra, font= Ayudas.boton_pequeno, width = 4, height= 1)
        BotonSalirEliminar.place(relx = 0.423, rely = 0.70)

    #-----Funcion para salir-----
    def SalirBotonEliminar():

        PopUpEliminar.destroy()

    #-----Validar número-----
    def ValidarEntrada(Entrada):

        try:
            int(Entrada.get())
        
        except ValueError:

            messagebox.showerror("Error","Ingrese un número entero")


    #-----Inicio de las funciones (VE es ventana emergente)-----
    def VE_EliminarArepas():

        global EntryEliminarArepas
        EntryEliminarArepas = EntryEliminar
        LabelTituloEliminar.config(text="Eliminar arepas")
        BotonSalirEliminar.config(command= lambda: [EliminarAlimento.TomarValorArepas(),EliminarAlimento.SalirBotonEliminar()])

    def TomarValorArepas():

        EliminarAlimento.ValidarEntrada(EntryEliminarArepas)
        ValorTomado = EntryEliminarArepas.get()

        ArchivoInventario = open("Archivos planos\InventarioInfo.txt", "r+")
        LineasInventario = ArchivoInventario.readlines()
        ValorAnterior = LineasInventario[3]

        if int(ValorTomado)<0:

            PopUpEliminar.destroy()

            messagebox.showerror("Error","El valor ingresado es menor que 0")

        if int(ValorAnterior) < int(ValorTomado):
            
            PopUpEliminar.destroy()

            messagebox.showerror("Error","El valor ingresado es mayor al que se tiene en inventario")

        else:

            ValorFinal = str(int(ValorAnterior)-int(ValorTomado))
            LineasInventario[3] = (ValorFinal + "\n")
            ArchivoInventario.seek(0)
            ArchivoInventario.writelines(LineasInventario)

        ArchivoInventario.close()

    def VE_EliminarLeche():

        global EntryEliminarLeche
        EntryEliminarLeche = EntryEliminar
        LabelTituloEliminar.config(text="Eliminar bolsas de leche")
        BotonSalirEliminar.config(command= lambda: [EliminarAlimento.TomarValorLeche(),EliminarAlimento.SalirBotonEliminar()])

    def TomarValorLeche():

        EliminarAlimento.ValidarEntrada(EntryEliminarLeche)
        ValorTomado = EntryEliminarLeche.get()

        ArchivoInventario = open("Archivos planos\InventarioInfo.txt", "r+")
        LineasInventario = ArchivoInventario.readlines()
        ValorAnterior = LineasInventario[6]

        if int(ValorTomado)<0:

            PopUpEliminar.destroy()

            messagebox.showerror("Error","El valor ingresado es menor que 0")

        if int(ValorAnterior) < int(ValorTomado):
            
            PopUpEliminar.destroy()

            messagebox.showerror("Error","El valor ingresado es mayor al que se tiene en inventario")

        else:

            ValorFinal = str(int(ValorAnterior)-int(ValorTomado))
            LineasInventario[6] = (ValorFinal + "\n")
            ArchivoInventario.seek(0)
            ArchivoInventario.writelines(LineasInventario)

        ArchivoInventario.close()
     
    def VE_EliminarCarne():

        global EntryEliminarCarne
        EntryEliminarCarne = EntryEliminar
        LabelTituloEliminar.config(text="Eliminar libras de carne")
        BotonSalirEliminar.config(command= lambda: [EliminarAlimento.TomarValorCarne(),EliminarAlimento.SalirBotonEliminar()])

    def TomarValorCarne():

        EliminarAlimento.ValidarEntrada(EntryEliminarCarne)
        ValorTomado = EntryEliminarCarne.get()

        ArchivoInventario = open("Archivos planos\InventarioInfo.txt", "r+")
        LineasInventario = ArchivoInventario.readlines()
        ValorAnterior = LineasInventario[9]

        if int(ValorTomado)<0:

            PopUpEliminar.destroy()

            messagebox.showerror("Error","El valor ingresado es menor que 0")

        if int(ValorAnterior) < int(ValorTomado):
            
            PopUpEliminar.destroy()

            messagebox.showerror("Error","El valor ingresado es mayor al que se tiene en inventario")

        else:

            ValorFinal = str(int(ValorAnterior)-int(ValorTomado))
            LineasInventario[9] = (ValorFinal + "\n")
            ArchivoInventario.seek(0)
            ArchivoInventario.writelines(LineasInventario)

        ArchivoInventario.close()

    def VE_EliminarHuevos():

        global EntryEliminarHuevos
        EntryEliminarHuevos = EntryEliminar
        LabelTituloEliminar.config(text="Eliminar huevos")
        BotonSalirEliminar.config(command= lambda: [EliminarAlimento.TomarValorHuevos(),EliminarAlimento.SalirBotonEliminar()])

    def TomarValorHuevos():

        EliminarAlimento.ValidarEntrada(EntryEliminarHuevos)
        ValorTomado = EntryEliminarHuevos.get()

        ArchivoInventario = open("Archivos planos\InventarioInfo.txt", "r+")
        LineasInventario = ArchivoInventario.readlines()
        ValorAnterior = LineasInventario[12]

        if int(ValorTomado)<0:

            PopUpEliminar.destroy()

            messagebox.showerror("Error","El valor ingresado es menor que 0")

        if int(ValorAnterior) < int(ValorTomado):
            
            PopUpEliminar.destroy()

            messagebox.showerror("Error","El valor ingresado es mayor al que se tiene en inventario")

        else:

            ValorFinal = str(int(ValorAnterior)-int(ValorTomado))
            LineasInventario[12] = (ValorFinal + "\n")
            ArchivoInventario.seek(0)
            ArchivoInventario.writelines(LineasInventario)

        ArchivoInventario.close()

    def VE_EliminarTomates():

        global EntryEliminarTomates
        EntryEliminarTomates = EntryEliminar
        LabelTituloEliminar.config(text="Eliminar tomates")
        BotonSalirEliminar.config(command= lambda: [EliminarAlimento.TomarValorTomates(),EliminarAlimento.SalirBotonEliminar()])

    def TomarValorTomates():

        EliminarAlimento.ValidarEntrada(EntryEliminarTomates)
        ValorTomado = EntryEliminarTomates.get()

        ArchivoInventario = open("Archivos planos\InventarioInfo.txt", "r+")
        LineasInventario = ArchivoInventario.readlines()
        ValorAnterior = LineasInventario[15]

        if int(ValorTomado)<0:

            PopUpEliminar.destroy()

            messagebox.showerror("Error","El valor ingresado es menor que 0")

        if int(ValorAnterior) < int(ValorTomado):
            
            PopUpEliminar.destroy()

            messagebox.showerror("Error","El valor ingresado es mayor al que se tiene en inventario")

        else:

            ValorFinal = str(int(ValorAnterior)-int(ValorTomado))
            LineasInventario[15] = (ValorFinal + "\n")
            ArchivoInventario.seek(0)
            ArchivoInventario.writelines(LineasInventario)

        ArchivoInventario.close()

    def VE_EliminarSalchichas():

        global EntryEliminarSalchichas
        EntryEliminarSalchichas = EntryEliminar
        LabelTituloEliminar.config(text="Eliminar salchichas")
        BotonSalirEliminar.config(command= lambda: [EliminarAlimento.TomarValorSalchichas(),EliminarAlimento.SalirBotonEliminar()])

    def TomarValorSalchichas():

        EliminarAlimento.ValidarEntrada(EntryEliminarSalchichas)
        ValorTomado = EntryEliminarSalchichas.get()

        ArchivoInventario = open("Archivos planos\InventarioInfo.txt", "r+")
        LineasInventario = ArchivoInventario.readlines()
        ValorAnterior = LineasInventario[18]

        if int(ValorTomado)<0:

            PopUpEliminar.destroy()

            messagebox.showerror("Error","El valor ingresado es menor que 0")

        if int(ValorAnterior) < int(ValorTomado):
            
            PopUpEliminar.destroy()

            messagebox.showerror("Error","El valor ingresado es mayor al que se tiene en inventario")

        else:

            ValorFinal = str(int(ValorAnterior)-int(ValorTomado))
            LineasInventario[18] = (ValorFinal + "\n")
            ArchivoInventario.seek(0)
            ArchivoInventario.writelines(LineasInventario)

        ArchivoInventario.close()