import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox
from conexion import BaseDeDatos
from medicos import Medico

#Conectar a la base de datos
db = BaseDeDatos("localhost", "root", "EsromzN4nJWyr8X", "sistema_hospital") #EsromzN4nJWyr8X
db.conectar()
medico_db = Medico(db)

#Estilos personalizados para botones en blanco y negro
def configurar_estilo():
    style = ttk.Style()
    style.configure(
        "Custom.TButton",
        font=font,
        padding=10,
        relief="flat",
        background="white",
        foreground="black",
        borderwidth=0
    )
    style.map(
        "Custom.TButton",
        background=[("active", "gray")],
        relief=[("pressed", "solid")],
    )
    style.configure("TLabel", foreground="black")
    style.configure("TFrame", background="white")
    style.configure("TEntry", fieldbackground="white", foreground="black")

#Crear ventana para registrar médico
def mostrar_registro_medico():
    ventana = tk.Toplevel()
    ventana.title("Registrar Médico")
    ventana.geometry("600x400")

    ttk.Label(ventana, text="Nombre:", style="TLabel").grid(row=0, column=0, pady=5)
    nombre_entry = ttk.Entry(ventana, style="TEntry")
    nombre_entry.grid(row=0, column=1, pady=5)

    ttk.Label(ventana, text="Apellido:", style="TLabel").grid(row=1, column=0, pady=5)
    apellido_entry = ttk.Entry(ventana, style="TEntry")
    apellido_entry.grid(row=1, column=1, pady=5)

    ttk.Label(ventana, text="Matrícula:", style="TLabel").grid(row=2, column=0, pady=5)
    matricula_entry = ttk.Entry(ventana, style="TEntry")
    matricula_entry.grid(row=2, column=1, pady=5)

    ttk.Label(ventana, text="Teléfono:", style="TLabel").grid(row=3, column=0, pady=5)
    telefono_entry = ttk.Entry(ventana, style="TEntry")
    telefono_entry.grid(row=3, column=1, pady=5)

    ttk.Label(ventana, text="Especialidad:", style="TLabel").grid(row=4, column=0, pady=5)
    especialidad_entry = ttk.Entry(ventana, style="TEntry")
    especialidad_entry.grid(row=4, column=1, pady=5)

    def registrar_medico():
        nombre = nombre_entry.get()
        apellido = apellido_entry.get()
        matricula = matricula_entry.get()
        telefono = telefono_entry.get()
        especialidad = especialidad_entry.get()

        medico_db.registrar_medico(nombre, apellido, matricula, telefono, especialidad)
        messagebox.showinfo("Éxito", "Médico registrado con éxito.")
        ventana.destroy()

    ttk.Button(
        ventana, text="Registrar", command=registrar_medico, style="Custom.TButton"
    ).grid(row=5, columnspan=2, pady=10)

#Crear ventana para actualizar médico
def mostrar_actualizacion_medico():
    ventana = tk.Toplevel()
    ventana.title("Actualizar Médico")
    ventana.geometry("600x400")

    listbox = tk.Listbox(ventana, width=60, bg="white", fg="black", font=font)
    listbox.pack()

    medicos = medico_db.ver_medicos()
    for medico in medicos:
        listbox.insert(tk.END, f"{medico[0]} - {medico[1]} {medico[2]}")

    def actualizar_medico():
        seleccion = listbox.curselection()
        if not seleccion:
            messagebox.showwarning("Seleccionar Médico", "Debe seleccionar un médico para actualizar.")
            return
        medico_id = medicos[seleccion[0]][0]

        #Obtener los datos actuales del médico
        medico_actual = medico_db.ver_medico(medico_id)[0]

        #Ventana para actualizar datos del médico seleccionado
        actualizacion_ventana = tk.Toplevel()
        actualizacion_ventana.title("Actualizar Datos del Médico")
        actualizacion_ventana.geometry("600x400")

        ttk.Label(actualizacion_ventana, text="Nombre:", style="TLabel").grid(row=0, column=0)
        nombre_entry = ttk.Entry(actualizacion_ventana, style="TEntry")
        nombre_entry.insert(0, medico_actual[1])  #Nombre actual
        nombre_entry.grid(row=0, column=1, pady=5)

        ttk.Label(actualizacion_ventana, text="Apellido:", style="TLabel").grid(row=1, column=0)
        apellido_entry = ttk.Entry(actualizacion_ventana, style="TEntry")
        apellido_entry.insert(0, medico_actual[2])  #Apellido actual
        apellido_entry.grid(row=1, column=1, pady=5)

        ttk.Label(actualizacion_ventana, text="Matrícula:", style="TLabel").grid(row=2, column=0)
        matricula_entry = ttk.Entry(actualizacion_ventana, style="TEntry")
        matricula_entry.insert(0, medico_actual[3])  #Matrícula actual
        matricula_entry.grid(row=2, column=1, pady=5)

        ttk.Label(actualizacion_ventana, text="Teléfono:", style="TLabel").grid(row=3, column=0)
        telefono_entry = ttk.Entry(actualizacion_ventana, style="TEntry")
        telefono_entry.insert(0, medico_actual[4])  #Teléfono actual
        telefono_entry.grid(row=3, column=1, pady=5)

        ttk.Label(actualizacion_ventana, text="Especialidad:", style="TLabel").grid(row=4, column=0)
        especialidad_entry = ttk.Entry(actualizacion_ventana, style="TEntry")
        especialidad_entry.insert(0, medico_actual[5])  #Especialidad actual
        especialidad_entry.grid(row=4, column=1, pady=5)

        def guardar_cambios():
            nombre = nombre_entry.get()
            apellido = apellido_entry.get()
            matricula = matricula_entry.get()
            telefono = telefono_entry.get()
            especialidad = especialidad_entry.get()

            medico_db.actualizar_medico(medico_id, nombre, apellido, matricula, telefono, especialidad)
            messagebox.showinfo("Éxito", "Médico actualizado con éxito.")
            actualizacion_ventana.destroy()

        ttk.Button(
            actualizacion_ventana, text="Guardar Cambios", command=guardar_cambios, style="Custom.TButton"
        ).grid(row=5, columnspan=2, pady=10)

    ttk.Button(ventana, text="Actualizar Médico Seleccionado", command=actualizar_medico, style="Custom.TButton").pack()

#Crear ventana para eliminar médico
def mostrar_eliminacion_medico():
    ventana = tk.Toplevel()
    ventana.title("Eliminar Médico")

    listbox = tk.Listbox(ventana, width=60, bg="white", fg="black", font=font)
    listbox.pack()

    medicos = medico_db.ver_medicos()
    for medico in medicos:
        listbox.insert(tk.END, f"{medico[0]} - {medico[1]} {medico[2]}")

    def eliminar_medico():
        seleccion = listbox.curselection()
        if not seleccion:
            messagebox.showwarning("Seleccionar Médico", "Debe seleccionar un médico para eliminar.")
            return
        medico_id = medicos[seleccion[0]][0]

        medico_db.eliminar_medico(medico_id)
        messagebox.showinfo("Éxito", "Médico eliminado con éxito.")
        listbox.delete(seleccion)

    ttk.Button(
        ventana, text="Eliminar Médico Seleccionado", command=eliminar_medico, style="Custom.TButton"
    ).pack()

#Crear ventana para ver médicos
def mostrar_medicos():
    ventana = tk.Toplevel()
    ventana.title("Ver Médicos")

    listbox = tk.Listbox(ventana, width=60, bg="white", fg="black", font=font)
    listbox.pack()

    for medico in medico_db.ver_medicos():
        listbox.insert(tk.END, f"{medico[0]} - {medico[1]} {medico[2]} - {medico[5]}")

root = tk.Tk()
root.title("Gestión de Médicos")
font = Font(family="Arial", size=12)
root.geometry("600x400")

#Crear botones
ttk.Button(root, text="Registrar Médico", command=mostrar_registro_medico, style="Custom.TButton").grid(row=0, column=0, pady=10, padx=10, sticky="nsew")
ttk.Button(root, text="Actualizar Médico", command=mostrar_actualizacion_medico, style="Custom.TButton").grid(row=1, column=0, pady=10, padx=10, sticky="nsew")
ttk.Button(root, text="Eliminar Médico", command=mostrar_eliminacion_medico, style="Custom.TButton").grid(row=2, column=0, pady=10, padx=10, sticky="nsew")
ttk.Button(root, text="Ver Médicos", command=mostrar_medicos, style="Custom.TButton").grid(row=3, column=0, pady=10, padx=10, sticky="nsew")

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()