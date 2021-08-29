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

    #-------------------Esto irá en el código main------------------------
    
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













        
"""#-----StringVar-----
        Hora = StringVar()
        Minutos = StringVar()
        Segundos = StringVar()

        #-----Entry-----
        global EntryHora
        EntryHora = Entry(FormularioVentana,width=3,font=Ayudas.boton_pequeno, textvariable=Hora )
        EntryHora.place(relx=0.2,rely= 0.5)

        global EntryMinutos
        EntryMinutos = Entry(FormularioVentana,width=3,font=Ayudas.boton_pequeno, textvariable=Minutos )
        EntryMinutos.place(relx=0.4,rely= 0.5)

        global EntrySegundos
        EntrySegundos = Entry(FormularioVentana,width=3,font=Ayudas.boton_pequeno, textvariable=Segundos)
        EntrySegundos.place(relx=0.6,rely= 0.5)"""

"""while True:

    current_time = time.strftime("%H:%M:%S")

    if current_time=="16:29:00":
        print(current_time)
        break
    else:
        pass


hr=ToastNotifier()

hr.show_toast("Alarm","This is the measage")"""
