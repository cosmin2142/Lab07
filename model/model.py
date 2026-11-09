from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        biblio_id = None
        if biblioteca and biblioteca != "Nessun filtro":
            try:
                biblio_id = int(biblioteca)
            except ValueError:
                biblio_id = biblioteca
        gen = None
        if genere and genere != "Nessun filtro":
            gen = genere
        if biblio_id is not None and gen is not None:
            return self._libro_dao.read_books_for_generes_in_libraries_from_db(biblio_id, gen)
        elif biblio_id is not None:
            return self._libro_dao.read_books_in_libraries_from_db(biblio_id)
        elif gen is not None:
            return self._libro_dao.read_books_for_generes_from_db(gen)
        else:
            return self._libro_dao.read_books_from_db()

    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        tutti_i_libri = self._libro_dao.read_books_from_db()
        insieme_generi = set()
        for libro in tutti_i_libri:
            insieme_generi.add(libro.genere)
        return insieme_generi

    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        return self._biblioteca_dao.read_libraries_from_db()
