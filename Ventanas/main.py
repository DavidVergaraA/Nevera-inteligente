from tkinter import *

#---Crear y configurar ventana---
ventana_principal= Tk()
ventana_principal.title=("Ventana principal")
ventana_principal.iconbitmap("Imagenes/logo.ico")

#---Colocar tamaño de la ventana---
ancho_ventana=ventana_principal.winfo_screenwidth()
alto_ventana=ventana_principal.winfo_screenheight()
ventana_principal.geometry("{}x{}+0+0".format(ancho_ventana,alto_ventana))

#---Frame cuerpo---
framecuerpo=Frame()
framecuerpo.config(bg="red",highlightbackground="black",highlightthickness=4)
framecuerpo.place(relheight=1,relwidth=1,rely=0,anchor=E)

#---Frame menú---
#frameMenu=Frame(ventana_principal)
#frameMenu.config(bg="green",highlightbackground="black",highlightthickness=4)
#frameMenu.place(relheight=1,relwidth=0.2,rely=0,anchor=W)



ventana_principal.mainloop()