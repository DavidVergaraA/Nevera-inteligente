from tkinter import *
from PIL import ImageTk, Image
import Ayudas
#from MenuBar import MenuClass


# -----Ventana de inventario-----
inventario = Tk()

inventario.iconbitmap(Ayudas.icono)

inventario.title("Inventario")
inventario.configure(background=Ayudas.azul_hielo)

posx = int(inventario.winfo_screenwidth() / 2 - (Ayudas.ancho2 / 2))
posy = int(inventario.winfo_screenheight() / 2 - (Ayudas.alto2 / 2))
inventario.geometry(
    "{}x{}+{}+{}".format(Ayudas.ancho2, Ayudas.alto2, posx, posy))
inventario.resizable(0, 0)

# -----Titulo-----
titulo = Label(inventario, text="Inventario", font=Ayudas.titulo,
               bg=Ayudas.azul_hielo, fg=Ayudas.negro_letra)
titulo.place(relx=0.45, rely=0.1)

# -----Logo-----
ImgCaja = ImageTk.PhotoImage(Image.open("Imagenes/caja.png"))
LogoCaja = Label(image=ImgCaja, height=70, width=70, bg=Ayudas.azul_hielo)
LogoCaja.place(relx=0.37, rely=0.07)

# -----Imagenes inventario-----
img1 = ImageTk.PhotoImage(Image.open("Imagenes/arepa.jpg"))
Imagen1 = Label(image=img1, height=155, width=213)
Imagen1.place(relx=0.1, rely=0.3)

img2 = ImageTk.PhotoImage(Image.open("Imagenes/leche.jpg"))
Imagen2 = Label(image=img2, height=155, width=213)
Imagen2.place(relx=0.4, rely=0.3)

img3 = ImageTk.PhotoImage(Image.open("Imagenes/carne.jpg"))
Imagen3 = Label(image=img3, height=155, width=213)
Imagen3.place(relx=0.7, rely=0.3)

img4 = ImageTk.PhotoImage(Image.open("Imagenes/huevo.jpg"))
Imagen4 = Label(image=img4, height=155, width=213)
Imagen4.place(relx=0.1, rely=0.65)

img5 = ImageTk.PhotoImage(Image.open("Imagenes/quesito.jpg"))
Imagen5 = Label(image=img5, height=155, width=213)
Imagen5.place(relx=0.4, rely=0.65)

img6 = ImageTk.PhotoImage(Image.open("Imagenes/salchichas.jpg"))
Imagen6 = Label(image=img6, height=155, width=213)
Imagen6.place(relx=0.7, rely=0.65)

# -----Botones-----
Boton1_Im1 = Button(
    bg=Ayudas.blanco, font=Ayudas.boton_pequeno, height=1, width=7, text="Cantidad")
Boton1_Im1.place(relx=0.099, rely=0.533)
Boton2_Im1 = Button(
    bg=Ayudas.blanco, font=Ayudas.boton_pequeno, height=1, width=7, text="Agregar")
Boton2_Im1.place(relx=0.171, rely=0.533)
Boton3_Im1 = Button(
    bg=Ayudas.blanco, font=Ayudas.boton_pequeno, height=1, width=7, text="Eliminar")
Boton3_Im1.place(relx=0.242, rely=0.533)

Boton1_Im2 = Button(
    bg=Ayudas.blanco, font=Ayudas.boton_pequeno, height=1, width=7, text="Cantidad")
Boton1_Im2.place(relx=0.399, rely=0.533)
Boton2_Im2 = Button(
    bg=Ayudas.blanco, font=Ayudas.boton_pequeno, height=1, width=7, text="Agregar")
Boton2_Im2.place(relx=0.471, rely=0.533)
Boton3_Im2 = Button(
    bg=Ayudas.blanco, font=Ayudas.boton_pequeno, height=1, width=7, text="Eliminar")
Boton3_Im2.place(relx=0.542, rely=0.533)

Boton1_Im3 = Button(
    bg=Ayudas.blanco, font=Ayudas.boton_pequeno, height=1, width=7, text="Cantidad")
Boton1_Im3.place(relx=0.699, rely=0.533)
Boton2_Im3 = Button(
    bg=Ayudas.blanco, font=Ayudas.boton_pequeno, height=1, width=7, text="Agregar")
Boton2_Im3.place(relx=0.771, rely=0.533)
Boton3_Im3 = Button(
    bg=Ayudas.blanco, font=Ayudas.boton_pequeno, height=1, width=7, text="Eliminar")
Boton3_Im3.place(relx=0.842, rely=0.533)

Boton1_Im4 = Button(
    bg=Ayudas.blanco, font=Ayudas.boton_pequeno, height=1, width=7, text="Cantidad")
Boton1_Im4.place(relx=0.099, rely=0.883)
Boton2_Im4 = Button(
    bg=Ayudas.blanco, font=Ayudas.boton_pequeno, height=1, width=7, text="Agregar")
Boton2_Im4.place(relx=0.171, rely=0.883)
Boton3_Im4 = Button(
    bg=Ayudas.blanco, font=Ayudas.boton_pequeno, height=1, width=7, text="Eliminar")
Boton3_Im4.place(relx=0.242, rely=0.883)

Boton1_Im5 = Button(
    bg=Ayudas.blanco, font=Ayudas.boton_pequeno, height=1, width=7, text="Cantidad")
Boton1_Im5.place(relx=0.399, rely=0.883)
Boton2_Im5 = Button(
    bg=Ayudas.blanco, font=Ayudas.boton_pequeno, height=1, width=7, text="Agregar")
Boton2_Im5.place(relx=0.471, rely=0.883)
Boton3_Im5 = Button(
    bg=Ayudas.blanco, font=Ayudas.boton_pequeno, height=1, width=7, text="Eliminar")
Boton3_Im5.place(relx=0.542, rely=0.883)

Boton1_Im6 = Button(
    bg=Ayudas.blanco, font=Ayudas.boton_pequeno, height=1, width=7, text="Cantidad")
Boton1_Im6.place(relx=0.699, rely=0.883)
Boton2_Im6 = Button(
    bg=Ayudas.blanco, font=Ayudas.boton_pequeno, height=1, width=7, text="Agregar")
Boton2_Im6.place(relx=0.771, rely=0.883)
Boton3_Im6 = Button(
    bg=Ayudas.blanco, font=Ayudas.boton_pequeno, height=1, width=7, text="Eliminar")
Boton3_Im6.place(relx=0.842, rely=0.883)

"""MenuClass.MenuFunction(inventario)
    MenuClass.Traer_Inventario(inventario_funcion)"""

inventario.mainloop()
