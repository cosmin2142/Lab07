from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def read_books_from_db(self):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            print("Connection established")
            query = "SELECT * FROM libro"
            cursor = cnx.cursor()
            cursor.execute(query)
            result = []
            for row in cursor:
                libri = Libro(*row)
                result.append(libri)
            cursor.close()
            cnx.close()
            return result

    def read_books_in_libraries_from_db(self, biblioteca):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            print("Connection established")
            query = f"SELECT l.* FROM biblioteca as b, libro as l WHERE b.id=l.id_biblioteca AND b.id={biblioteca}"
            cursor = cnx.cursor()
            cursor.execute(query)
            result = []
            for row in cursor:
                libri = Libro(*row)
                result.append(libri)
            cursor.close()
            cnx.close()
            return result

    def read_books_for_generes_from_db(self, genere):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            print("Connection established")
            query = f"SELECT * FROM libro WHERE genere='{genere}'"
            cursor = cnx.cursor()
            cursor.execute(query)
            result = []
            for row in cursor:
                libri = Libro(*row)
                result.append(libri)
            cursor.close()
            cnx.close()
            return result

    def read_books_for_generes_in_libraries_from_db(self, biblioteca, genere):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            print("Connection established")
            query = f"SELECT l.* FROM biblioteca as b, libro as l WHERE b.id=l.id_biblioteca AND b.id={biblioteca} AND l.genere='{genere}'"
            cursor = cnx.cursor()
            cursor.execute(query)
            result = []
            for row in cursor:
                libri = Libro(*row)
                result.append(libri)
            cursor.close()
            cnx.close()
            return result
