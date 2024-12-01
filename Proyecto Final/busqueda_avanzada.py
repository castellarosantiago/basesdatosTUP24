import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from conexion import BaseDeDatos
from tkinter import messagebox
from medicos import Medico
from pacientes import Paciente
from turnos import Turno

# Conectar a la base de datos
db = BaseDeDatos("localhost", "root", "EsromzN4nJWyr8X", "sistema_hospital")
db.conectar()
paciente_db = Paciente(db)
medico_db = Medico(db)
turno_db = Turno(db)

# Mostrar resultados en una nueva ventana
def mostrar_resultados_busqueda(datos, titulo):
    ventana_resultados = tk.Toplevel()
    ventana_resultados.title(titulo)
    ventana_resultados.geometry("400x300")
    
    # Crear un Treeview
    tree = ttk.Treeview(ventana_resultados, columns=("ID", "Nombre", "Apellido"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Apellido", text="Apellido")
    tree.column("ID", width=50, anchor="center")
    tree.column("Nombre", width=150, anchor="center")
    tree.column("Apellido", width=150, anchor="center")
    
    for dato in datos:
      tree.insert("", "end", values=dato)
    
    tree.pack(fill="both", expand=True)

# Ventana de búsqueda de pacientes
def busqueda_avanzada_paciente():
    ventana = tk.Toplevel()
    ventana.title("Búsqueda avanzada de pacientes")
    ventana.geometry("400x300")
    
    tk.Label(ventana, text="Buscar por apellido:").pack(pady=10)
    busqueda_entry = tk.Entry(ventana)
    busqueda_entry.pack(pady=5)
    
    def buscar_paciente():
      texto_busqueda = busqueda_entry.get()
      pacientes = paciente_db.buscar_paciente_por_apellido(texto_busqueda)
      if pacientes:
          mostrar_resultados_busqueda(pacientes, "Pacientes")
      else:
          tk.messagebox.showinfo("Sin resultados", "No se encontraron pacientes.")
  
    tk.Button(ventana, text="Buscar", command=buscar_paciente).pack(pady=10)

def busqueda_avanzada_medico():
  ventana = tk.Toplevel()
  ventana.title("Búsqueda avanzada de médicos")
  ventana.geometry("400x300")
  
  # Etiqueta y campo de entrada para buscar médicos
  tk.Label(ventana, text="Buscar por apellido:").pack(pady=10)
  busqueda_entry = tk.Entry(ventana)
  busqueda_entry.pack(pady=5)
  
  def buscar_medico():
    texto_busqueda = busqueda_entry.get()
    # Llamar al método de la clase Médico para buscar por apellido
    medicos = medico_db.buscar_medico_por_apellido(texto_busqueda)
    if medicos:
        mostrar_resultados_busqueda(medicos, "Médicos")
    else:
        tk.messagebox.showinfo("Sin resultados", "No se encontraron médicos.")
  
  # Botón para realizar la búsqueda
  tk.Button(ventana, text="Buscar", command=buscar_medico).pack(pady=10)

def mostrar_resultados_busqueda_turnos(resultados):
  ventana_resultados = tk.Toplevel()
  ventana_resultados.title("Resultados de búsqueda de turnos")
  ventana_resultados.geometry("600x400")
  
  # Crear el Treeview con las columnas correspondientes
  columnas = ("Id Turno", "Paciente", "Médico")
  tree = ttk.Treeview(ventana_resultados, columns=columnas, show="headings")

  # Definir las cabeceras
  tree.heading("Id Turno", text="Id Turno")
  tree.heading("Paciente", text="Paciente")
  tree.heading("Médico", text="Médico")

  # Establecer el ancho de las columnas
  tree.column("Id Turno", width=100, anchor='w')
  tree.column("Paciente", width=200, anchor='w')
  tree.column("Médico", width=200, anchor='w')

  for turno in resultados:
    tree.insert("", "end", values=(turno[0], f"{turno[1]}", turno[2]))

  # Colocar el Treeview en la ventana
  tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
  
def busqueda_avanzada_turno():
  ventana = tk.Toplevel()
  ventana.title("Búsqueda avanzada de turnos")
  ventana.geometry("400x300")
  
  criterio_var = tk.StringVar(value="medico")
  
  tk.Label(ventana, text="Buscar por:").pack(pady=10)
  tk.Radiobutton(ventana, text="Apellido del Médico", variable=criterio_var, value="medico").pack(pady=5)
  tk.Radiobutton(ventana, text="Apellido del Paciente", variable=criterio_var, value="paciente").pack(pady=5)
  
  tk.Label(ventana, text="Buscar por apellido:").pack(pady=10)
  busqueda_entry = tk.Entry(ventana)
  busqueda_entry.pack(pady=5)
  
  def buscar_turno():
    texto_busqueda = busqueda_entry.get()
    criterio = criterio_var.get()
    
    if criterio == "medico":
      turnos = turno_db.buscar_turnos_por_medico(texto_busqueda)
      if turnos:
        mostrar_resultados_busqueda_turnos(turnos)
      else:
        messagebox.showinfo("Sin resultados", "No se encontraron turnos para ese médico.")
    elif criterio == "paciente":
      turnos = turno_db.buscar_turnos_por_paciente(texto_busqueda)
      if turnos:
        mostrar_resultados_busqueda_turnos(turnos)
      else:
        messagebox.showinfo("Sin resultados", "No se encontraron turnos para ese paciente.")
  
  # Botón para realizar la búsqueda
  tk.Button(ventana, text="Buscar", command=buscar_turno).pack(pady=10)

    
# Configuración principal de la interfaz
root = tk.Tk()
root.title("Búsqueda avanzada")
root.geometry("400x300")

font = Font(family="Arial", size=12)

style = ttk.Style()
style.configure("Custom.TButton", font=font, padding=10)

ttk.Button(root, text="Buscar pacientes", style="Custom.TButton", command=busqueda_avanzada_paciente).pack(pady=20, fill="x", padx=50)
ttk.Button(root, text="Buscar medicos", style="Custom.TButton", command=busqueda_avanzada_medico).pack(pady=20, fill="x", padx=50)
ttk.Button(root, text="Buscar turnos", style="Custom.TButton", command=busqueda_avanzada_turno).pack(pady=20, fill="x", padx=50)


root.mainloop()
