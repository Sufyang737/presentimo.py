import alumno as Alu
import tkinter as tk
from tkinter.ttk import *
import tkinter.messagebox as mb
from tkinter import Toplevel  

# Función para guardar los campos
def guardar():
    if (txtNombre.get() == "" or txtApellido.get() == "" or txtApellido2.get() == "" or txtTurno.get() == "" or txtCurso.get() == ""):
        mb.showerror('Verificar', 'El campo no puede estar vacío')
    else:
        # Crear una instancia de la clase Alumno
        alumno = Alu.Alumno()
        res = alumno.save(
            nombre=txtNombre.get(),
            apellido1=txtApellido.get(),
            apellido2=txtApellido2.get(),
            turno=txtTurno.get(),
            curso=txtCurso.get()
        )
        if res:
            mb.showinfo('Correcto', 'Se guardó con éxito el alumno')
        else:
            mb.showerror('Error', 'No se ha podido guardar el alumno ingresado.')

# Función para limpiar campos
def limpiar_campos():
    txtNombre.set("")
    txtApellido.set("")
    txtApellido2.set("")
    txtTurno.set("")
    txtCurso.set("")

# Función para mostrar la consulta en la misma ventana
def mostrar_consulta():
    alumno = Alu.Alumno()
    data = alumno.consultar_alumnos()

    if data:
        if hasattr(ven, "tree_frame"):
            ven.tree_frame.destroy()
        ven.tree_frame = Frame(ven)
        ven.tree_frame.place(x=10, y=300)

        tree = Treeview(ven.tree_frame)
        tree["columns"] = ("nombre", "apellido1", "apellido2", "turno", "curso")
        tree.heading("nombre", text="Nombre")
        tree.heading("apellido1", text="Apellido1")
        tree.heading("apellido2", text="Apellido2")
        tree.heading("turno", text="Turno")
        tree.heading("curso", text="Curso")

        for row in data:
            tree.insert("", "end", values=row)

        tree.pack()

    else:
        mb.showinfo("Consulta", "No hay datos para mostrar.")
    

# Función para buscar al alumno por apellido
"""
def buscar():
    def mostrar_consulta(self,where=""):
    alumno = Alu.Alumno()
    data = alumno.consultar_alumnos()
    if len(where)>0:
        cur=self.queryalumno("SELECT 'nombre', 'clave' FROM álumnos' "+where)
    
"""
# Crear la ventana principal
ven = tk.Tk()
ven.title("Planilla alumnos")
ven.config(width=700, height=700)

##Titulo
Label(ven, text="Informacion sobre el alumno").place(x=50, y=30)

#botones

# Campos de registro
Label(ven, text="Nombre:").place(x=50, y=70)
txtNombre = tk.StringVar()
Entry(ven, textvariable=txtNombre).place(x=110, y=70)

Label(ven, text="Apellido1:").place(x=50, y=104)
txtApellido = tk.StringVar()
Entry(ven, textvariable=txtApellido).place(x=110, y=104)

Label(ven, text="Apellido2:").place(x=50, y=140)
txtApellido2 = tk.StringVar()
Entry(ven, textvariable=txtApellido2).place(x=110, y=140)

Label(ven, text="Turno:").place(x=310, y=70)
txtTurno = tk.StringVar()
Entry(ven, textvariable=txtTurno).place(x=360, y=70)

Label(ven, text="Curso:").place(x=310, y=100)
txtCurso = tk.StringVar()
Entry(ven, textvariable=txtCurso).place(x=360, y=100)

#centro de ayuda
Label(ven, text="Centro de ayuda").place(x=50, y=200)

#Busqueda
Label(ven, text="Busqueda:").place(x=50, y=250)
txtBusqueda = tk.StringVar()
Entry(ven, textvariable=txtBusqueda).place(x=120, y=250)

# Botones
Button(ven, text="Enviar", command=guardar).place(x=600, y=70)
Button(ven, text="Eliminar", command=limpiar_campos).place(x=600, y=130)
Button(ven, text="Consulta", command=mostrar_consulta).place(x=600, y=100)


# Iniciar la interfaz
ven.mainloop()
