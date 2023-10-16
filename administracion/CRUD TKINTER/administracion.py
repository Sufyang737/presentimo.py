import alumno as Alu
import tkinter as tk
from tkinter.ttk import *
import tkinter.messagebox as mb
from tkcalendar import Calendar

#------------------------------------FUNCIONES----------------------------------------

# Función para guardar los campos
def guardar_alumno():
    if (txtNombre.get() == "" or txtApellido.get() == "" or txtTurno.get() == "" or txtCurso.get() == ""):
        mb.showerror('Verificar', 'El campo no puede estar vacío')
    elif (txtApellido2.get() == ""):
        alumno = Alu.Alumno()
        res = alumno.save_alumno(
            nombre=txtNombre.get(),
            apellido1=txtApellido.get(),
            apellido2= "NULL",
            turno=txtTurno.get(),
            curso=txtCurso.get()
        )
        if res:
            mb.showinfo('Correcto', 'Se guardó con éxito el alumno')
            limpiar_datos()
            mostrar_consulta_alumnos()
        else:
            mb.showerror('Error', 'No se ha podido guardar el alumno ingresado.')
    else:
        # Crear una instancia de la clase Alumno
        alumno = Alu.Alumno()
        res = alumno.save_alumno(
            nombre=txtNombre.get(),
            apellido1=txtApellido.get(),
            apellido2=txtApellido2.get(),
            turno=txtTurno.get(),
            curso=txtCurso.get()

        )
        if res:
            mb.showinfo('Correcto', 'Se guardó con éxito el alumno')
            limpiar_datos()
            mostrar_consulta_alumnos()
        else:
            mb.showerror('Error', 'No se ha podido guardar el alumno ingresado.')

def guardar_asistencia():
    if (txtFecha.get()=="" or txtPresentismo.get()==""):
        mb.showerror('Verificar', 'El campo no puede estar vacío')
    else:
        # Crear una instancia de la clase Alumno
        alumno = Alu.Alumno()
        res = alumno.save_asistencia(
            fecha=txtFecha.get(),
            presentismo=txtPresentismo.get()
        )
        if res:
            mb.showinfo('Correcto', 'Se guardó con éxito el alumno')
            limpiar_datos()
            mostrar_consulta_asistencia()
        else:
            mb.showerror('Error', 'No se ha podido guardar el alumno ingresado.')

def limpiar_datos():
    txtNombre.set("")
    txtApellido.set("")
    txtApellido2.set("")
    txtTurno.set("")
    txtCurso.set("")
    txtFecha.set("")
    txtPresentismo.set("")

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

# Función para buscar al alumno por presentismo
def buscar_alumno_presentismo():
    presentismo_buscar = txtbuscarPresentismo.get()
    if presentismo_buscar != "":
        alumno = Alu.Alumno()
        data = alumno.buscar_por_presentismo(presentismo_buscar)
        if data:
            tree.delete(*tree.get_children())
            for row in data:
                tree.insert("", "end", values=row)
        else:
            mb.showinfo("Búsqueda", "No se encontraron alumnos con esa condición.")
    else:
        mb.showinfo("Búsqueda", "Ingrese una condi para buscar.")

# Función para buscar al alumno por fecha
def buscar_alumno_fecha():
    fecha_buscar = txtbuscarFecha.get()
    if fecha_buscar != "":
        alumno = Alu.Alumno()
        data = alumno.buscar_por_fecha(fecha_buscar)
        if data:
            tree.delete(*tree.get_children())
            for row in data:
                tree.insert("", "end", values=row)
        else:
            mb.showinfo("Búsqueda", "No se encontraron alumnos en esa fecha.")
    else:
        mb.showinfo("Búsqueda", "Ingrese una fecha para buscar.")

# Función para buscar al alumno por curso
def buscar_alumno_asistencia():
    curso_buscar = txtSeleccionarCurso.get()
    mostrar_consulta_asistencia()
    if curso_buscar != "":
        alumno = Alu.Alumno()
        data = alumno.buscar_por_asistencia(curso_buscar)
        if data:
            tree.delete(*tree.get_children())
            for row in data:
                tree.insert("", "end", values=row)
        else:
            mb.showinfo("Búsqueda", "No se encontraron registros en esa division.")
    else:
        mb.showinfo("Búsqueda", "Ingrese un curso para buscar.")

def ajustar_ancho_columnas_base(tree):
    tree.column("#0", width=0)
    tree.column("id", width=20)  
    tree.column("nombre", width=80)  
    tree.column("apellido1", width=100)  
    tree.column("apellido2", width=100) 
    tree.column("turno",  width=90) 
    tree.column("curso", width=60)
    #tree.column("Presentismo", width=70)
    #tree.column("Fecha", width=70)

def ajustar_ancho_columnas_asistencia(tree2):
    tree2.column("#0", width=0)
    tree2.column("id", width=10)  
    tree2.column("nombre", width=10)  
    tree2.column("apellido1", width=10)  
    tree2.column("Fecha", width=10)
    tree2.column("Presentismo", width=10)

# Función para mostrar la consulta en la misma ventana
def mostrar_consulta_alumnos():
    alumno = Alu.Alumno()
    data = alumno.consultar_alumnos()

    if data:
        if hasattr(ven, "tree_frame"):
            ven.tree_frame.destroy()
        ven.tree_frame = Frame(ven)
        ven.tree_frame.place(x=230, y=30)

        global tree
        tree = Treeview(ven.tree_frame)
        tree["columns"] = ("id","nombre", "apellido1", "apellido2", "curso", "turno")
        tree.heading("id", text="Id")
        tree.heading("nombre", text="Nombre")
        tree.heading("apellido1", text="Apellido1")
        tree.heading("apellido2", text="Apellido2")
        tree.heading("curso", text="Curso")
        tree.heading("turno", text="Turno")

        

        for row in data:
            tree.insert("", "end", values=row)

        tree.pack()

        # Llamar a la función para ajustar el ancho de las columnas
        ajustar_ancho_columnas_base(tree)
    else:
        mb.showinfo("Consulta", "No hay datos para mostrar.")

def mostrar_consulta_asistencia():
    alumno = Alu.Alumno()
    data = alumno.consultar_asistencia()

    if data:
        if hasattr(ven, "tree_slice"):
            ven.tree_slice.destroy()
        ven.tree_slice = Frame(ven)
        ven.tree_slice.place(x=120,y=300)#Ubicacion de la tabla

        global tree2
        tree2 = Treeview(ven.tree_slice)
        tree2["columns"] = ("nombre", "apellido1", "Fecha")
        tree2.heading("nombre", text="Nombre")
        tree2.heading("apellido1", text="Apellido1")
        tree2.heading("Fecha", text="Fecha")

        for row in data:
            tree2.insert("", "end", values=row)

        tree2.pack()

        # Llamar a la función para ajustar el ancho de las columnas
        ajustar_ancho_columnas_asistencia(tree2)
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
        mostrar_consulta_alumnos()
    else:
        mb.showerror('Error', 'No se ha podido eliminar el registro.')



def actualizar():
    selected_item = tree.selection()
    if not selected_item:
        mb.showinfo("Eliminar Alumno", "Por favor, seleccione un alumno para eliminar.")
        return
    id_alumno = tree.item(selected_item)["values"][0]
    alumno =  Alu.Alumno()
    res = alumno.editar_datos_alumnos(
            id=id_alumno,
            nombre=txtNombre.get(),
            apellido1=txtApellido.get(),
            apellido2=txtApellido2.get(),
            turno=txtTurno.get(),
            curso=txtCurso.get(),
            fecha=txtFecha.get(),
            presentismo=txtPresentismo.get()
        )
    if res:
            mb.showinfo('Correcto', 'Se guardó con éxito el alumno')
            limpiar_datos()
            mostrar_consulta_alumnos()
    else:
            mb.showerror('Error', 'No se ha podido editar el alumno ingresado.')
"""
def actualizar_fecha():
    selected_item = tree.selection()
    if not selected_item:
        mb.showinfo("Eliminar Alumno", "Por favor, seleccione un alumno para eliminar.")
        return
    id_alumno = tree.item(selected_item)["values"][0]
    alumno =  Alu.Alumno()
    res = alumno.editar_datos_asistencia(
            id=id_alumno,
            curso=txtCurso.get(),
            fecha=txtFecha.get(),
            presentismo=txtPresentismo.get()
        )
    if res:
            mb.showinfo('Correcto', 'Se guardó con éxito el registro')
            limpiar_datos()
            mostrar_consulta_asistencia()
    else:
            mb.showerror('Error', 'No se ha podido editar el alumno ingresado.')
"""
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
    txtTurno.set(values[5])
    txtCurso.set(values[4])
    txtFecha.set(values[6])
    txtPresentismo.set(values[7])
    
#funcion para obtener la fecha
def obtener_fecha():
    fecha_seleccionada = cal.get_date()
    txtFecha.set(fecha_seleccionada)

#------------------------------------TKINTER--------------------------------------

# Crear la ventana principal
ven = tk.Tk()
ven.title("Planilla alumnos")

# Crear una etiqueta para mostrar la opción seleccionada
etiqueta = tk.Label(ven, text="")
etiqueta.pack()

# Creacion de marcos para el entorno viusal
marco1 = tk.LabelFrame(ven, width=700, height=500, border=3, relief="groove")
marco1.place(x=10, y=20)
marco2 = tk.LabelFrame(ven, width=700, height=500, border=3, relief="raised")
marco2.place(x=720, y=20)
"""
marco3 = tk.LabelFrame(ven, width=1090, height=160, border=3, relief="sunken")
marco3.place(x=30, y=380)
"""

# Centrar verticalmente
posicion_y = (ven.winfo_screenheight() - 1200 // 2)
ven.geometry(f"1200x1200+0+{posicion_y}")

##Titulo
Label(ven, text="Cargar alumno").place(x=20, y=30)
Label(ven, text="Registro de puntualidad").place(x=720, y=30)

# Campos de registro
regnom = tk.Label(ven, text="Nombre:").place(x=20, y=70)
txtNombre = tk.StringVar()
Entry(ven, textvariable=txtNombre).place(x=80, y=70)

rega1 = tk.Label(ven, text="Apellido1:").place(x=20, y=100)
txtApellido = tk.StringVar()
Entry(ven, textvariable=txtApellido).place(x=80, y=100)

rega2 = tk.Label(ven, text="Apellido2:").place(x=20, y=130)
txtApellido2 = tk.StringVar()
Entry(ven, textvariable=txtApellido2).place(x=80, y=130)

Label(ven, text="Turno: ").place(x=20, y=160)
txtTurno = Combobox(ven, values=["Mañana", "Tarde", "Vespertino"], width=17)
txtTurno.place(x=80, y=160)

Label(ven, text="Curso:").place(x=20, y=190)
txtCurso = Combobox(ven, values=['4to1da','4to2da','4to3da',
                                '5to1da','5to2da','5to3da',
                                '6to1da','6to2da','6to3da'], width=17)
txtCurso.place(x=80, y=190)
"""
# Centro de ayuda
Label(ven, text="Centro de ayuda").place(x=50, y=370)
"""

#Registro de puntualidad
Label(ven, text='Fecha: ').place(x=740, y=70)
txtFecha = tk.StringVar()
Entry(ven, textvariable=txtFecha).place(x=820, y=70)
Label(ven, text="Presentismo: ").place(x=740, y=100)
txtPresentismo = Combobox(ven, values=["Presente", "Ausente", "Tarde"], width=17)
txtPresentismo.place(x=820, y=100)
Label(ven, text="Curso: ").place(x=740, y=130)
txtSeleccionarCurso= Combobox(ven, values=['4to1da','4to2da','4to3da',
                                            '5to1da','5to2da','5to3da',
                                            '6to1da','6to2da','6to3da'], width=50)
txtSeleccionarCurso.place(x=820, y=130, width=100)
"""
# Busqueda por nombre
Label(ven, text="Busqueda nombre: ").place(x=50, y=420)
txtbuscarNombre = tk.StringVar()
Entry(ven, textvariable=txtbuscarNombre).place(x=180, y=420)
# Busqueda por apellido
Label(ven, text="Busqueda apellido: ").place(x=50, y=450)
txtbuscarApellido = tk.StringVar()
Entry(ven, textvariable=txtbuscarApellido).place(x=180, y=450)
# Busqueda por curso
Label(ven, text="Busqueda curso: ").place(x=600, y=420)
txtbuscarCurso = tk.StringVar()
Entry(ven, textvariable=txtbuscarCurso).place(x=720, y=420)
# Busqueda por curso
Label(ven, text="Busqueda turno: ").place(x=600, y=450)
txtbuscarTurno = tk.StringVar()
Entry(ven, textvariable=txtbuscarTurno).place(x=720, y=450)
# Busqueda por presentismo
Label(ven, text="Busqueda presentismo: ").place(x=50, y=480)
txtbuscarPresentismo = tk.StringVar()
Entry(ven, textvariable=txtbuscarPresentismo).place(x=180, y=480)
# Busqueda por fecha
Label(ven, text="Busqueda fecha: ").place(x=600, y=480)
txtbuscarFecha = tk.StringVar()
Entry(ven, textvariable=txtbuscarFecha).place(x=720, y=480)
"""
# Botones
enviar = tk.Button(ven, text="Enviar", command=guardar_alumno, fg='green').place(x=20, y=220, width=100)
enviar = tk.Button(ven, text="Enviar", command=guardar_asistencia, fg='green').place(x=20, y=430, width=100)
editar = tk.Button(ven, text="Editar", command=actualizar, fg='green').place(x=20, y=250, width=100)
mostrar_base = tk.Button(ven, text="Consulta", command=mostrar_consulta_alumnos, fg='maroon').place(x=20, y=280, width=100)
mostrar_asistencia = tk.Button(ven, text="Tabla", command=mostrar_consulta_asistencia, fg='maroon').place(x=960, y=128, width=100)

limpiar = tk.Button(ven, text="Limpiar", command=limpiar_datos, fg='gold').place(x=20, y=310, width=100)
selec = tk.Button(ven, text="Seleccionar", command=editar_alumnno, fg='gray').place(x=20, y=340, width=100)
eliminar = tk.Button(ven, text="Eliminar", command=eliminar_registro, fg='red').place(x=20, y=370, width=100)


"""
bsc1 = tk.Button(ven, text="Buscar", command=buscar_alumno_nombre).place(x=400, y=420)
bsc2 = tk.Button(ven, text="Buscar", command=buscar_alumno_apellido).place(x=400, y=450)
bsc3 = tk.Button(ven, text="Buscar", command=buscar_alumno_curso).place(x=940, y=420)
bsc4 = tk.Button(ven, text="Buscar", command=buscar_alumno_turno).place(x=940, y=450)
bsc5 = tk.Button(ven, text="Buscar", command=buscar_alumno_presentismo).place(x=400, y=480)
bsc6 = tk.Button(ven, text="Buscar", command=buscar_alumno_fecha).place(x=940, y=480)
"""


# Calendario
cal = Calendar(ven, selectmode="day", date_pattern="dd/mm/yyyy")
cal.place(x=740,y=160)

# Botón para obtener la fecha seleccionada
boton_obtener_fecha = tk.Button(ven, text="Seleccionar Fecha", command=obtener_fecha, width=35)
boton_obtener_fecha.place(x=740,y=350)


# Iniciar la interfaz
ven.mainloop()