import qrcode
from PIL import Image
import tkinter as tk



ventana = tk.Tk()
ventana.title('QR Converter')
ventana.geometry('500x500+500+50')
ventana.resizable(width=False, height=False)

link = tk.StringVar()
nombre = tk.StringVar()

entrada = tk.Entry(ventana,justify=tk.CENTER, textvar=link, width=50, relief='flat', bg='#CFCFCF')
entrada.place(x=90, y=244)
entrada.insert(0, 'Ingrese el link')

entrada2 = tk.Entry(ventana,justify=tk.CENTER, textvar=nombre, width=50, relief='flat', bg='#CFCFCF')
entrada2.place(x=90, y=300)
entrada2.insert(0, 'Ingrese el nombre del archivo')




def salir():
    ventana.destroy()


def convertir():
    enlace = link.get()
    imagen = qrcode.make(enlace)
    nombre_archivo = nombre.get()+'qrcode' + '.png'
    archivo_imagen = open(nombre_archivo, 'wb')
    imagen.save(archivo_imagen)
    archivo_imagen.close()
    ruta_archivo = './'+nombre_archivo
    Image.open(ruta_archivo).show()

# Botones

boton1 = tk.Button(ventana,foreground='#ffffff', text='Convertir',command=convertir, cursor="hand2", bg="#338F39", width=12, relief='flat', font=('Roboto',12 ))
boton1.place(x=300, y=400) 

boton2 = tk.Button(ventana,foreground='#ffffff', text='Salir',command=salir, cursor="hand2", bg="#FF0000", width=12, relief='flat', font=('Roboto',12 ))
boton2.place(x=60, y=400) 



ventana.mainloop()


# def crearQr():
