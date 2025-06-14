from ..Connection import get_connection

class Celda:
    def __init__(self, id_celda, tipo, estado="disponible"):
        self.id_celda = id_celda
        self.tipo = tipo
        self.estado = estado

    @staticmethod
    def obtener_disponible(tipo):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT ID_Celda FROM Celda WHERE Tipo = ? AND Estado = 'disponible' LIMIT 1", (tipo,))
        row = cursor.fetchone()
        conn.close()
        return row[0] if row else None

    @staticmethod
    def obtener_disponibles(tipo):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT ID_Celda, Nombre FROM Celda WHERE Tipo = ? AND Estado = 'disponible'", (tipo,))
        rows = cursor.fetchall()
        conn.close()
        # Retorna lista de tuplas (ID_Celda, Nombre)
        return rows if rows else []

    @staticmethod
    def ocupar_celda(nombre):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Celda SET Estado = 'ocupada' WHERE Nombre = ?", (nombre,))
        conn.commit()
        conn.close()

    @staticmethod
    def liberar_celda(nombre):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Celda SET Estado = 'disponible' WHERE Nombre = ?", (nombre,))
        conn.commit()
        conn.close()

    @staticmethod
    def esta_disponible(nombre):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT Estado FROM Celda WHERE Nombre = ?", (nombre,))
        row = cursor.fetchone()
        conn.close()
        return row and row[0] == 'disponible'
