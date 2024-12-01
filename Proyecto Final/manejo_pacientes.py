import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox
from pacientes import Paciente
from conexion import BaseDeDatos

#Conectar a la base de datos
db = BaseDeDatos("localhost", "root", "EsromzN4nJWyr8X", "sistema_hospital") #EsromzN4nJWyr8X
db.conectar()
paciente_db = Paciente(db)

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
  style.configure(
    "TLabel", 
    foreground="black"
  )
  style.configure("TFrame", background="white")
  style.configure("TEntry", fieldbackground="white", foreground="black")

#Crear ventana de registro de paciente
def mostrar_registro_paciente():
  ventana = tk.Toplevel()
  ventana.title("Registrar paciente")
  ventana.geometry("600x400")

  ttk.Label(ventana, text="Nombre:", style="TLabel").grid(row=0, column=0, pady=5)
  nombre_entry = ttk.Entry(ventana, style="TEntry")
  nombre_entry.grid(row=0, column=1, pady=5)

  ttk.Label(ventana, text="Apellido:", style="TLabel").grid(row=1, column=0, pady=5)
  apellido_entry = ttk.Entry(ventana, style="TEntry")
  apellido_entry.grid(row=1, column=1, pady=5)

  ttk.Label(ventana, text="DNI:", style="TLabel").grid(row=2, column=0, pady=5)
  dni_entry = ttk.Entry(ventana, style="TEntry")
  dni_entry.grid(row=2, column=1, pady=5)

  ttk.Label(ventana, text="Teléfono:", style="TLabel").grid(row=3, column=0, pady=5)
  telefono_entry = ttk.Entry(ventana, style="TEntry")
  telefono_entry.grid(row=3, column=1, pady=5)

  ttk.Label(ventana, text="Email:", style="TLabel").grid(row=4, column=0, pady=5)
  email_entry = ttk.Entry(ventana, style="TEntry")
  email_entry.grid(row=4, column=1, pady=5)

  ttk.Label(ventana, text="Dirección:", style="TLabel").grid(row=5, column=0, pady=5)
  direccion_entry = ttk.Entry(ventana, style="TEntry")
  direccion_entry.grid(row=5, column=1, pady=5)
  
  ttk.Label(ventana, text="Obra Social:", style="TLabel").grid(row=6, column=0, pady=5)
  obra_social_entry = ttk.Entry(ventana, style="TEntry")
  obra_social_entry.grid(row=6, column=1, pady=5)

  def registrar_paciente():
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    dni = dni_entry.get()
    telefono = telefono_entry.get()
    email = email_entry.get()
    direccion = direccion_entry.get()
    obra_social = obra_social_entry.get()

    paciente_db.registrar_paciente(nombre, apellido, dni, telefono, email, direccion, obra_social)
    messagebox.showinfo("Éxito", "Paciente registrado con éxito.")
    ventana.destroy()

  ttk.Button(
    ventana, text="Registrar", command=registrar_paciente, style="Custom.TButton"
  ).grid(row=7, columnspan=2, pady=10)

#Crear ventana de actualización de paciente
def mostrar_actualizacion_paciente():
  ventana = tk.Toplevel()
  ventana.title("Actualizar Paciente")
  ventana.geometry("600x400")

  listbox = tk.Listbox(ventana, width=60, bg="white", fg="black", font=font)
  listbox.pack()

  pacientes = paciente_db.ver_pacientes()
  for paciente in pacientes:
    listbox.insert(tk.END, f"{paciente[0]} - {paciente[1]} {paciente[2]} - {paciente[3]}")

  def actualizar_paciente():
    seleccion = listbox.curselection()
    if not seleccion:
        messagebox.showwarning("Seleccionar Paciente", "Debe seleccionar un paciente para actualizar.")
        return
    paciente_id = pacientes[seleccion[0]][0]

    #Obtener los datos actuales del paciente
    paciente_actual = paciente_db.ver_paciente(paciente_id)[0]

    #Ventana para actualizar los datos del paciente seleccionado
    actualizacion_ventana = tk.Toplevel()
    actualizacion_ventana.title("Actualizar Datos del Paciente")
    actualizacion_ventana.geometry("600x400")

    ttk.Label(actualizacion_ventana, text="Nombre:", style="TLabel").grid(row=0, column=0)
    nombre_entry = ttk.Entry(actualizacion_ventana, style="TEntry")
    nombre_entry.insert(0, paciente_actual[1])  
    nombre_entry.grid(row=0, column=1, pady=5)

    ttk.Label(actualizacion_ventana, text="Apellido:", style="TLabel").grid(row=1, column=0)
    apellido_entry = ttk.Entry(actualizacion_ventana, style="TEntry")
    apellido_entry.insert(0, paciente_actual[2])  #Apellido actual
    apellido_entry.grid(row=1, column=1, pady=5)

    ttk.Label(actualizacion_ventana, text="DNI:", style="TLabel").grid(row=2, column=0)
    dni_entry = ttk.Entry(actualizacion_ventana, style="TEntry")
    dni_entry.insert(0, paciente_actual[3])  #DNI actual
    dni_entry.grid(row=2, column=1, pady=5)

    ttk.Label(actualizacion_ventana, text="Teléfono:", style="TLabel").grid(row=3, column=0)
    telefono_entry = ttk.Entry(actualizacion_ventana, style="TEntry")
    telefono_entry.insert(0, paciente_actual[4])  #Teléfono actual
    telefono_entry.grid(row=3, column=1, pady=5)

    ttk.Label(actualizacion_ventana, text="Email:", style="TLabel").grid(row=4, column=0)
    email_entry = ttk.Entry(actualizacion_ventana, style="TEntry")
    email_entry.insert(0, paciente_actual[5])  #Email actual
    email_entry.grid(row=4, column=1, pady=5)

    ttk.Label(actualizacion_ventana, text="Dirección:", style="TLabel").grid(row=5, column=0)
    direccion_entry = ttk.Entry(actualizacion_ventana, style="TEntry")
    direccion_entry.insert(0, paciente_actual[6]) #Dirección actual
    direccion_entry.grid(row=5, column=1, pady=5)
    
    ttk.Label(actualizacion_ventana, text="Obra Social:", style="TLabel").grid(row=6, column=0)
    obra_social_entry = ttk.Entry(actualizacion_ventana, style="TEntry")
    obra_social_entry.insert(0, paciente_actual[7]) #Obra Social actual
    obra_social_entry.grid(row=6, column=1, pady=5)

    def guardar_cambios():
      nombre = nombre_entry.get()
      apellido = apellido_entry.get()
      dni = dni_entry.get()
      telefono = telefono_entry.get()
      email = email_entry.get()
      direccion = direccion_entry.get()
      obra_social = obra_social_entry.get()
      
      paciente_db.actualizar_paciente(paciente_id, nombre, apellido, dni, telefono, email, direccion, obra_social)
      messagebox.showinfo("Éxito", "Paciente actualizado con éxito.")
      actualizacion_ventana.destroy()

    ttk.Button(actualizacion_ventana, text="Guardar Cambios", command=guardar_cambios, style="Custom.TButton").grid(row=7, columnspan=2)

  ttk.Button(ventana, text="Actualizar Paciente Seleccionado", command=actualizar_paciente, style="Custom.TButton").pack()

#Crear ventana para eliminación de paciente
def mostrar_eliminacion_paciente():
  ventana = tk.Toplevel()
  ventana.title("Eliminar Paciente")

  listbox = tk.Listbox(ventana, width=60, bg="white", fg="black", font=font)
  listbox.pack()

  pacientes = paciente_db.ver_pacientes()
  for paciente in pacientes:
    listbox.insert(tk.END, f"{paciente[0]} - {paciente[1]} {paciente[2]} - {paciente[3]}")

  def eliminar_paciente():
    seleccion = listbox.curselection()
    if not seleccion:
        messagebox.showwarning("Seleccionar Paciente", "Debe seleccionar un paciente para eliminar.")
        return
    paciente_id = pacientes[seleccion[0]][0]

    paciente_db.eliminar_paciente(paciente_id)
    messagebox.showinfo("Éxito", "Paciente eliminado con éxito.")
    listbox.delete(seleccion)

  ttk.Button(ventana, text="Eliminar Paciente Seleccionado", command=eliminar_paciente, style="Custom.TButton").pack()

#Mostrar lista de pacientes
def mostrar_pacientes():
  ventana = tk.Toplevel()
  ventana.title("Ver Pacientes")
  
  listbox = tk.Listbox(ventana, width=60, bg="white", fg="black", font=font)
  listbox.pack()

  for paciente in paciente_db.ver_pacientes():
    listbox.insert(tk.END, f"{paciente[0]} - {paciente[1]} {paciente[2]} - {paciente[3]}")

root = tk.Tk()
root.title("Gestión de Pacientes")
font = Font(family="Arial", size=12)
root.geometry("600x400")

#Establecer un estilo personalizado para los botones
style = ttk.Style()
style.configure("Custom.TButton",  font=font, padding=10)

#Crear los botones y usarlos en el gestor de geometría `grid` con alineación centrada
ttk.Button(root, text="Registrar Paciente",command=mostrar_registro_paciente, style="Custom.TButton").grid(row=0, column=0, pady=10, padx=10, sticky="nsew")
ttk.Button(root, text="Actualizar Paciente",command=mostrar_actualizacion_paciente, style="Custom.TButton").grid(row=1, column=0, pady=10, padx=10, sticky="nsew")
ttk.Button(root, text="Eliminar Paciente", command=mostrar_eliminacion_paciente, style="Custom.TButton").grid(row=2, column=0, pady=10, padx=10, sticky="nsew")
ttk.Button(root, text="Ver Pacientes",command=mostrar_pacientes, style="Custom.TButton").grid(row=3, column=0, pady=10, padx=10, sticky="nsew")

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()