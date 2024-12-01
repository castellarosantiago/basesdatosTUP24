from conexion import BaseDeDatos

class Medico:
    def __init__(self, db):
        self.db = db

    def registrar_medico(self, nombre, apellido, matricula, telefono, especialidad):
        query = "INSERT INTO Medicos (nombre, apellido, matricula, telefono, especialidad) VALUES (%s, %s, %s, %s, %s)"
        valores = (nombre, apellido, matricula, telefono, especialidad)
        self.db.ejecutar(query, valores)
        return "Médico registrado con éxito."

    def actualizar_medico(self, medico_id, nombre, apellido, matricula, telefono, especialidad):
        query = "UPDATE Medicos SET nombre=%s, apellido=%s, matricula=%s, telefono=%s, especialidad=%s WHERE medico_id=%s"
        valores = (nombre, apellido, matricula, telefono, especialidad, medico_id)
        self.db.ejecutar(query, valores)
        return "Médico actualizado con éxito."

    def ver_medico(self, medico_id):
        query = "SELECT * FROM Medicos WHERE medico_id = %s"
        return self.db.obtener_datos(query, (medico_id,))
        
    def eliminar_medico(self, medico_id):
        query = "DELETE FROM Medicos WHERE medico_id = %s"
        self.db.ejecutar(query, (medico_id,))
        return "Médico eliminado con éxito."

    def ver_medicos(self):
        query = "SELECT * FROM Medicos"
        return self.db.obtener_datos(query)
        
    def buscar_medico_por_apellido(self, apellido):
        try:
            cursor = self.db.conexion.cursor()
            consulta = """
                SELECT medico_id, nombre, apellido 
                FROM Medicos 
                WHERE LOWER(apellido) LIKE %s
            """
            busqueda = f"{apellido.lower()}%"
            cursor.execute(consulta, (busqueda,))
            
            # Obtener los resultados
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(f"Error al buscar medicos: {e}")
            return []
    
    def buscar_medico_por_especialidad(self, nombre, apellido, especialidad):
        query = "SELECT * FROM Medicos WHERE (nombre LIKE %s) AND (apellido LIKE %s) AND (especialidad LIKE %s)"
        valores = (f"%{nombre}%", f"%{apellido}%", f"%{especialidad}%")
        return self.db.obtener_datos(query, valores)
    
    def buscar_medico_por_matricula(self, nombre, apellido, matricula):
        query = "SELECT * FROM Medicos WHERE (nombre LIKE %s) AND (apellido LIKE %s) AND (matricula LIKE %s)"
        valores = (f"%{nombre}%", f"%{apellido}%", f"%{matricula}%")
        return self.db.obtener_datos(query, valores)