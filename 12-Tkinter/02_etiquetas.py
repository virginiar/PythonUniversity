import tkinter as tk
from tkinter import ttk

# Creamos una ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Nueva Ventana')
ventana.configure(background='#1d2d44')

# Creamos una etiqueta (label)
etiqueta = ttk.Label(ventana, text='Saludos')

# Cambiar el texto usando configure
etiqueta.configure(text='Nos vemos...')

# Cambiar el texto con ayuda de la llave text
etiqueta['text'] = 'Adiós'

# Publicamos el componente
etiqueta.pack(pady=20)

ventana.mainloop()
