
"""
def mostrar_consulta_asistencia():
    alumno = Alu.Alumno()
    data = alumno.consultar_alumnos()

    if data:
        if hasattr(ven, "tree_frame"):
            ven.tree_frame.destroy()
        ven.tree_frame = Frame(ven)
        ven.tree_frame.place(x=80, y=550)

        global tree
        tree = Treeview(ven.tree_frame)
        tree["columns"] = ("id", "nombre", "apellido1", "presentismo")
        tree.heading("id", text="Id")
        tree.heading("nombre", text="Nombre")
        tree.heading("apellido1", text="Apellido1")
        tree.heading("presentismo", text="Presentismo")

        for row in data:
            # Agregar un Combobox en la última columna (presentismo)
            presentismo_combobox = Combobox(tree, values=["Presente", "Tarde", "Ausente", "Ausente con presente"])
            presentismo_combobox.set(row[-1])  # Establecer el valor del Combobox según los datos
            tree.insert("", "end", values=row[:-1] + (presentismo_combobox,))
            presentismo_combobox.bind("<<ComboboxSelected>>", on_combobox_select)  # Agregar evento

        tree.pack()

        # Llamar a la función para ajustar el ancho de las columnas
        ajustar_ancho_columnas(tree)
    else:
        mb.showinfo("Consulta", "No hay datos para mostrar.")
def on_combobox_select(event):
    selected_item = tree.selection()
    if selected_item:
        combobox_value = event.widget.get()
        id_alumno = tree.item(selected_item)["values"][0]
        alumno = Alu.Alumno()
        res = alumno.actualizar_presentismo(id_alumno, combobox_value)
        if res:
            mb.showinfo('Correcto', 'Se actualizó el presentismo del alumno')
        else:
            mb.showerror('Error', 'No se pudo actualizar el presentismo del alumno')
def actualizar():
    selected_item = tree.selection()
    if not selected_item:
        mb.showinfo("Editar Alumno", "Por favor, seleccione un alumno para editar.")
        return
    id_alumno = tree.item(selected_item)["values"][0]
    alumno = Alu.Alumno()
    res = alumno.editar_datos(
        id=id_alumno,
        nombre=txtNombre.get(),
        apellido1=txtApellido.get(),
        fecha=txtFecha.get(),
        presentismo=txtPresentismo.get()  # Eliminar esta línea
    )
    if res:
        mb.showinfo('Correcto', 'Se guardó con éxito el alumno')
        limpiar_datos()
        mostrar_consulta_alumnos()
    else:
        mb.showerror('Error', 'No se ha podido editar el alumno ingresado.')
"""