from tkinter import *
from tkinter import messagebox
from io import open
from time import strftime
from win10toast import ToastNotifier
import time
import Ayudas

class FormularioNotificaciones:

    def formulario(ventana):

        #-----Formulario Ventana-----
        global FormularioVentana
        FormularioVentana = Toplevel(ventana)
        FormularioVentana.title("Formulario notificaciones")
        posx = int(FormularioVentana.winfo_screenwidth() / 2 - (600 / 2))
        posy = int(FormularioVentana.winfo_screenheight() / 2 - (300 / 2))
        FormularioVentana.geometry("{}x{}+{}+{}".format(600,300,posx,posy))
        FormularioVentana.resizable(0,0)
        FormularioVentana.iconbitmap(Ayudas.icono)
        FormularioVentana.config(bg = Ayudas.azul_claro)

        #-----Titulo-----
        TituloFormulario = Label(FormularioVentana,font = Ayudas.titulo, bg = Ayudas.azul_claro, text = "Notificaciones")
        TituloFormulario.place(relx = 0.33, rely=0.06)

        SubtituloFormualrio = Label(FormularioVentana,font = Ayudas.boton, bg = Ayudas.azul_claro, text = "Ingrese las cantidades mínimas que deben haber \n en  el inventario para ser notificado")
        SubtituloFormualrio.place(relx=0.12, rely=0.23)

        #-----Labels-----
        LabelArepas = Label(FormularioVentana,bg=Ayudas.azul_claro,font= Ayudas.normal,text="Arepas")
        LabelArepas.place(relx=0.14,rely=0.48)

        LabelHuevos = Label(FormularioVentana,bg=Ayudas.azul_claro,font= Ayudas.normal,text="Huevos")
        LabelHuevos.place(relx=0.14,rely=0.68)

        LabelLeche = Label(FormularioVentana,bg=Ayudas.azul_claro,font= Ayudas.normal,text="Leche")
        LabelLeche.place(relx=0.39, rely=0.48)

        LabelCarne = Label(FormularioVentana,bg=Ayudas.azul_claro,font= Ayudas.normal,text="Carne")
        LabelCarne.place(relx=0.39, rely=0.68)

        LabelTomates = Label(FormularioVentana,bg=Ayudas.azul_claro,font= Ayudas.normal,text="Tomates")
        LabelTomates.place(relx=0.63,rely=0.48)
        
        LabelSalchichas = Label(FormularioVentana,bg=Ayudas.azul_claro,font= Ayudas.normal,text="Salchichas")
        LabelSalchichas.place(relx=0.63,rely=0.68)

        #-----Stringvar-----
        ArepasNoti=StringVar()
        LecheNoti=StringVar()
        CarneNoti=StringVar()
        HuevosNoti=StringVar()
        TomateNoti=StringVar()
        SalchichasNoti=StringVar()

        #-----Entry-----
        EntryArepas = Entry(FormularioVentana,textvariable=ArepasNoti,width=8)
        EntryArepas.place(relx=0.24,rely=0.48)
        
        EntryHuevos = Entry(FormularioVentana,textvariable=HuevosNoti,width=8)
        EntryHuevos.place(relx=0.24,rely=0.68)

        EntryLeche = Entry(FormularioVentana,textvariable=LecheNoti,width=8)
        EntryLeche.place(relx=0.49,rely=0.48)

        EntryCarne = Entry(FormularioVentana,textvariable=CarneNoti,width=8)
        EntryCarne.place(relx=0.49,rely=0.68)

        EntryTomate = Entry(FormularioVentana,textvariable=TomateNoti,width=8)
        EntryTomate.place(relx=0.76,rely=0.48)

        EntrySalchichas = Entry(FormularioVentana,textvariable=SalchichasNoti,width=8)
        EntrySalchichas.place(relx=0.76,rely=0.68)

        #-----Funcionalidad botones
        def SalirFormulario():
            FormularioVentana.destroy()

        def ValidarDatos():

            try:
                int(ArepasNoti.get())
                int(HuevosNoti.get())
                int(LecheNoti.get())
                int(CarneNoti.get())
                int(TomateNoti.get())
                int(SalchichasNoti.get())
        
            except ValueError:

                FormularioVentana.destroy()
                messagebox.showerror("Error","El valor ingresado no es un número entero")
                return False

        def TomarValores():

            ValidarDatos() 
        
            NotificacionArepas = ArepasNoti.get()
            NotificacionHuevos = HuevosNoti.get()
            NotificacionLeche = LecheNoti.get()
            NotificacionCarne = CarneNoti.get()
            NotificacionTomate = TomateNoti.get()
            NotificacionSalchichas = SalchichasNoti.get()

            Archivo_Notificaciones = open("Archivos planos\\Notificaciones.txt", "r+")
            LineasNotificaciones = Archivo_Notificaciones.readlines()

            LineasNotificaciones[3]=(NotificacionArepas + "\n")
            LineasNotificaciones[6]=(NotificacionLeche + "\n")
            LineasNotificaciones[9]=(NotificacionCarne + "\n")
            LineasNotificaciones[12]=(NotificacionHuevos + "\n")
            LineasNotificaciones[15]=(NotificacionTomate + "\n")
            LineasNotificaciones[18]=(NotificacionSalchichas + "\n")

            Archivo_Notificaciones.seek(0)
            Archivo_Notificaciones.writelines(LineasNotificaciones)
            Archivo_Notificaciones.close()

        #-----Botones-----
        BotonSalir = Button(FormularioVentana,text = "Salir",bg= Ayudas.naranja, font= Ayudas.boton_pequeno, width = 7, height= 1, command=SalirFormulario)
        BotonSalir.place(relx=0.37,rely=0.85)

        BotonOk = Button(FormularioVentana,text = "OK",bg= Ayudas.naranja, font= Ayudas.boton_pequeno, width = 7, height= 1, command= lambda:[TomarValores(),SalirFormulario()])
        BotonOk.place(relx=0.50,rely=0.85)






