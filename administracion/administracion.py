import alumno as Alu
import tkinter as tk
from tkinter.ttk import *
import tkinter.messagebox as mb
from tkinter import Toplevel  
import tkinter.font as tkFont

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
            limpiar_datos()
            mostrar_consulta()
        else:
            mb.showerror('Error', 'No se ha podido guardar el alumno ingresado.')
    
def limpiar_datos():
    txtNombre.set("")
    txtApellido.set("")
    txtApellido2.set("")
    txtTurno.set("")
    txtCurso.set("")

# Función para buscar al alumno por nombre
def buscar_alumno_nombre():
    nombre_buscar = txtbuscarNombre.get()
    if nombre_buscar != "":
        alumno = Alu.Alumno()
        data = alumno.buscar_por_nombre(nombre_buscar)
        if data:
            
            tree.delete(*tree.get_children())
            for row in data:
                tree.insert("", "end", values=row)
        else:
            mb.showinfo("Búsqueda", "No se encontraron alumnos con ese nombre.")
    else:
        mb.showinfo("Búsqueda", "Ingrese un nombre para buscar.")


def buscar_alumno_apellido():
    apellido_buscar = txtbuscarApellido.get()
    if apellido_buscar != "":
        alumno = Alu.Alumno()
        data = alumno.buscar_por_apellido(apellido_buscar)
        if data:
            tree.delete(*tree.get_children())
            for row in data:
                tree.insert("", "end", values=row)
            limpiar_datos()
            mostrar_consulta()
        else:
            mb.showinfo("Búsqueda", "No se encontraron alumnos con ese nombre.")
    else:
        mb.showinfo("Búsqueda", "Ingrese un nombre para buscar.")
    
# Función para mostrar la consulta en la misma ventana
def mostrar_consulta():
    alumno = Alu.Alumno()
    data = alumno.consultar_alumnos()

    if data:
        if hasattr(ven, "tree_frame"):
            ven.tree_frame.destroy()
        ven.tree_frame = Frame(ven)
        ven.tree_frame.place(x=10, y=300)

        global tree
        tree = Treeview(ven.tree_frame)
        tree["columns"] = ("id","nombre", "apellido1", "apellido2", "turno", "curso")
        tree.heading("id", text="Id")
        tree.heading("nombre", text="Nombre")
        tree.heading("apellido1", text="Apellido1")
        tree.heading("apellido2", text="Apellido2")
        tree.heading("turno", text="Turno")
        tree.heading("curso", text="Curso")

        for row in data:
            tree.insert("", "end", values=row)

        tree.pack()

        for col in tree["columns"]:
            tree.heading(col, text=col.title(), command=lambda _col=col: sort_column(tree, _col))
            max_width = max([tree.bbox(item, col)[2] for item in tree.get_children()])
            tree.column(col, width=max_width)
    else:
        mb.showinfo("Consulta", "No hay datos para mostrar.")

#def eliminar_registro():
#    if (txtNombre.get() == "" or txtApellido.get() == "" or txtApellido2.get() == "" or txtTurno.get() == "" or txtCurso.get() == ""):
#        mb.showerror('Verificar', 'El campo no puede estar vacío')
#    else:
        # Crear una instancia de la clase Alumno
#        alumno = Alu.Alumno()
#        res = alumno.eliminar_datos(
#            nombre=txtNombre.get(),
#            apellido1=txtApellido.get(),
#            apellido2=txtApellido2.get(),
#            turno=txtTurno.get(),
#            curso=txtCurso.get()
#        )
#        if res:
#            mb.showinfo('Correcto', 'Se guardó con éxito el alumno')
#            limpiar_datos()
#            mostrar_consulta()
#        else:
#            mb.showerror('Error', 'No se ha podido guardar el alumno ingresado.')

def sort_column(tree, col):
    items = [(tree.set(item, col), item) for item in tree.get_children("")]
    items.sort()
    for index, (val, item) in enumerate(items):
        tree.move(item, "", index)


# Crear la ventana principal
ven = tk.Tk()
ven.title("Planilla alumnos")
ven.config(width=1200, height=1200)

##Titulo
Label(ven, text="Informacion sobre el alumno").place(x=50, y=30)

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

# Centro de ayuda
Label(ven, text="Centro de ayuda").place(x=50, y=200)

# Busqueda
Label(ven, text="Busqueda nombre: ").place(x=50, y=250)
txtbuscarNombre = tk.StringVar()
Entry(ven, textvariable=txtbuscarNombre).place(x=180, y=250)
# Busqueda
Label(ven, text="Busqueda apellido: ").place(x=50, y=280)
txtbuscarApellido = tk.StringVar()
Entry(ven, textvariable=txtbuscarApellido).place(x=180, y=280)

# Botones
Button(ven, text="Enviar", command=guardar).place(x=600, y=70)
Button(ven, text="Limpiar", command=limpiar_datos).place(x=600, y=130)
Button(ven, text="Consulta", command=mostrar_consulta).place(x=600, y=100)
Button(ven, text="Buscar", command=buscar_alumno_nombre).place(x=340, y=250)
Button(ven, text="Buscar", command=buscar_alumno_apellido).place(x=340, y=280)
Button(ven, text="Eliminar").place(x=600, y=160)

# Iniciar la interfaz
ven.mainloop()
