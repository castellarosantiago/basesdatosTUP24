import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
import subprocess

#Funciones para abrir las aplicaciones independientes
def abrir_app_pacientes():
    subprocess.Popen(["python", "manejo_pacientes.py"])

def abrir_app_medicos():
    subprocess.Popen(["python", "manejo_medicos.py"])

def abrir_app_turnos():
    subprocess.Popen(["python", "manejo_turnos.py"])
    
def abrir_busqueda_avanzada():
    subprocess.Popen(["python", "busqueda_avanzada.py"])

#Ventana principal
root = tk.Tk()
root.title("Manejador Principal")
root.geometry("600x350")

#Fuente personalizada para los botones
font = Font(family="Arial", size=12)

style = ttk.Style()
style.configure("Custom.TButton", font=font, padding=10)

#Botones principales
ttk.Button(root, text="Pacientes", command=abrir_app_pacientes, style="Custom.TButton").pack(pady=20, fill="x", padx=50)
ttk.Button(root, text="Médicos", command=abrir_app_medicos, style="Custom.TButton").pack(pady=20, fill="x", padx=50)
ttk.Button(root, text="Turnos", command=abrir_app_turnos, style="Custom.TButton").pack(pady=20, fill="x", padx=50)
ttk.Button(root, text="Búsqueda avanzada", command=abrir_busqueda_avanzada, style="Custom.TButton").pack(pady=20, fill="x", padx=50)

root.mainloop()