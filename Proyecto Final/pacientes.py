from conexion import BaseDeDatos

class Paciente:
  def __init__(self, db):
    self.db = db

  def registrar_paciente(self, nombre, apellido, dni, telefono, email, direccion, obra_social):
    query = "INSERT INTO Pacientes (nombre, apellido, dni, telefono, email, direccion, obra_social) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    valores = (nombre, apellido, dni, telefono, email, direccion, obra_social)
    self.db.ejecutar(query, valores)
    return "Paciente registrado con éxito."

  def actualizar_paciente(self, paciente_id, nombre, apellido, dni, telefono, email, direccion, obra_social):
    query = "UPDATE Pacientes SET nombre=%s, apellido=%s, dni=%s, telefono=%s, email=%s, direccion=%s, obra_social=%s WHERE paciente_id=%s"
    valores = (nombre, apellido, dni, telefono, email, direccion, obra_social, paciente_id)
    self.db.ejecutar(query, valores)
    return "Paciente actualizado con éxito."

  def ver_paciente(self, paciente_id):
    query = "SELECT * FROM Pacientes WHERE paciente_id = %s"
    return self.db.obtener_datos(query, (paciente_id,))
      
  def eliminar_paciente(self, paciente_id):
    query = "DELETE FROM Pacientes WHERE paciente_id = %s"
    self.db.ejecutar(query, (paciente_id,))
    return "Paciente eliminado con éxito."

  def ver_pacientes(self):
    query = "SELECT * FROM Pacientes"
    return self.db.obtener_datos(query)
  
  def buscar_paciente_por_apellido(self, apellido):
    try:
        cursor = self.db.conexion.cursor()
        consulta = """
            SELECT paciente_id, nombre, apellido 
            FROM pacientes 
            WHERE LOWER(apellido) LIKE %s
        """
        busqueda = f"{apellido.lower()}%"
        cursor.execute(consulta, (busqueda,))
        
        # Obtener los resultados
        resultados = cursor.fetchall()
        return resultados
    except Exception as e:
        print(f"Error al buscar pacientes: {e}")
        return []

  def buscar_paciente_por_dni(self, nombre, apellido, dni):
      query = "SELECT * FROM Pacientes WHERE (nombre LIKE %s) AND (apellido LIKE %s) AND (dni LIKE %s)"
      valores = (f"%{nombre}%", f"%{apellido}%", f"%{dni}%")
      return self.db.obtener_datos(query, valores)