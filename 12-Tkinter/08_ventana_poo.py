import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class App(tk.Tk):
    def __init__(self):
        super().__init__()  # constructor de la clase padre Tk
        # Configurar la ventana
        self.configurar_ventana()
        # Configurar el grid
        self.configurar_grid()
        # Mostrar la tabla
        self.mostrar_tabla()

    def configurar_ventana(self):
        self.geometry('600x400')
        self.configure(background='#1d2d44')
        self.title('Manejo de ventanas con POO')

    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)

    def mostrar_tabla(self):
        # Definir un estilo
        estilos = ttk.Style()
        estilos.theme_use('clam')  # Prepara el manejo del tema oscuro
        estilos.configure('Treeview', background='black',
                          foreground='white',
                          fieldbackground='black',
                          rowheight=30)
        estilos.map('Treeview', background=[('selected', '#3a86ff')])

        # Definir las columnas
        columnas = ('Id', 'Nombre', 'Edad')
        self.tabla = ttk.Treeview(self, columns=columnas, show='headings')

        # Cabeceras de la tabla
        self.tabla.heading('Id', text='Id', anchor="center")
        self.tabla.heading('Nombre', text='Nombre', anchor="w")
        self.tabla.heading('Edad', text='Edad', anchor="w")

        # Formato de las columnas
        self.tabla.column('Id', width=80)
        self.tabla.column('Nombre', width=120)
        self.tabla.column('Edad', width=120)

        # Cargar datos a la tabla
        datos = ((1, 'Alejandra', 25), (2, 'Matías', 32))
        # datos = ((1, 'Alejandra', 25), (2, 'Matías', 32)) + ((1, 'Alejandra', 25), (2, 'Matías', 32)) + ((1, 'Alejandra', 25), (2, 'Matías', 32)) + ((1, 'Alejandra', 25), (2, 'Matías', 32)) + ((1, 'Alejandra', 25), (2, 'Matías', 32)) + ((1, 'Alejandra', 25), (2, 'Matías', 32)) + ((1, 'Alejandra', 25), (2, 'Matías', 32)) + ((1, 'Alejandra', 25), (2, 'Matías', 32)) + ((1, 'Alejandra', 25), (2, 'Matías', 32)) + ((1, 'Alejandra', 25), (2, 'Matías', 32)) + ((1, 'Alejandra', 25), (2, 'Matías', 32))# datos = ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32)) + ((1, 'Alejandra', 25), (2, 'Matias', 32))
        for persona in datos:
            self.tabla.insert(parent='', index="end", values=persona)

        # Agregamos un scrollbar
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        # Asociar el evento select de la tabla
        self.tabla.bind('<<TreeviewSelect>>', self.mostrar_registro_seleccionado)

        # Publicamos la tabla
        self.tabla.grid(row=0, column=0, sticky=tk.NSEW)

    # Mostrar registro seleccionado
    def mostrar_registro_seleccionado(self, event):
        print('Ejecutando metodo mostrar_registro_seleccionado')
        elemento_seleccionado = self.tabla.selection()[0]  # solo procesamos el primer registro
        elemento = self.tabla.item(elemento_seleccionado)  # item
        persona = elemento['values']  # tupla de persona
        print(persona)
        showinfo(title='Persona Seleccionada', message=f'Persona: {persona}')


if __name__ == '__main__':
    app = App()
    app.mainloop()
