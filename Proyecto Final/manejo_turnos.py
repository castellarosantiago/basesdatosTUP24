import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font
from conexion import BaseDeDatos
from turnos import Turno

# Conectar a la base de datos
db = BaseDeDatos("localhost", "root", "EsromzN4nJWyr8X", "sistema_hospital") #EsromzN4nJWyr8X
db.conectar()
turno_db = Turno(db)

# Crear ventana para programar turno
def mostrar_programar_turno():
    ventana = tk.Toplevel()
    ventana.title("Programar Turno")
    ventana.geometry("600x400")

    ttk.Label(ventana, text="ID Paciente:", style="TLabel").grid(row=0, column=0, pady=5)
    id_paciente_entry = ttk.Entry(ventana)
    id_paciente_entry.grid(row=0, column=1, pady=5)

    ttk.Label(ventana, text="ID Médico:", style="TLabel").grid(row=1, column=0, pady=5)
    id_medico_entry = ttk.Entry(ventana)
    id_medico_entry.grid(row=1, column=1, pady=5)

    ttk.Label(ventana, text="Fecha (YYYY-MM-DD):", style="TLabel").grid(row=2, column=0, pady=5)
    fecha_entry = ttk.Entry(ventana)
    fecha_entry.grid(row=2, column=1, pady=5)

    ttk.Label(ventana, text="Hora (HH:MM):", style="TLabel").grid(row=3, column=0, pady=5)
    hora_entry = ttk.Entry(ventana)
    hora_entry.grid(row=3, column=1, pady=5)

    def programar_turno():
        id_paciente = id_paciente_entry.get()
        id_medico = id_medico_entry.get()
        fecha = fecha_entry.get()
        hora = hora_entry.get()

        try:
            mensaje = turno_db.registrar_turno(id_paciente, id_medico, fecha, hora)
            messagebox.showinfo("Éxito", mensaje)
            ventana.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo programar el turno: {e}")

    ttk.Button(ventana, text="Programar Turno", command=programar_turno, style="Custom.TButton").grid(row=4, columnspan=2, pady=10)

# Crear ventana para actualizar turno
def mostrar_actualizar_turno():
    ventana = tk.Toplevel()
    ventana.title("Actualizar Turno")
    ventana.geometry("600x400")

    ttk.Label(ventana, text="ID Turno:", style="TLabel").grid(row=0, column=0, pady=5)
    id_turno_entry = ttk.Entry(ventana)
    id_turno_entry.grid(row=0, column=1, pady=5)

    ttk.Label(ventana, text="Nueva Fecha (YYYY-MM-DD):", style="TLabel").grid(row=1, column=0, pady=5)
    nueva_fecha_entry = ttk.Entry(ventana)
    nueva_fecha_entry.grid(row=1, column=1, pady=5)

    ttk.Label(ventana, text="Nueva Hora (HH:MM):", style="TLabel").grid(row=2, column=0, pady=5)
    nueva_hora_entry = ttk.Entry(ventana)
    nueva_hora_entry.grid(row=2, column=1, pady=5)

    def actualizar_turno():
        id_turno = id_turno_entry.get()
        nueva_fecha = nueva_fecha_entry.get()
        nueva_hora = nueva_hora_entry.get()

        try:
            mensaje = turno_db.actualizar_turno(id_turno, nueva_fecha, nueva_hora)
            messagebox.showinfo("Éxito", mensaje)
            ventana.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo actualizar el turno: {e}")

    ttk.Button(ventana, text="Actualizar Turno", command=actualizar_turno, style="Custom.TButton").grid(row=3, columnspan=2, pady=10)


#################CHATGPT FULL POWER HABIA QUE CANCELAR INDIVIDUALMENTE POR PACIENTE DIGAMOS O
#  POR MEDICO Y FECHA COMO CANCELACIÓN DE AGENDA COMPLETA SUPONGO POR SI NO PUEDE IR EL MÉDICO
# Crear ventana para cancelar turno
def mostrar_cancelacion_turnos():
    ventana = tk.Toplevel()
    ventana.title("Cancelar Turnos")
    ventana.geometry("600x400")

    # Botones para elegir el método de cancelación
    def cancelar_individual():
        ventana_individual = tk.Toplevel()
        ventana_individual.title("Cancelar Turno Individual")

        ttk.Label(ventana_individual, text="Seleccione el turno a cancelar:", style="TLabel").pack(pady=10)
        
        # Listbox para mostrar turnos disponibles
        listbox = tk.Listbox(ventana_individual, width=60, bg="white", fg="black", font=font)
        listbox.pack(pady=10)

        turnos = turno_db.ver_turnos()
        for turno in turnos:
            listbox.insert(tk.END, f"Turno ID: {turno[0]} - Paciente: {turno[1]} - Médico: {turno[2]} - {turno[3]} {turno[4]}")

        def confirmar_cancelacion():
            seleccion = listbox.curselection()
            if not seleccion:
                messagebox.showwarning("Advertencia", "Debe seleccionar un turno para cancelar.")
                return
            id_turno = turnos[seleccion[0]][0]
            turno_db.cancelar_turno(id_turno)
            messagebox.showinfo("Éxito", f"Turno {id_turno} cancelado con éxito.")
            ventana_individual.destroy()

        ttk.Button(ventana_individual, text="Cancelar Turno", command=confirmar_cancelacion, style="Custom.TButton").pack(pady=10)

    def cancelar_por_rango():
        ventana_rango = tk.Toplevel()
        ventana_rango.title("Cancelar Turnos por Médico y Rango de Fechas")

        ttk.Label(ventana_rango, text="ID del Médico:", style="TLabel").grid(row=0, column=0, pady=5)
        id_medico_entry = ttk.Entry(ventana_rango, style="TEntry")
        id_medico_entry.grid(row=0, column=1, pady=5)

        ttk.Label(ventana_rango, text="Fecha Inicio (YYYY-MM-DD):", style="TLabel").grid(row=1, column=0, pady=5)
        fecha_inicio_entry = ttk.Entry(ventana_rango, style="TEntry")
        fecha_inicio_entry.grid(row=1, column=1, pady=5)

        ttk.Label(ventana_rango, text="Fecha Fin (YYYY-MM-DD):", style="TLabel").grid(row=2, column=0, pady=5)
        fecha_fin_entry = ttk.Entry(ventana_rango, style="TEntry")
        fecha_fin_entry.grid(row=2, column=1, pady=5)

        def confirmar_cancelacion_rango():
            id_medico = id_medico_entry.get()
            fecha_inicio = fecha_inicio_entry.get()
            fecha_fin = fecha_fin_entry.get()

            if not id_medico or not fecha_inicio or not fecha_fin:
                messagebox.showwarning("Advertencia", "Debe completar todos los campos.")
                return

            turno_db.cancelar_turnos_por_medico_y_fecha(id_medico, fecha_inicio, fecha_fin)
            messagebox.showinfo("Éxito", f"Turnos cancelados para el médico {id_medico} entre {fecha_inicio} y {fecha_fin}.")
            ventana_rango.destroy()

        ttk.Button(ventana_rango, text="Cancelar Turnos", command=confirmar_cancelacion_rango, style="Custom.TButton").grid(row=3, columnspan=2, pady=10)

    # Botones principales en la ventana
    ttk.Button(ventana, text="Cancelar Turno Individual", command=cancelar_individual, style="Custom.TButton").pack(pady=10)
    ttk.Button(ventana, text="Cancelar Turnos por Médico y Rango", command=cancelar_por_rango, style="Custom.TButton").pack(pady=10)

# Crear ventana para ver turnos
def mostrar_ver_turnos():
    ventana = tk.Toplevel()
    ventana.title("Ver Turnos")
    ventana.geometry("800x400")

    listbox = tk.Listbox(ventana, width=100)
    listbox.pack(pady=10)

    try:
        turnos = turno_db.ver_turnos()
        for turno in turnos:
            listbox.insert(tk.END, f"ID: {turno[0]} - Paciente: {turno[1]} - Médico: {turno[2]} - Fecha: {turno[3]} - Hora: {turno[4]}")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudieron cargar los turnos: {e}")

def mostrar_reporte_turnos():
    ventana = tk.Toplevel()
    ventana.title("Reporte de turnos")
    ventana.geometry("600x400")

    listbox = tk.Listbox(ventana, width=100)
    listbox.pack(pady=10)
    
    try:
        turnos = turno_db.reporte_medicos_con_mas_turnos()
        for turno in turnos:
            listbox.insert(tk.END, f"Médico: {turno[0]} {turno[1]} - Total de turnos: {turno[2]}")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudieron cargar los turnos: {e}")

    
# Ventana principal
root = tk.Tk()
root.title("Gestión de Turnos")
font = Font(family="Arial", size=12)
root.geometry("600x400")

style = ttk.Style()
style.configure("Custom.TButton", font=font, padding=10)

ttk.Button(root, text="Programar Turno", command=mostrar_programar_turno, style="Custom.TButton").grid(row=0, column=0, pady=10, padx=10, sticky="nsew")
ttk.Button(root, text="Actualizar Turno", command=mostrar_actualizar_turno, style="Custom.TButton").grid(row=1, column=0, pady=10, padx=10, sticky="nsew")
ttk.Button(root, text="Cancelar Turno", command=mostrar_cancelacion_turnos, style="Custom.TButton").grid(row=2, column=0, pady=10, padx=10, sticky="nsew")
ttk.Button(root, text="Ver Turnos", command=mostrar_ver_turnos, style="Custom.TButton").grid(row=3, column=0, pady=10, padx=10, sticky="nsew")
ttk.Button(root, text="Reporte de Turnos", command=mostrar_reporte_turnos, style="Custom.TButton").grid(row=4, column=0, pady=10, padx=10, sticky="nsew")


root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()