import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_dropdown(self):
        self._view.dd_biblioteca.options.clear()

        biblioteche = self._model.get_biblioteche()
        for b in biblioteche:
            self._view.dd_biblioteca.options.append(ft.dropdown.Option(key=str(b.id), text=b.nome))

        self._view.dd_genere.options.clear()

        generi = self._model.get_generi()
        for g in generi:
            self._view.dd_genere.options.append(ft.dropdown.Option(key=g, text=g))

        self._view.update()

    # CALLBACKS DROPDOWN
    def handle_biblioteca_change(self, e):
        self.biblioteca_selezionata = self._view.dd_biblioteca.value
    def handle_genere_change(self, e):
        self.genere_selezionato = self._view.dd_genere.value

    # AZIONE: MOSTRA LIBRI
    def handle_mostra_libri(self, e):
        id_biblioteca = self._view.dd_biblioteca.value
        genere = self._view.dd_genere.value
        libri = self._model.get_libri_filtrati(id_biblioteca, genere)
        self._view.list_view.controls.clear()
        for libro in libri:
            testo_riga = f"{libro.titolo} - Autore: {getattr(libro, 'autore')} (Genere: {getattr(libro, 'genere')})"
            self._view.list_view.controls.append(ft.Text(testo_riga))

        self._view.update()