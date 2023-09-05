import alumno as Alu
from alumno import Alumno
import tkinter as tk
from tkinter.ttk import *
import tkinter.messagebox as mb
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

# Función para buscar al alumno por apellido
def buscar_alumno_apellido():
    apellido_buscar = txtbuscarApellido.get()
    if apellido_buscar != "":
        alumno = Alu.Alumno()
        data = alumno.buscar_por_apellido(apellido_buscar)
        if data:
            tree.delete(*tree.get_children())
            for row in data:
                tree.insert("", "end", values=row)
        else:
            mb.showinfo("Búsqueda", "No se encontraron alumnos con ese nombre.")
    else:
        mb.showinfo("Búsqueda", "Ingrese un apellido para buscar.")

# Función para buscar al alumno por curso
def buscar_alumno_curso():
    curso_buscar = txtbuscarCurso.get()
    if curso_buscar != "":
        alumno = Alu.Alumno()
        data = alumno.buscar_por_curso(curso_buscar)
        if data:
            tree.delete(*tree.get_children())
            for row in data:
                tree.insert("", "end", values=row)
        else:
            mb.showinfo("Búsqueda", "No se encontraron alumnos en ese curso.")
    else:
        mb.showinfo("Búsqueda", "Ingrese un curso para buscar.")

# Función para buscar al alumno por turno
def buscar_alumno_turno():
    turno_buscar = txtbuscarTurno.get()
    if turno_buscar != "":
        alumno = Alu.Alumno()
        data = alumno.buscar_por_turno(turno_buscar)
        if data:
            tree.delete(*tree.get_children())
            for row in data:
                tree.insert("", "end", values=row)
        else:
            mb.showinfo("Búsqueda", "No se encontraron alumnos en ese curso.")
    else:
        mb.showinfo("Búsqueda", "Ingrese un curso para buscar.")

def ajustar_ancho_columnas(tree):
    tree.column("#0", width=50)
    tree.column("id", width=50)  
    tree.column("nombre", width=150)  
    tree.column("apellido1", width=150)  
    tree.column("apellido2", width=150) 
    tree.column("turno", width=100) 
    tree.column("curso", width=100) 

# Función para mostrar la consulta en la misma ventana
def mostrar_consulta():
    alumno = Alu.Alumno()
    data = alumno.consultar_alumnos()

    if data:
        if hasattr(ven, "tree_frame"):
            ven.tree_frame.destroy()
        ven.tree_frame = Frame(ven)
        ven.tree_frame.place(x=60, y=400)

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

        # Llamar a la función para ajustar el ancho de las columnas
        ajustar_ancho_columnas(tree)
    else:
        mb.showinfo("Consulta", "No hay datos para mostrar.")

def sort_column(tree, col):
    items = [(tree.set(item, col), item) for item in tree.get_children("")]
    items.sort()
    for index, (val, item) in enumerate(items):
        tree.move(item, "", index)

#Elimina un registro de la tabla
def eliminar_registro():
    selected_item = tree.selection()
    if not selected_item:
        mb.showinfo("Eliminar Alumno", "Por favor, seleccione un alumno para eliminar.")
        return
    id_alumno = tree.item(selected_item)["values"][0]
    alumno = Alu.Alumno()
    res = alumno.eliminar_datos(id_alumno)
    if res:
        mb.showinfo('Correcto', 'Se eliminó con éxito el registro')
        limpiar_datos()
        mostrar_consulta()
    else:
        mb.showerror('Error', 'No se ha podido eliminar el registro.')

def eliminar_datos(self, id_alumno):
    try:
        cursor = self.conexion.cursor()
        sql = f"""
            DELETE FROM alumnos 
            WHERE id = {id_alumno}
        """
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Error al eliminar datos:", str(e))
        return False


#funcion editar alumno 
def editar_alumnno():
    selected_item = tree.selection()
    if not selected_item:
        mb.showinfo("Editar Alumno", "Por favor, seleccione un alumno para editar.")
        return
    values = tree.item(selected_item)["values"]
    txtNombre.set(values[1])
    txtApellido.set(values[2])
    txtApellido2.set(values[3])
    txtTurno.set(values[4])
    txtCurso.set(values[5])

# Crear la ventana principal
ven = tk.Tk()
ven.title("Planilla alumnos")

# Centrar verticalmente
posicion_y = (ven.winfo_screenheight() - 1200) // 2
ven.geometry(f"1200x1200+0+{posicion_y}")

##Titulo
Label(ven, text="Información sobre el alumno").place(x=50, y=30)
Label(ven, text="Registro de puntualidad").place(x=760, y=30)

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

# Busqueda por nombre
Label(ven, text="Busqueda nombre: ").place(x=50, y=250)
txtbuscarNombre = tk.StringVar()
Entry(ven, textvariable=txtbuscarNombre).place(x=180, y=250)
# Busqueda por apellido
Label(ven, text="Busqueda apellido: ").place(x=50, y=280)
txtbuscarApellido = tk.StringVar()
Entry(ven, textvariable=txtbuscarApellido).place(x=180, y=280)
# Busqueda por curso
Label(ven, text="Busqueda curso: ").place(x=600, y=250)
txtbuscarCurso = tk.StringVar()
Entry(ven, textvariable=txtbuscarCurso).place(x=720, y=250)
# Busqueda por curso
Label(ven, text="Busqueda turno: ").place(x=600, y=280)
txtbuscarTurno = tk.StringVar()
Entry(ven, textvariable=txtbuscarTurno).place(x=720, y=280)

# Botones
Button(ven, text="Enviar", command=guardar).place(x=600, y=70)
Button(ven, text="Limpiar", command=limpiar_datos).place(x=600, y=130)
Button(ven, text="Consulta", command=mostrar_consulta).place(x=600, y=100)
Button(ven, text="Buscar", command=buscar_alumno_nombre).place(x=400, y=250)
Button(ven, text="Buscar", command=buscar_alumno_apellido).place(x=400, y=280)
Button(ven, text="Buscar", command=buscar_alumno_curso).place(x=1000, y=250)
Button(ven, text="Buscar", command=buscar_alumno_turno).place(x=1000, y=280)
Button(ven, text="Seleccionar alumno", command=editar_alumnno).place(x=600, y=160)
Button(ven, text="Eliminar", command=eliminar_registro).place(x=600, y=190)

# Iniciar la interfaz
ven.mainloop()
